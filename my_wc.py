import sys

args = sys.argv

if len(args) < 3:
    print("Usage: python my_wc.py [-l|-w|-c] filename")
    sys.exit(1)

flag = args[1]
filename = args[2]

try:
    with open(filename, 'r') as file:
        content = file.read()
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
    char_count = len(content)
    print(f"characters: {char_count}")
else:
    print("Invalid flag. Use -l for lines, -w for words, or -c for characters.")







