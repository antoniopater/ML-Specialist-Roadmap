#!/usr/bin/env python3
"""
Script to create a new course note with proper naming and frontmatter template.

Usage:
    python scripts/create_course_note.py <course> <lesson_title>
    
Example:
    python scripts/create_course_note.py ng-ml-spec "Neural Networks"
"""

import sys
import os
from datetime import datetime
from pathlib import Path

def create_course_note(course: str, lesson_title: str):
    """Create a new course note file with template."""
    
    # Get repository root (parent of scripts directory)
    repo_root = Path(__file__).parent.parent
    
    # Create course notes directory path
    course_dir = repo_root / "01_course_notes" / course
    
    # Create directory if it doesn't exist
    course_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate filename: YYYY_MM_DD_Lesson_Title.md
    today = datetime.now()
    date_str = today.strftime("%Y_%m_%d")
    filename = f"{date_str}_{lesson_title.replace(' ', '_')}.md"
    filepath = course_dir / filename
    
    # Check if file already exists
    if filepath.exists():
        print(f"⚠️  File already exists: {filepath}")
        response = input("Do you want to overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Aborted.")
            return
    
    # Create frontmatter and template
    frontmatter = f"""---
course: {course}
lesson: "{lesson_title}"
date: {today.strftime("%Y-%m-%d")}
time_spent_h: 0
tags: [course, {course.replace('-', ', ')}]
---

## {lesson_title}

### Overview


### Key Concepts


### Examples


### Takeaways


---
"""
    
    # Write file
    filepath.write_text(frontmatter, encoding='utf-8')
    print(f"✅ Created: {filepath}")
    print(f"📝 Edit the file to add your notes!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scripts/create_course_note.py <course> <lesson_title>")
        print("\nExample:")
        print('  python scripts/create_course_note.py ng-ml-spec "Neural Networks"')
        sys.exit(1)
    
    course = sys.argv[1]
    lesson_title = " ".join(sys.argv[2:])  # Join all remaining args as title
    
    create_course_note(course, lesson_title)

