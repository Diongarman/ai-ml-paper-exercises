#!/usr/bin/env python3
"""Validate roadmap.json and maintain curriculum text without editing personal work.

--write regenerates ROADMAP.md, the README index and managed exercise briefs.
--check is read-only and exits nonzero for mismatches. Neither contacts Google Sheets.
"""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- BEGIN GENERATED CURRICULUM -->'
END = '<!-- END GENERATED CURRICULUM -->'
INDEX_START = '<!-- BEGIN GENERATED EXERCISE INDEX -->'
INDEX_END = '<!-- END GENERATED EXERCISE INDEX -->'


def validate(data):
    papers = {p['id']: p for p in data['papers']}
    exercises = {e['id']: e for e in data['exercises']}
    assert len(papers) == len(data['papers']), 'Duplicate paper ID'
    assert len(exercises) == len(data['exercises']), 'Duplicate exercise ID'
    assert len({e['path'] for e in exercises.values()}) == len(exercises), 'Duplicate folder'
    broad = data['broad_sequence']
    assert len(set(broad)) == len(broad), 'Duplicate broad-sequence paper'
    assert all(pid in papers for pid in broad), 'Unknown broad-sequence paper'
    for p in papers.values():
        assert p['url'].startswith('https://'), p['id']
        assert len(set(p['exercise_ids'])) == len(p['exercise_ids']), p['id']
        for eid in p['exercise_ids']:
            assert eid in exercises and p['id'] in exercises[eid]['paper_ids'], (p['id'], eid)
    for e in exercises.values():
        assert re.fullmatch(r'exercises/E\d{2}-[a-z0-9-]+', e['path']), e['id']
        assert e['path'].split('/')[1].startswith(e['id'] + '-'), e['id']
        assert e['implementation'].count('Hand: ') == 1, e['id']
        assert e['implementation'].count('\nCode: ') == 1, e['id']
        for pid in e['paper_ids']:
            assert pid in papers and e['id'] in papers[pid]['exercise_ids'], (e['id'], pid)
        for pre in e.get('prerequisite_exercise_ids', []):
            assert pre in exercises and pre != e['id'], (e['id'], pre)
        if e.get('prerequisite_exercise_ids'):
            assert e['implementation'].startswith('Prerequisites: ' + ', '.join(e['prerequisite_exercise_ids']) + '.\n'), e['id']
    def visit(eid, chain):
        assert eid not in chain, f'Prerequisite cycle: {chain + [eid]}'
        for pre in exercises[eid].get('prerequisite_exercise_ids', []):
            visit(pre, chain + [eid])
    for eid in exercises:
        visit(eid, [])
    assert len({t['track'] for t in data['tracks']}) == len(data['tracks'])
    for track in data['tracks']:
        assert all(pid in papers for pid in track['paper_ids']), track['track']
        assert all(eid in exercises for eid in track['exercise_ids']), track['track']
        assert len(set(track['paper_ids'])) == len(track['paper_ids']), track['track']
        assert len(set(track['exercise_ids'])) == len(track['exercise_ids']), track['track']
    for placement in data['placements']:
        assert all(pid in papers for pid in placement['paper_ids'])
    # Learning prerequisites that motivated this update.
    for first, second in [('P029', 'P077'), ('P077', 'P079'), ('P080', 'P035'), ('P081', 'P043'), ('P043', 'P048'), ('P017', 'P083'), ('P083', 'P048'), ('P084', 'P048'), ('P048', 'P085'), ('P076', 'P082'), ('P082', 'P066')]:
        assert broad.index(first) < broad.index(second), (first, second)
    return papers, exercises


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', '<br>')


def exercise_link(exercise, prefix=''):
    return f"[{exercise['id']}]({prefix}{exercise['path']}/)"


def brief(data, e, papers):
    row = int(e['id'][1:]) + 1
    url = data['spreadsheet_url'] + f"#gid={data['sheet_ids']['Exercises']}&range=A{row}:K{row}"
    hand = e['implementation'].split('Hand: ', 1)[1].split('\nCode: ', 1)[0]
    code = e['implementation'].split('\nCode: ', 1)[1]
    pre = e.get('prerequisite_exercise_ids', [])
    pre_text = ('\n**Prerequisites:** ' + ', '.join(exercise_link(next(x for x in data['exercises'] if x['id'] == eid), '../../') for eid in pre) + '\n') if pre else ''
    related = '\n'.join(f"- **{pid}:** [{papers[pid]['title']}]({papers[pid]['url']})" for pid in e['paper_ids'])
    return f'''# {e['id']} — {e['title']}

[Exercise row in the spreadsheet]({url}) · [Repository guide](../../README.md) · [Reading order](../../ROADMAP.md)

**Stage:** {e['stage']}  
**Suggested effort:** {e['effort']}  
**Suggested stack:** {e['stack']}
{pre_text}
This is an unsolved starter workspace. Its curriculum brief matches roadmap.json and the spreadsheet; keep your progress status in the spreadsheet. Curriculum version: {data['curriculum_version']}.

## Related papers

{related}

## Work by hand

{hand}

## Implement and investigate

{code}

## Requested deliverables

{e['deliverables']}

Use [notes.md](notes.md) for explanations and worked mathematics. Save small results in results/ and plots in figures/, or keep the brief's filenames beside your script. Link to handwritten workings if you prefer writing them elsewhere.
'''


def execution_record():
    return '''
## How to run

Add the exact commands after you create an implementation. No runnable implementation has been added yet.

- Python version:
- Dependencies and installed versions:
- Dataset/source and split, if relevant:
- Random seed:
- Command or notebook execution steps:

## Results and limitations

Record the observed outputs, comparison with your hand calculation or baseline, and the limits of what the experiment demonstrates. Link to the saved figures/results.
'''


def notes(data, e):
    row = int(e['id'][1:]) + 1
    hand = e['implementation'].split('Hand: ', 1)[1].split('\nCode: ', 1)[0]
    url = data['spreadsheet_url'] + f"#gid={data['sheet_ids']['Exercises']}&range=A{row}:K{row}"
    return f'''# {e['id']} — Working notes

[Exercise brief](README.md) · [Spreadsheet exercise row]({url})

## The idea in my own words

Write the central idea and why it matters. Distinguish the paper's claims from this exercise's simplified demonstration.

## Worked calculation or sketch

{hand}

_Add your derivation, sketch, or a link to handwritten workings here._

## Implementation choices

Explain the representation, assumptions, and any changes to the exercise brief.

## Results and interpretation

Link to your figures or result files and explain what you learned from them.

## Mistakes and limitations

Record an error, failed approach, unexpected result, or boundary of the demonstration.

## Questions to revisit

Record the next question you would investigate.
'''


def roadmap(data, papers, exercises):
    out = [
        '# AI and ML paper reading roadmap', '',
        f"**{len(papers)} papers · {len(exercises)} exercises · {len(data['tracks'])} tracks · {len(data['broad_sequence'])} broad steps.** Curriculum version: {data['curriculum_version']}.", '',
        f"[Live spreadsheet]({data['spreadsheet_url']}) · [Exercise workspaces](README.md#exercise-index) · [Shared curriculum data](roadmap.json)", '',
        data['order_note'], '',
        'The Papers tab retains stable ID order, so P076–P085 are appended there. The broad sequence and deeper paths below show their learning order. Years use the cited publication year for proceedings/journals, or first preprint year for arXiv papers.', '',
        '## Broad sequence', '',
        '| Step | Paper | Year | Exercises |', '| --- | --- | --- | --- |',
    ]
    for step, pid in enumerate(data['broad_sequence'], 1):
        p = papers[pid]
        links = ', '.join(exercise_link(exercises[eid]) for eid in p['exercise_ids']) or '—'
        out.append(f"| {step} | **{pid}** [{cell(p['title'])}]({p['url']}) | {p['year']} | {links} |")
    out += ['', '## Placement guide', '', '| Papers | Placement | Reason |', '| --- | --- | --- |']
    for p in data['placements']:
        out.append('| ' + ' | '.join([', '.join(p['paper_ids']), p['placement'], p['reason']]) + ' |')
    out += ['', '## Deeper paths', '']
    for t in data['tracks']:
        out += ['### ' + t['track'], '', t['teaches'], '', '**Paper order:** ' + ' → '.join(t['paper_ids']), '', '**Exercises:** ' + ', '.join(exercise_link(exercises[eid]) for eid in t['exercise_ids']), '']
    out += ['## Complete paper catalogue', '', 'Full authors, topics and learning rationale are also in roadmap.json and the spreadsheet. Personal reading dates, notes and status stay in the spreadsheet.', '', '| ID | Year | Paper | Track | Tier | Exercises |', '| --- | --- | --- | --- | --- | --- |']
    for p in data['papers']:
        links = ', '.join(exercise_link(exercises[eid]) for eid in p['exercise_ids']) or '—'
        out.append(f"| {p['id']} | {p['year']} | [{cell(p['title'])}]({p['url']}) | {cell(p['track'])} | {p['tier']} | {links} |")
    out += ['', '## Keeping the two copies aligned', '',
        'roadmap.json contains the shared curriculum: paper metadata, exercise briefs, relationships, broad order and deeper paths. It excludes personal status, reading dates and notes. The spreadsheet holds that progress; exercise notes.md files and execution/results sections hold your own work.', '',
        'For a curriculum change, edit roadmap.json, run `python scripts/sync_roadmap.py --write`, then `python scripts/sync_roadmap.py --check`. Apply the same fields to the existing spreadsheet by stable ID, preserving tracking columns, and compare the spreadsheet readback with the manifest. Include reading paths, inverse paper/exercise mappings and Work links in that comparison.', '',
        'The script validates and regenerates repository content. It does not connect to Google Sheets or automatically synchronize future edits. Personal exercise notes and the execution/results sections are preserved by generation.', '']
    return '\n'.join(out)


def index(data):
    out = [INDEX_START, '| Exercise | Focus | Stage | Suggested effort |', '| --- | --- | --- | --- |']
    for e in data['exercises']:
        out.append(f"| {exercise_link(e)} | {cell(e['title'])} | {cell(e['stage'])} | {e['effort']} |")
    return '\n'.join(out + [INDEX_END])


def replace_region(text, start, end, replacement):
    assert text.count(start) == text.count(end) == 1, 'Missing or duplicate generation markers'
    a, rest = text.split(start, 1)
    _, z = rest.split(end, 1)
    return a + replacement + z


def generated_files(data):
    papers, exercises = validate(data)
    outputs = {ROOT / 'ROADMAP.md': roadmap(data, papers, exercises)}
    readme = (ROOT / 'README.md').read_text()
    outputs[ROOT / 'README.md'] = replace_region(readme, INDEX_START, INDEX_END, index(data))
    for e in data['exercises']:
        folder = ROOT / e['path']
        path = folder / 'README.md'
        content = brief(data, e, papers)
        managed = START + '\n' + content + END
        if path.exists():
            old = path.read_text()
            if START in old:
                new = replace_region(old, START, END, managed)
            else:
                assert '\n## How to run\n' in old, f'Cannot safely migrate {path}'
                # Preserve the entire personal execution/results area verbatim.
                new = managed + '\n' + old[old.index('\n## How to run\n'):]
        else:
            new = managed + '\n' + execution_record()
        outputs[path] = new
        notes_path = folder / 'notes.md'
        if not notes_path.exists():
            outputs[notes_path] = notes(data, e)
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--write', action='store_true')
    args = parser.parse_args()
    data = json.loads((ROOT / 'roadmap.json').read_text())
    outputs = generated_files(data)
    changed = [p for p, content in outputs.items() if not p.exists() or p.read_text() != content]
    if args.write:
        for p in changed:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(outputs[p])
        print(f'Updated {len(changed)} generated files; personal notes and execution records preserved.')
    elif changed:
        print('Curriculum files differ; run python scripts/sync_roadmap.py --write:', file=sys.stderr)
        for p in changed:
            print(p.relative_to(ROOT), file=sys.stderr)
        return 1
    print(f"Validated {len(data['papers'])} papers, {len(data['exercises'])} exercises, {len(data['broad_sequence'])} broad steps and {len(data['tracks'])} tracks.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
