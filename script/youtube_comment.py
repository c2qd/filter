import sys
import os

def add_filter_line(arg):
    mobile = "filter/youtube_comment_mobile.txt"
    desktop = "filter/youtube_comment.txt"

    filter_format = {
        "m.youtube.com": "m.youtube.com##ytm-comment-renderer:has(a[href=\"/{}\"])",
        "www.youtube.com": "www.youtube.com##ytd-comment-view-model:has(a[href=\"/{}\"])"
    }

    username = arg.strip()

    def process_file(filename, filter_format, username):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            added = False
            for i in range(len(lines) - 1, -1, -1):
                if "youtube.com" in lines[i]:
                    if "m.youtube.com##ytm-comment-renderer:has(a[href" in lines[i]:
                        filter_line = filter_format["m.youtube.com"].format(username)
                    elif "www.youtube.com##ytd-comment-view-model:has(a[href" in lines[i]:
                        filter_line = filter_format["www.youtube.com"].format(username)

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

    process_file(mobile, filter_format, username)
    process_file(desktop, filter_format, username)

if len(sys.argv) != 2:
    print("Usage: python script/youtube_comment.py <username>")
else:
    username = sys.argv[1]
    add_filter_line(username)
