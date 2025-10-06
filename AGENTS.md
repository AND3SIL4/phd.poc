# Agent Guidelines for POCs Repository

## Commands
- **Install dependencies**: `uv sync`
- **Run main script**: `python app/main.py`
- **Run tests**: `python -m pytest` (if pytest is added)
- **Run single test**: `python -m pytest tests/test_file.py::test_function`
- **Lint**: `ruff check .` (if ruff is added)
- **Format**: `ruff format .` (if ruff is added)

## Code Style Guidelines
- **Python version**: 3.13+
- **Imports**: Standard library first, then third-party, then local imports
- **Naming**: snake_case for variables/functions, PascalCase for classes
- **Types**: Use type hints for function parameters and return values
- **Error handling**: Use try/except blocks for external operations (PDF processing, OCR)
- **Docstrings**: Add docstrings to functions and classes
- **Line length**: Keep lines under 88 characters
- **Formatting**: Use ruff for consistent formatting