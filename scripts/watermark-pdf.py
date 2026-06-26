#!/usr/bin/env python3
"""
CC408 PDF Watermark Script
Adds semi-transparent diagonal watermark to all PDF files in static/resources/
Output goes to static/resources-wm/
"""
import os
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF not installed. Install with: pip install PyMuPDF")
    print("Skipping PDF watermarking.")
    sys.exit(0)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(BASE_DIR, '..', 'static', 'resources')
OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'static', 'resources-wm')
WATERMARK_TEXT = 'CC408 · 仅供学习 · 禁止传播'


def add_watermark_to_pdf(input_path, output_path):
    """Add watermark to all pages of a PDF."""
    doc = fitz.open(input_path)
    for page in doc:
        # Add repeating watermark pattern (tile)
        for y in range(0, int(page.rect.height), 200):
            for x in range(0, int(page.rect.width), 300):
                page.insert_text(
                    fitz.Point(x + 50, y + 50),
                    WATERMARK_TEXT,
                    fontsize=14,
                    color=(0.5, 0.5, 0.5),
                    opacity=0.05,
                    rotation=-30
                )
    doc.save(output_path)
    doc.close()


def main():
    if not os.path.isdir(RESOURCES_DIR):
        print(f"Resources directory not found: {RESOURCES_DIR}")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    processed = 0
    for root, dirs, files in os.walk(RESOURCES_DIR):
        for fname in files:
            if fname.lower().endswith('.pdf'):
                input_path = os.path.join(root, fname)
                # Preserve directory structure
                rel_path = os.path.relpath(root, RESOURCES_DIR)
                output_path = os.path.join(OUTPUT_DIR, rel_path, fname)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                try:
                    add_watermark_to_pdf(input_path, output_path)
                    processed += 1
                    print(f"  Watermarked: {fname}")
                except Exception as e:
                    print(f"  Error processing {fname}: {e}")

    print(f"Done. Watermarked {processed} PDF(s) to {OUTPUT_DIR}")


if __name__ == '__main__':
    main()
