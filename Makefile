.PHONY: help install install-dev clean lint format test setup new-note

help:
	@echo "Available commands:"
	@echo "  make install      - Install base dependencies"
	@echo "  make install-dev  - Install development dependencies"
	@echo "  make clean        - Remove Python cache files"
	@echo "  make lint         - Run linters"
	@echo "  make format       - Format code with black"
	@echo "  make test         - Run tests"
	@echo "  make setup        - Initial setup (install all dependencies)"
	@echo ""
	@echo "Scripts:"
	@echo "  make new-note COURSE=<course> TITLE=\"<title>\" - Create new course note"
	@echo "    Example: make new-note COURSE=ng-ml-spec TITLE=\"Neural Networks\""

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -e ".[dev]"

setup: install install-dev
	@echo "Setup complete!"

clean:
	find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} + 2>/dev/null || true
	find . -type d -name ".ipynb_checkpoints" -exec rm -r {} + 2>/dev/null || true

lint:
	flake8 . --exclude=venv,env,.venv

format:
	black .

test:
	pytest

# Scripts
new-note:
	@if [ -z "$(COURSE)" ] || [ -z "$(TITLE)" ]; then \
		echo "Usage: make new-note COURSE=<course> TITLE=\"<title>\""; \
		echo "Example: make new-note COURSE=ng-ml-spec TITLE=\"Neural Networks\""; \
		exit 1; \
	fi
	python scripts/create_course_note.py $(COURSE) "$(TITLE)"

