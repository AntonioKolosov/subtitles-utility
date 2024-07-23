import json

def convert_to_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the content based on "1."
    chunks = content.split("1.")
    # Remove any empty strings that may result from splitting
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    
    # Create the JSON structure
    data = [{"chank": chunk} for chunk in chunks]
    
    # Write to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Example usage
input_file = './he_dolly.txt'
output_file = './he_dolly_converted.json'
convert_to_json(input_file, output_file)
