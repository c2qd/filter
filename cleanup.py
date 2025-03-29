import sys

def remove_duplicates_from_file(filename):
    seen = set()
    with open(filename, 'r') as infile:
        lines = infile.readlines()

    with open(filename, 'w') as outfile:
        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith('!'):
                outfile.write(line)
                continue
            if not stripped_line:
                outfile.write(line)
                continue
            if stripped_line in seen:
                print(f"Duplicate: {line.strip()}")
            else:
                outfile.write(line)
                seen.add(stripped_line)

if len(sys.argv) != 2:
    print("Usage: python script.py <filename>")
else:
    remove_duplicates_from_file(sys.argv[1])
