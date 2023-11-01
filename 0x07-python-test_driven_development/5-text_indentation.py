#!/usr/bin/python3
"""text_indentation Module"""


def text_indentation(text):
    """prints a text with 2 new lines
    after each of these characters: ., ? and :"""
    if not isinstance(text, str) or text is None or len(text) < 0:
        raise TypeError("text must be a string")
    flag = 0
    for c in text:
        if c in ('?', ':', '.'):
            print(c, end="\n\n")
            flag = 1
        else:
            if flag == 0:
                print(c, end="")
            else:
                if c == ' ' or c == '\t':
                    pass
                else:
                    print(c, end="")
                    flag = 0
