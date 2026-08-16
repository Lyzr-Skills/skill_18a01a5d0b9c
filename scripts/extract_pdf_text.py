#!/usr/bin/env python3
"""
extract_pdf_text.py — Extracts readable text from a PDF file.

Usage:
    python extract_pdf_text.py <path-to-pdf> [--pages N-M] [--output file.txt]

Options:
    --pages     Page range to extract, e.g. "1-10" or "5" (default: all)
    --output    Write output to a file instead of stdout
    --metadata  Also print document metadata (title, author, etc.)

Exit codes:
    0  Success
    1  File not found or unreadable
    2  Extraction produced no text (likely a scanned/image PDF)
    3  Missing dependency
"""

import sys
import os
import argparse

# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------
try:
    import pdfplumber
except ImportError:
    try:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pdfplumber", "-q"])
        import pdfplumber
    except Exception:
        print(
            "ERROR: Could not import or install 'pdfplumber'.\n"
            "Install it with:  pip install pdfplumber",
            file=sys.stderr,
        )
        sys.exit(3)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def parse_page_range(spec: str, total_pages: int) -> range:
    """Parse a page range string like '1-10' or '5' into a range object (0-indexed)."""
    spec = spec.strip()
    if "-" in spec:
        parts = spec.split("-", 1)
        start = max(1, int(parts[0])) - 1          # convert to 0-indexed
        end = min(total_pages, int(parts[1]))       # inclusive end
    else:
        page = int(spec)
        start = max(1, page) - 1
        end = min(total_pages, page)
    return range(start, end)


def extract_metadata(pdf) -> dict:
    """Return a dict of available document metadata."""
    meta = pdf.metadata or {}
    clean = {}
    for key in ("Title", "Author", "Subject", "Creator", "Producer", "CreationDate"):
        val = meta.get(key) or meta.get(key.lower())
        if val:
            clean[key] = val.strip() if isinstance(val, str) else val
    clean["Pages"] = len(pdf.pages)
    return clean


def format_metadata(meta: dict) -> str:
    lines = ["=== Document Metadata ==="]
    for k, v in meta.items():
        lines.append(f"  {k}: {v}")
    lines.append("=" * 26)
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main extraction logic
# ---------------------------------------------------------------------------
def extract_text(pdf_path: str, page_range: range = None, show_metadata: bool = False) -> str:
    """
    Open the PDF at `pdf_path` and extract text from the given page range.
    Returns the extracted text as a string.
    """
    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)

        meta_block = ""
        if show_metadata:
            meta_block = format_metadata(extract_metadata(pdf)) + "\n\n"

        pages_to_read = page_range if page_range is not None else range(total)

        chunks = []
        for i in pages_to_read:
            if i >= total:
                break
            page = pdf.pages[i]
            text = page.extract_text(x_tolerance=2, y_tolerance=3) or ""
            # Annotate each page for orientation
            chunks.append(f"--- Page {i + 1} ---\n{text.strip()}")

        body = "\n\n".join(chunks)
        return meta_block + body


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Extract text from a PDF file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument(
        "--pages",
        default=None,
        help="Page range to extract (e.g. '1-10' or '5'). Default: all pages.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Write output to this file path instead of stdout.",
    )
    parser.add_argument(
        "--metadata",
        action="store_true",
        help="Print document metadata at the top of the output.",
    )

    args = parser.parse_args()

    # --- Validate file ---
    if not os.path.isfile(args.pdf_path):
        print(f"ERROR: File not found: {args.pdf_path}", file=sys.stderr)
        sys.exit(1)

    # --- Determine page range ---
    page_range = None
    if args.pages:
        try:
            # We need the total page count first; open briefly
            with pdfplumber.open(args.pdf_path) as _pdf:
                total = len(_pdf.pages)
            page_range = parse_page_range(args.pages, total)
        except ValueError:
            print(
                f"ERROR: Invalid page range '{args.pages}'. Use format like '1-10' or '5'.",
                file=sys.stderr,
            )
            sys.exit(1)

    # --- Extract ---
    try:
        text = extract_text(args.pdf_path, page_range=page_range, show_metadata=args.metadata)
    except Exception as exc:
        print(f"ERROR: Failed to read PDF: {exc}", file=sys.stderr)
        sys.exit(1)

    # --- Check output ---
    if not text.strip():
        print(
            "WARNING: No text was extracted. The PDF may be scanned/image-based.\n"
            "Consider using an OCR tool (e.g. pytesseract, Adobe Acrobat, or Google Drive).",
            file=sys.stderr,
        )
        sys.exit(2)

    # --- Output ---
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Text saved to: {args.output}")
    else:
        print(text)


if __name__ == "__main__":
    main()
