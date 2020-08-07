import sys

def format(text):
    line_limit = 30
    current_pos = 0
    lines = []
    while current_pos < len(text):
        lines.append(text[current_pos:current_pos + line_limit])
        current_pos += line_limit

    f = "" 
    f = " " + ("_" * line_limit) + " \n"
    for i in lines:
        f += "|" + i + " " * (line_limit - len(i)) + "|\n"
    f += " " + ("-" * line_limit) + " "

    return f
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Too few arguments!")
        sys.exit(1)

    say = sys.argv[1]
    cow = """
     \\
      \\ 
       \\
        ^__^
        (oo)\_________
        (__)\\ o O  o  )/\\/\\
            |   o O  O|
            ||------w-|
            ||       ||
            uu       uu
    """
    print(format(say), end="")
    print(cow)
