import os


def writefile(name, text):
    # writes data to file
    with open(name, 'w', encoding='utf-8') as f:
        f.write(text)


def readfile(name):
    # reads and returns file
    text = None
    with open(name, 'r', encoding='utf-8') as f:
        text = str(f.read())
    return text