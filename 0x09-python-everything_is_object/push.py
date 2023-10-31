#!/usr/bin/python3
if __name__ == "__main__":
    import os
    from sys import argv

    os.system('git add .')
    commit = "git commit -m" + argv[1]
    os.system(commit)
    os.system("git push")
