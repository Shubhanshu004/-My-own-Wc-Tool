import sys

args = sys.argv

if len(args) < 2:
    print("Use : python pythonfilename.py [-l|-w|-c] filename")
    sys.exit(1)

# If only filename is given (no flag)
if len(args) == 2:
    filename = args[1]
    try:
        with open(filename, 'r' , encoding='utf-8') as file:
            content = file.read()
        content = content.strip()
        lines = content.split('\n')
        num_lines = len(lines)
        words = content.split()
        num_words = len(words)
        num_chars = len(content)
        print(f"lines: {num_lines}")
        print(f"words: {num_words}")
        print(f"characters: {num_chars}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(1)
else:
    flag = args[1]
    filename = args[2]
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        content = content.strip()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(1)

    if flag == '-l':
        lines = content.split('\n')
        if lines and lines[-1] == '':
            lines = lines[:-1]
        num_lines = len(lines)
        print(f"lines: {num_lines}")
    elif flag == '-w':
        words = content.split()
        num_words = len(words)
        print(f"words: {num_words}")
    elif flag == '-c':
        num_chars = len(content)
        print(f"characters: {num_chars}")
    else:
        print("Invalid flag. Use -l for lines, -w for words, or -c for characters.")
