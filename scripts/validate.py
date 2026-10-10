"""Validate repository artifacts; optionally build the allowlisted runtime archive."""

import argparse
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ('SKILL.md', 'LICENSE', 'agents/openai.yaml')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def payload(root):
    paths = [root / name for name in RUNTIME]
    paths.extend(sorted((root / 'references').glob('*.md')))
    require(len(paths) == 10, 'Expected seven runtime references and three root/metadata files')
    for path in paths:
        require(path.is_file(), f'Missing runtime file: {path.relative_to(root)}')
        require(path.resolve().is_relative_to(root.resolve()), f'Runtime path escapes repository: {path.name}')
        content = path.read_text(encoding='utf-8')
        require(bool(content.strip()), f'Empty runtime file: {path.name}')
        require(not re.search(r'(?:[A-Z]:[/\\]Users[/\\]|/home/[^/\s]+/|/Users/[^/\s]+/|codex://threads/)', content),
                f'Private path/chat reference in runtime file: {path.name}')
    return paths


def check_links(root, paths):
    for path in paths:
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if '://' in target or target.startswith('#'):
                continue
            local = target.split('#', 1)[0]
            if local:
                destination = (path.parent / local).resolve()
                require(destination.is_relative_to(root.resolve()) and destination.is_file(),
                        f'Broken or escaping link in {path.relative_to(root)}: {target}')


def validate(root):
    paths = payload(root)
    skill = (root / 'SKILL.md').read_text(encoding='utf-8')
    front = re.match(r'\A---\r?\n(.*?)\r?\n---\r?\n', skill, re.DOTALL)
    require(front is not None, 'Missing SKILL.md frontmatter')
    require(re.search(r'^name: test-critic$', front[1], re.MULTILINE), 'Skill name must be test-critic')
    description = re.search(r'^description: >-?\n((?:  .+\n?)*)', front[1], re.MULTILINE)
    require(description is not None, 'Expected folded description in frontmatter')
    text = ' '.join(line.strip() for line in description[1].splitlines())
    require(0 < len(text) <= 269 and '<' not in text and '>' not in text,
            'Description must remain at most half the original 538 characters, without angle brackets')
    require(len(skill[front.end():].splitlines()) <= 500, 'Skill body exceeds 500 lines')
    documents = list(root.glob('*.md')) + list((root / 'evals').rglob('*.md'))
    check_links(root, [*paths, *documents])
    for path in (root / 'evals').glob('*.json'):
        json.loads(path.read_text(encoding='utf-8'))
    cases = json.loads((root / 'evals/evals.json').read_text(encoding='utf-8'))['evals']
    require(len({case['id'] for case in cases}) == len(cases), 'Duplicate eval IDs')
    for case in cases:
        require(bool(case['expectations']), f'No expectations for eval {case["id"]}')
        for file in case['files']:
            path = (root / file).resolve()
            require(path.is_relative_to(root.resolve()) and path.is_file(), f'Missing/escaping eval fixture: {file}')
    return paths


def build(root, paths):
    archive = root / 'dist/test-critic.skill'
    archive.parent.mkdir(exist_ok=True)
    require(archive.parent.resolve().is_relative_to(root.resolve()), 'Archive directory escapes repository')
    require(not archive.is_symlink(), 'Archive target cannot be a symlink')
    entries = {'test-critic/' + path.relative_to(root).as_posix(): path for path in paths}
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as output:
        for entry, path in entries.items():
            output.write(path, entry)
    with zipfile.ZipFile(archive) as output:
        require(output.testzip() is None, 'Archive CRC failure')
        require(set(output.namelist()) == set(entries), 'Archive includes unintended files')
        for entry, path in entries.items():
            require(output.read(entry) == path.read_bytes(), f'Archive differs from source: {entry}')
    return archive


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', action='store_true', help='Build dist/test-critic.skill')
    args = parser.parse_args()
    try:
        paths = validate(ROOT)
        print(f'PASS: frontmatter, {len(paths)} runtime files, links and eval fixtures')
        if args.package:
            print(f'PASS: byte-verified archive at {build(ROOT, paths)}')
    except (ValueError, OSError, KeyError, json.JSONDecodeError, zipfile.BadZipFile) as error:
        parser.exit(1, f'FAIL: {error}\n')


if __name__ == '__main__':
    main()
