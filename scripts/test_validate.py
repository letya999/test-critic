"""Check publication boundaries with disposable copies, never runtime execution."""

import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path

from validate import ROOT, build, validate


class PublicationChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('SKILL.md', 'LICENSE', 'agents', 'references', 'evals'):
            source = ROOT / name
            destination = self.root / name
            if source.is_dir():
                shutil.copytree(source, destination)
            else:
                shutil.copy2(source, destination)

    def test_package_excludes_authoring_and_private_state(self):
        (self.root / '.eval-work').mkdir()
        (self.root / '.eval-work/private.txt').write_text('local context', encoding='utf-8')
        archive = build(self.root, validate(self.root))
        with zipfile.ZipFile(archive) as output:
            entries = set(output.namelist())
            self.assertIn('test-critic/LICENSE', entries)
            self.assertIn('test-critic/SKILL.md', entries)
            self.assertEqual(len(entries), 10)
            self.assertFalse(any('evals' in entry or '.eval-work' in entry for entry in entries))

    def test_broken_runtime_reference_blocks_publication(self):
        path = self.root / 'references/report-format.md'
        path.unlink()
        with self.assertRaisesRegex(ValueError, 'Expected seven runtime references'):
            validate(self.root)
        shutil.copy2(ROOT / 'references/report-format.md', path)
        with (self.root / 'SKILL.md').open('a', encoding='utf-8') as output:
            output.write('\n[Missing helper](references/not-present.md)\n')
        with self.assertRaisesRegex(ValueError, 'Broken or escaping link'):
            validate(self.root)


if __name__ == '__main__':
    unittest.main()
