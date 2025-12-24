# Scripts

This directory contains utility scripts to help maintain and manage the repository.

## Purpose

Scripts here automate common tasks such as:

- Creating new course notes with proper naming and frontmatter
- Generating progress reports from notes
- Validating repository structure
- Syncing notebooks and notes
- Generating statistics and summaries
- Backup and maintenance tasks

## Usage

All scripts should be executable and can be run from the repository root:

```bash
# Make script executable
chmod +x scripts/script_name.py

# Run from repository root
python scripts/script_name.py
# or
./scripts/script_name.py
```

## Script Naming Convention

- Use descriptive names: `create_note.py`, `generate_progress.py`
- Use underscores for multi-word names
- Add `.sh` extension for shell scripts, `.py` for Python scripts

## Examples

- `create_course_note.py` - Create a new course note with template
- `sync_notebooks.py` - Sync notebooks with course notes
- `generate_progress_report.py` - Generate progress summary
- `validate_structure.py` - Check repository structure integrity
- `update_readme_progress.py` - Update progress in README automatically
