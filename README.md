# PDF Information Extraction POC

A Proof of Concept (POC) project for extracting information from PDF files using OCR technology. The goal is to process PDF documents and extract structured data for export to CSV or Excel formats.

## Current Functionality

- PDF to image conversion using `pdf2image`
- OCR text extraction using `pytesseract` (Tesseract OCR)
- Support for Spanish language text recognition
- Basic text processing and concatenation

## Future Plans

- Export extracted data to CSV/Excel formats
- Integration with OpenAI ChatGPT API for intelligent data processing
- Enhanced text parsing and data structuring
- Web interface for file uploads and processing

## Requirements

- Python 3.13+
- Tesseract OCR installed on the system
- Poppler (for PDF processing)

## Installation

1. Install Python dependencies:

   ```bash
   uv sync
   ```

2. Install Tesseract OCR:

   - **Windows**: Download from [GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

3. Install Poppler:
   - **Windows**: Included with `pdf2image`
   - **macOS**: `brew install poppler`
   - **Linux**: `sudo apt-get install poppler-utils`

## Usage

Run the main script with a PDF file:

```bash
python app/main.py
```

The script currently processes `test.pdf` and outputs extracted text to the console.

## Project Structure

```
pocs/
├── app/
│   ├── main.py          # Main processing script
│   └── modules/         # Additional modules (future use)
├── pyproject.toml       # Project configuration
├── uv.lock             # Dependency lock file
└── README.md           # This file
```

## Dependencies

- `pdf2image`: PDF to image conversion
- `pillow`: Image processing
- `pytesseract`: OCR text extraction

---

_Created by AND3SIL4 at Net Applications | On October 06_
