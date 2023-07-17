"""Module that merge first pages of all pdf files."""

import os
import argparse
from rich.progress import track
from PyPDF2 import PdfReader, PdfWriter

# 设置PDF文件所在目录和输出路径
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--pdf_dir', required=True)
args = parser.parse_args()

last_dir = os.path.basename(args.pdf_dir)
output_path = f'/Users/limu/merge/all_page_1_in_[{last_dir}].pdf'

# 获取PDF文件列表
pdf_files = [f for f in os.listdir(args.pdf_dir) if f.endswith('.pdf')]

# 创建一个新的PDF文件写入器
pdf_writer = PdfWriter()

# 遍历PDF文件列表，提取第一页并添加到PDF文件写入器中
for pdf_file in track(pdf_files):
    # 构建输入文件的路径
    input_path = os.path.join(args.pdf_dir, pdf_file)
    
    # 使用PyPDF2库获取第一页
    with open(input_path, 'rb') as f:
        pdf_reader = PdfReader(f)
        first_page = pdf_reader.pages[0]
        
        # 添加第一页到PDF文件写入器中
        pdf_writer.add_page(first_page)

# 将PDF文件写入器中的所有页面写入到输出文件中
with open(output_path, 'wb') as out:
    pdf_writer.write(out)

print(f'Successfully merged first pages of {len(pdf_files)} PDF files into {output_path}.')
