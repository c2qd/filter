import sys

def remove_duplicates_from_file(filename):
    seen = set()
    with open(filename, 'r') as infile:
        lines = infile.readlines()

    with open(filename, 'w') as outfile:
        for line in lines:
            stripped_line = line.strip()  # Remove leading/trailing whitespace for comparison
            if not stripped_line:  # Skip empty lines
                outfile.write(line)
                continue
            if stripped_line in seen:
                print(f"Duplicate: {line.strip()}")
            else:
                outfile.write(line)  # Write original line with its newline intact
                seen.add(stripped_line)

if len(sys.argv) != 2:
    print("Usage: python script.py <filename>")
else:
    remove_duplicates_from_file(sys.argv[1])
