def remove_duplicates_from_file(filenames):
    seen = set()
    for filename in filenames:
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
                    print(f"Duplicate in {filename}: {line.strip()}")
                else:
                    outfile.write(line)
                    seen.add(stripped_line)

files = ['filter/youtube_comment.txt', 'filter/youtube_comment_mobile.txt']

remove_duplicates_from_file(files)
