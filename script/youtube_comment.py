import sys
import os

def add_filter_line(arg):
    mobile = "filter/youtube_comment_mobile.txt"
    desktop = "filter/youtube_comment.txt"

    filter_format = {
        "m.youtube.com": [
            "m.youtube.com##ytm-comment-thread-renderer:has(a[href=\"/{}\"])",
            "m.youtube.com##ytm-comment-renderer:has(a[href=\"/{}\"])"
        ],
        "www.youtube.com": [
            "www.youtube.com##ytd-comment-thread-renderer:has(a[href=\"/{}\"])",
            "www.youtube.com##ytd-comment-view-model:has(a[href=\"/{}\"])"
        ]
    }

    username = arg.strip()

    def process_file(filename, site_key, formats, username):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            added = False
            for i in range(len(lines) - 1, -1, -1):
                if site_key in lines[i]:
                    for format_line in formats:
                        filter_line = format_line.format(username)
                        lines.insert(i + 1, filter_line + "\n")
                    added = True
                    break

            if added:
                with open(filename, 'w') as file:
                    file.writelines(lines)
                print(f"Filters for '{username}' have been added to {filename}.")
            else:
                print(f"No matching URL found to add filters for '{username}' in {filename}.")
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
        except Exception as e:
            print(f"An error occurred while processing {filename}: {e}")

    process_file(mobile, "m.youtube.com", filter_format["m.youtube.com"], username)
    process_file(desktop, "www.youtube.com", filter_format["www.youtube.com"], username)

if len(sys.argv) != 2:
    print("Usage: python script/youtube_comment.py <username>")
else:
    username = sys.argv[1]
    add_filter_line(username)
