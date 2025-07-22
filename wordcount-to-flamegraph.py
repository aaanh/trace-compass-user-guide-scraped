import os

SRC_DIR = 'src'
OUTPUT_FILE = 'wordcount.folded'

folded_lines = []

for root, dirs, files in os.walk(SRC_DIR):
    for file in files:
        if file == 'index.md':
            file_path = os.path.join(root, file)
            # Build stack: remove src/ and index.md, join dirs with ;
            rel_path = os.path.relpath(file_path, SRC_DIR)
            parts = rel_path.split(os.sep)[:-1]  # exclude index.md
            if parts:
                stack = ';'.join(parts)
            else:
                stack = 'root'
            # Count words
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                word_count = len(text.split())
            folded_lines.append(f"{stack} {word_count}")

with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
    for line in folded_lines:
        out.write(line + '\n') 