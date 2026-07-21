#!/usr/bin/env python3
"""
Cover footer side text in exam PDFs while keeping the centered page number.

Default behavior:
- Reads PDFs from static/resources/pdfs.
- Skips files whose name contains "answer-sheet".
- Writes cleaned PDFs to static/resources/pdfs/processed.
- For 2009-2025-complete.pdf, starts at page 38 because pages 1-37
  were already covered manually.
- For individual yearly exam PDFs, starts at page 1.
"""

from __future__ import annotations

import argparse
import copy
import sys
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]
DEFAULT_INPUT_DIR = REPO_ROOT / "static" / "resources" / "pdfs"
DEFAULT_OUTPUT_DIR = DEFAULT_INPUT_DIR / "processed"

A4_WIDTH = 595.2
A4_HEIGHT = 841.92

# Coordinates are in PDF points, measured from the bottom-left corner.
# These rectangles tightly cover only the footer side labels:
# - left: "答案详见计算机考研杂货铺"
# - right: "www.csgraduates.com"
# The centered page number sits between them and is intentionally preserved.
FOOTER_RECTS = (
    (89.5, 49.5, 110.0, 12.0),
    (421.5, 49.0, 85.0, 12.0),
)

COMPLETE_PDF_NAME = "2009-2025-complete.pdf"
COMPLETE_START_PAGE = 38
YEARLY_START_PAGE = 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Batch cover footer side text in CC408 PDF resources."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=DEFAULT_INPUT_DIR,
        help=f"PDF directory to process. Default: {DEFAULT_INPUT_DIR}",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Output directory. Default: {DEFAULT_OUTPUT_DIR}",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite output PDFs if they already exist.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be processed without writing files.",
    )
    return parser.parse_args()


def first_page_to_cover(pdf_name: str) -> int:
    if pdf_name.lower() == COMPLETE_PDF_NAME:
        return COMPLETE_START_PAGE
    return YEARLY_START_PAGE


def make_footer_overlay(width: float, height: float) -> PdfReader:
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))
    c.setFillColorRGB(1, 1, 1)

    scale_x = width / A4_WIDTH
    scale_y = height / A4_HEIGHT
    for x, y, rect_width, rect_height in FOOTER_RECTS:
        c.rect(
            x * scale_x,
            y * scale_y,
            rect_width * scale_x,
            rect_height * scale_y,
            stroke=0,
            fill=1,
        )

    c.save()
    packet.seek(0)
    return PdfReader(packet)


def cover_pdf(input_path: Path, output_path: Path, start_page: int) -> int:
    reader = PdfReader(str(input_path))
    writer = PdfWriter()
    overlay_cache: dict[tuple[float, float], PdfReader] = {}
    covered_pages = 0

    for index, page in enumerate(reader.pages, start=1):
        output_page = copy.copy(page)

        if index >= start_page:
            box = output_page.mediabox
            width = float(box.width)
            height = float(box.height)
            key = (round(width, 2), round(height, 2))

            if key not in overlay_cache:
                overlay_cache[key] = make_footer_overlay(width, height)

            output_page.merge_page(overlay_cache[key].pages[0])
            covered_pages += 1

        writer.add_page(output_page)

    if reader.metadata:
        writer.add_metadata(dict(reader.metadata))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("wb") as handle:
        writer.write(handle)

    return covered_pages


def iter_target_pdfs(input_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in input_dir.iterdir()
        if path.is_file()
        and path.suffix.lower() == ".pdf"
        and "answer-sheet" not in path.name.lower()
    )


def main() -> int:
    args = parse_args()
    input_dir = args.input_dir.resolve()
    output_dir = args.output_dir.resolve()

    if not input_dir.is_dir():
        print(f"Input directory not found: {input_dir}", file=sys.stderr)
        return 1

    targets = iter_target_pdfs(input_dir)
    if not targets:
        print(f"No target PDFs found in {input_dir}")
        return 0

    print(f"Input:  {input_dir}")
    print(f"Output: {output_dir}")
    print(f"Targets: {len(targets)} PDF(s)")

    processed = 0
    skipped = 0

    for input_path in targets:
        output_path = output_dir / input_path.name
        start_page = first_page_to_cover(input_path.name)

        if output_path.exists() and not args.force:
            print(f"SKIP exists: {input_path.name}")
            skipped += 1
            continue

        reader = PdfReader(str(input_path))
        page_count = len(reader.pages)
        if start_page > page_count:
            print(
                f"SKIP no pages to cover: {input_path.name} "
                f"(pages={page_count}, start_page={start_page})"
            )
            skipped += 1
            continue

        if args.dry_run:
            print(
                f"DRY {input_path.name}: pages={page_count}, "
                f"cover pages {start_page}-{page_count}"
            )
            processed += 1
            continue

        covered_pages = cover_pdf(input_path, output_path, start_page)
        print(
            f"OK {input_path.name}: pages={page_count}, "
            f"covered={covered_pages}, output={output_path}"
        )
        processed += 1

    action = "Would process" if args.dry_run else "Processed"
    print(f"{action}: {processed}; skipped: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
