#!/usr/bin/env python3
import sys
sys.path.append(".")
import mod.userpass as userpass
import mod.addends as addends
import mod.fuzzy as fuzzy
import getopt

def help(argv):
    print("Usage: "+argv[0]+" <mode> <options>")
    print("Modes allowed:")
    print("help           -- Print this help page")
    print("userpass       -- Create a file with user pass in each line separeted by space or other separators")
    print("fuzzy          -- fuzzy wordlists with 1337 or other symbols")
    print("addends        -- input wordlist to add 123, !@#, etc at the end of each word")
    print("")
    userpass.help(0)
    print()
    addends.help(0)
    print()
    fuzzy.help(0)


def main():
    if len(sys.argv) == 1:
        help(sys.argv)
        exit()
    else:
        mode = str(sys.argv[1])
    modes = ["help", "userpass", "fuzzy", "addends"]
    if mode not in modes:
        help(sys.argv)
    elif mode == "help":
        help(sys.argv)
    elif mode == "userpass":
        code = userpass.main(sys.argv);
        if code != 0:
            userpass.help(code);
    elif mode == "addends":
        code = addends.main(sys.argv)
        if code != 0:
            addends.help(code);
    elif mode == "fuzzy":
        code = fuzzy.main(sys.argv)
        if code != 0:
            fuzzy.help(code);

main()
