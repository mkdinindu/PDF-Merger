#!/usr/bin/env python3

import sys
from PyPDF2 import PdfMerger, PdfReader, PdfWriter


# --------------------------
# Functions
# --------------------------
def merge_pdfs(pdf_list, output_filename):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_filename)
    merger.close()
    print(f"Merged PDFs into {output_filename}")


def compress_pdf(input_path, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata({})
    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"Compressed PDF saved as {output_path}")


# --------------------------
# Main Program
# --------------------------
if len(sys.argv) < 2:
    print("Usage:")
    print("  Merge: python PDF_Tools.py -m <pdf1> <pdf2> ... -o <output>")
    print("  Compress: python PDF_Tools.py -c <input_pdf> -o <output>")
    sys.exit(1)

mode = sys.argv[1]

if mode == "-m":
    # Merge mode
    if "-o" not in sys.argv:
        print("Error: missing -o flag for output filename")
        sys.exit(1)

    o_index = sys.argv.index("-o")
    pdf_list = sys.argv[2:o_index]  # PDFs to merge
    if not pdf_list:
        print("Error: no PDF files specified to merge")
        sys.exit(1)
    if o_index + 1 >= len(sys.argv):
        print("Error: output filename missing after -o")
        sys.exit(1)
    output_filename = sys.argv[o_index + 1]
    merge_pdfs(pdf_list, output_filename)

elif mode == "-c":
    # Compress mode
    if len(sys.argv) < 4 or sys.argv[2] == "-o":
        print("Usage: python PDF_Tools.py -c <input_pdf> -o <output>")
        sys.exit(1)
    input_pdf = sys.argv[2]
    if "-o" not in sys.argv:
        print("Error: missing -o flag for output filename")
        sys.exit(1)
    o_index = sys.argv.index("-o")
    if o_index + 1 >= len(sys.argv):
        print("Error: output filename missing after -o")
        sys.exit(1)
    output_filename = sys.argv[o_index + 1]
    compress_pdf(input_pdf, output_filename)

else:
    print("Error: unknown mode. Use -m to merge or -c to compress.")
    sys.exit(1)
