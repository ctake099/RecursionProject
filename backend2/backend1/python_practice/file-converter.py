import sys
import os
import markdown

input_file = sys.argv[2]
output_file = sys.argv[3]

if not os.path.exists(input_path):
    raise FileNotFoundError(f"{file_path}は存在しません")

with open(input_file, "r") as fi:
    content = fi.read()

with open(output_file, "w") as fo:
    html = markdown.markdown(content, extensions=['tables'])
    fo.write(html)