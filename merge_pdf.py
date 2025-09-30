#!/usr/bin/env python3

import sys

from PyPDF2 import PdfMerger
from sys import argv



if len(sys.argv) < 2:
    print("Usage: python pdf_tool.py <pdf1> <pdf2> ... -o <output> [-p <prefix>]")
    sys.exit(1)

pdf_list = []
i = 1

while i < len(sys.argv) and not sys.argv[i].startswith("-o"):
    pdf_list.append(sys.argv[i])
    i += 1

output_filename = None
if i < len(sys.argv) and sys.argv[i] == "-o":
    i += 1
    if i < len(sys.argv):
        output_filename = sys.argv[i]
    else:
        print("Error: -o requires an output file name")
        sys.exit(1)
else:
    print("Error: missing -o flag for the output file name")
    sys.exit(1)

if not pdf_list:
    print("Error: no pdf files found")
    sys.exit(1)



def merge_pdfs(pdf_list, output_filename):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_filename)
    merger.close()
    print(f"Merging into {output_filename}")



merge_pdfs(pdf_list, output_filename)