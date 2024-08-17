#!/usr/bin/env python3

import getopt
import os

global default_rulefiles_dir
default_rulefiles_dir = ""
global rulefiles_to_use
rulefiles_to_use = []
global rules
rules = {} 
global show_inverted
show_inverted = False

def list_all_default_files():
    global default_rulefiles_dir
    rulefiles = os.listdir(default_rulefiles_dir)
    for rulefile in rulefiles:
        f = open( default_rulefiles_dir + rulefile , "r")
        first_line = f.readline()
        f.close()
        print(rulefile + " " + first_line.strip())

def import_rules_from_file(rulefile_name):
    global rules
    rulefile = open(rulefile_name, "r")
    for line in rulefile:
        if line[0] != "#":
            key, subs = line.strip().split(':')
            if key not in rules.keys():
                rules[key] = set()
                rules[key].add(key)
            for s in subs.split(','):
                rules[key].add(s)             

def import_all_default_files():
    global rulefiles_to_use
    global default_rulefiles_dir
    rulefiles = os.listdir(default_rulefiles_dir)
    for rulefile in rulefiles:
        import_rules_from_file(default_rulefiles_dir + rulefile)

def print_word(word):
    global show_inverted
    print(word)
    if show_inverted:
        print(word[::-1])

def mount_word(lista, word=""):
    if len(lista) == 1:
        for char in lista[0]:
            print_word(word + char)
    else:
        for char in lista[0]:
            mount_word(lista[1:], word + char)

def execute():
    global word
    global rules
    word = word.lower()
    word_list = []
    for char in word:
        if char not in rules.keys():
            rules[char] = set()
            rules[char].add(char)
        word_list.append(rules[char])

    mount_word(word_list, word="")

def main(argv):
    global default_rulefiles_dir
    script_dir = os.path.dirname(os.path.realpath(__file__))
    default_rulefiles_dir = script_dir + "/fuzzy_rules/"
    global show_inverted
    global word

    try:
        opts, args = getopt.getopt(argv[2:], "LAr:iw:")
    except get.GetoptError as err:
        print(str(err))
        return 1

    for o, a in opts:
        if o == "-L":
            list_all_default_files()
            return 0
        elif o == "-A":
            import_all_default_files()
        elif o == "-r":
            import_rules_from_file(default_rulefiles_dir + a)
        elif o == "-i":
            show_inverted = True
        elif o == "-w":
            word = a

    execute()

