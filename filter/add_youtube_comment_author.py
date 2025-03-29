import sys

def add_filter_line(filename, arg):
    with open(filename, 'r') as file:
        lines = file.readlines()

    m_filter_prefix = "m.youtube.com##ytm-comment-renderer:has(a[href=\"/"
    m_added = False
    for i in range(len(lines)-1, -1, -1):
        if lines[i].startswith(m_filter_prefix):
            lines.insert(i + 1, f'm.youtube.com##ytm-comment-renderer:has(a[href="/{arg}"])\n')
            m_added = True
            break

    w_filter_prefix = "www.youtube.com##ytd-comment-view-model:has(a[href=\"/"
    w_added = False
    for i in range(len(lines)-1, -1, -1):
        if lines[i].startswith(w_filter_prefix):
            lines.insert(i + 1, f'www.youtube.com##ytd-comment-view-model:has(a[href="/{arg}"])\n')
            w_added = True
            break

    if m_added or w_added:
        with open(filename, 'w') as file:
            file.writelines(lines)
        print(f"Filters for '{arg}' have been added.")
    else:
        print(f"No matching lines found to add filters for '{arg}'.")

if len(sys.argv) != 3:
    print("Usage: python script.py <filename> <arg>")
else:
    filename = sys.argv[1]
    arg = sys.argv[2]
    add_filter_line(filename, arg)
