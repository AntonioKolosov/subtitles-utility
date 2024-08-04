"""
python main.py path/to/input/file path/to/output/file
"""

import re
import json
import argparse
import os
from os import listdir
from os.path import isfile, join
import time

def list_folder(folder):
    ''''''
    onlyfiles = [f for f in listdir(folder)]
    # onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    print(onlyfiles)

def build_full_paths(show, name, lang):
    ''''''
    input_folder = 'in'
    output_folder = 'out'
    input_folder += f'/{show}'
    output_folder += f'/{show}'
    input_file = f'{input_folder}/{name}'
    output_file = f'{output_folder}/{lang}_data.json'
  
    return (input_file, output_file)

def read_src_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.rstrip() for line in file]

def save_to_dest_file(data, output_file):
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

def main(show, name, lang):
    # list_folder('./')
    (input_file, output_file) = build_full_paths(show, name, lang)
    print(f'Files: original - {input_file}, converted - {output_file}')
    # time.sleep(3600)

    original_text = read_src_file(input_file)
    chunks = divide_to_chunks(original_text)

    output_data = {
        "name": f'{lang}_data',
        "content": chunks
    }
    save_to_dest_file(output_data, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Subtitle converter utility.')
    parser.add_argument('show', type=str, help='Path to the folder with the original text.')
    parser.add_argument('name', type=str, help='name of the file with the original text.')
    parser.add_argument('lang', type=str, help='language en, he, ru.')
      
    args = parser.parse_args()
       
    main(args.show, args.name, args.lang)
