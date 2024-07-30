"""
python main.py path/to/input/file path/to/output/file
"""


import re
import json
import argparse
import os

def read_subtitle_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def split_into_chunks(subtitle_text):
    chunks = subtitle_text.split('1.\n')
    return chunks

def parse_chunk(chunk):
    lines = chunk.strip().split('\n')
    if not lines:
        return None

    content = []
    for line in lines:
        if not re.match(r'^\d+\.$', line.strip()) and line.strip():
            content.append(line.strip())

    if content:
        return '- ' + '\n- '.join(content)
    return None

def convert_to_custom_format(chunks):
    custom_format = []

    for chunk in chunks:
        chunk_value = parse_chunk(chunk)
        if chunk_value:
            custom_format.append({"chank": chunk_value})

    return custom_format

def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main(input_file, output_file):
    subtitle_text = read_subtitle_file(input_file)
    chunks = split_into_chunks(subtitle_text)
    parsed_chunks = [parse_chunk(chunk) for chunk in chunks if parse_chunk(chunk)]
    custom_format = convert_to_custom_format(parsed_chunks)
    save_to_json(custom_format, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Subtitle chunk converter utility.')
    parser.add_argument('input_file', type=str, help='Path to the input subtitle file.')
    parser.add_argument('output_file', type=str, nargs='?', help='Path to the output JSON file. If not provided, saves in the same directory.')
    
    args = parser.parse_args()
    
    if args.output_file:
        output_file = args.output_file
    else:
        base, _ = os.path.splitext(args.input_file)
        output_file = f"{base}.json"
    
    main(args.input_file, output_file)
