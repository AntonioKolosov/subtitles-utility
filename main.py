"""
python main.py path/to/input/file path/to/output/file
"""

from itertools import groupby
import re
import json
import argparse
import os

def read_subtitle_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.rstrip() for line in file]
        # return file.readlines()

def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def divide_to_chunks(subtile_text):
    """"""
    chunks = []
    chunk_value = ''
    for line in subtile_text:
        if line.strip():
            if re.match(r"\d", line) is not None:
                if chunk_value != '':
                    n = sum(c.isdigit() for c in line)
                    s = line[n]
                    if s != '.':
                        # If it is not new chunks id
                        chunk_value += line + '\n'
                    chunk = {"chank": chunk_value}
                    chunks.append(chunk)
                    chunk_value = ''
                continue
            else:
                chunk_value += line + '\n'
    # last chunk
    if chunk_value != '':
        chunk = {"chank": chunk_value}
        chunks.append(chunk)
    
    return chunks

def main(input_file, output_file):
    subtitle_text = read_subtitle_file(input_file)
    chunks = divide_to_chunks(subtitle_text)
    file_name = os.path.splitext(os.path.basename(input_file))[0]
    content = {
        "name": file_name,
        "content": chunks
    }
    save_to_json(content, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Subtitle chunk converter utility.')
    parser.add_argument('input_file', type=str, help='Path to the input subtitle file.')
    parser.add_argument('output_file', type=str, nargs='?', help='Path to the output JSON file. If not provided, saves in the same directory as file with _output.json suffix.')
    
    args = parser.parse_args()
    
    if args.output_file:
        output_file = args.output_file
    else:
        base, _ = os.path.splitext(args.input_file)
        output_file = f"{base}_output.json"
    
    main(args.input_file, output_file)
