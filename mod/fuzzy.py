#!/usr/bin/env python3

import getopt

global passfile
passfile = ""
global output_
output_ = ""
global fuzzlevel
fuzzlevel = 3
global passwords
passwords = ""
global passlist
passlist = []
global listing
listing = 0 #0 - do nothing, 1 - list and quit, 2 - list and continue
global rules
rules = []
global rulefile
rulefile = ""
global ego
ego = 0 #0 - use all rules, 1 - use just passed rules
global rules_db
rules_db = {}
global verbose
verbose = False
global mirror
mirror = False

fuzzy_1337_vow = {
        'a':['4','a'],
        'e':['3','e'],
        'i':['i','1'],
        'o':['o','0'],
        'A':['4','a'],
        'E':['3','e'],
        'I':['i','1'],
        'O':['o','0'],
}

fuzzy_1337_con = {
        'a':['4','a'],
        'b':['b','8'],
        'e':['3','e'],
        'g':['g','8'],
        'i':['i','1'],
        'l':['l','1'],
        'o':['o','0'],
        's':['s','5'],
        't':['t','1','7'],
        'v':['v','7'],
        'A':['4','a'],
        'B':['b','8'],
        'E':['3','e'],
        'G':['g','8'],
        'I':['i','1'],
        'L':['l','1'],
        'O':['o','0'],
        'S':['s','5'],
        'T':['t','1','7'],
        'V':['v','7'],
}

fuzzy_total = {
        'a':['4','a','@'],
        'b':['b','8'],
        'e':['3','e','&'],
        'g':['g','8'],
        'h':['h','#'],
        'i':['i','1','!','|'],
        'l':['l','1','!','|'],
        'o':['o','0'],
        's':['s','5','$'],
        't':['t','1','7'],
        'v':['v','7'],
        'A':['4','A','@'],
        'B':['B','8'],
        'E':['3','e','&'],
        'G':['G','8'],
        'H':['H','#'],
        'I':['I','1','!','|'],
        'L':['L','1','!','|'],
        'O':['O','0'],
        'S':['S','5','$'],
        'T':['T','1','7'],
        'V':['V','7'],
}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def help(code):
	if code in [0,1]:
		print("mode fuzzy options")
		print("------------------")
		print("      -h         : Show this help page")
		print("      -p <pass>  : Define password(s) to be fuzzed")
		print("                 : -p pass, or -p pass1,pass2,pass3")
		print("      -P <file>  : Choose file with passwords")
		print("      -t <type>  : Choose the type of fuzzing")
		print("                 : 1 - 1337 on vowels")
		print("                 : 2 - 1337 on everything")
		print("                 : 3 - Use symbols like !,@,#,$... and 1337")
		print("                 : Default is 3")
		print("      -m         : Show reverse words (word and drow)")
		print("      -o <file>  : Choose the output file")
		print("      -r <rule>  : Add your own rules to substitution")
		print("                 : It can be used multiple times do more rules")
		print("      -R <file>  : File with substitution rules")
		print("      -e         : Use just your rules")
		print("      -l         : Show table of substitutions that will be made")
		print("                 : The program will quit after this")
		print("      -L         : Show table of substitutions that will be made")
		print("                 : The program will NOT quit after this")
		print("      -v         : Show results on screen")
		print(" -- Rule Format -- ")
		print("      A:4,@,a    : This means that A will be replaced by '4','@' and 'a'")
	elif code == 2:
		print(bcolors.FAIL+"You must give at least one password"+bcolors.ENDC)
		print("mode fuzzy options")
		print("------------------")
		print("      -h         : Show this help page")
		print(bcolors.FAIL+"      -p <pass>  : Define password(s) to be fuzzed"+bcolors.ENDC)
		print(bcolors.FAIL+"                 : -p pass, or -p pass1,pass2,pass3"+bcolors.ENDC)
		print(bcolors.FAIL+"      -P <file>  : Choose file with passwords"+bcolors.ENDC)
	elif code == 3:
		print(bcolors.FAIL+"You must give me at least one rule"+bcolors.ENDC)
		print("mode fuzzy options")
		print("------------------")
		print("      -h         : Show this help page")
		print("      -p <pass>  : Define password(s) to be fuzzed")
		print("                 : -p pass, or -p pass1,pass2,pass3")
		print("      -P <file>  : Choose file with passwords")
		print("      -t <type>  : Choose the type of fuzzing")
		print("                 : 1 - 1337 on vowels")
		print("                 : 2 - 1337 on everything")
		print("                 : 3 - Use symbols like !,@,#,$... and 1337")
		print("                 : Default is 3")
		print("      -m         : Show reverse words (word and drow)")
		print("      -o <file>  : Choose the output file")
		print(bcolors.FAIL+"      -r <rule>  : Add your own rule to substitution"+bcolors.ENDC)
		print(bcolors.FAIL+"                 : It can be used multiple times do more rules"+bcolors.ENDC)
		print(bcolors.FAIL+"      -R <file>  : File with substitution rules"+bcolors.ENDC)
		print(bcolors.FAIL+"      -e         : Use just your rules"+bcolors.ENDC)
		print("      -l         : Show table of substitutions that will be made")
		print("                 : The program will quit after this")
		print("      -L         : Show table of substitutions that will be made")
		print("                 : The program will NOT quit after this")
		print(" -- Rule Format -- ")
		print("      A:4,@,a    : This means that A will be replaced by '4','@' and 'a'")
	if code != 0:
		exit()


def join_list(lista):
	string = ""
	for a in lista:
		string = string + a + ","
	return string[:-1]

def list_rules(listing):
	global rules_db
	for letter in rules_db.keys():
		print(letter+"\t"+join_list(rules_db[letter]))

	if listing == 1:
		quit()

def prepare_rules(fuzzlevel):
	global rules_db
	global rules
	global rulefile
	global ego

	if ego == 0:
		if fuzzlevel == 1:
			rules_db = fuzzy_1337_vow;
		elif fuzzlevel == 2:
			rules_db = fuzzy_1337_con;
		elif fuzzlevel == 3:
			rules_db = fuzzy_total;

	
	if rules != []:
		for r in rules:
			l = r.split(':')[0]
			s = r.split(':')[1].split(',')
			if l in rules_db.keys():
				for i in s:
					rules_db[l].append(i)
			else:
				rules_db[l] = s
 		

def prepare_passwords():
	global passlist
	global passwords
	passlist = passwords.split(',')

def add(lista, maxi):
    lista[0] = lista[0] + 1
    if lista[0] == maxi[0] + 1:
        for i in range(len(lista)-1):
            if lista[i] == maxi[i] + 1:
                lista[i] = 0
                lista[i+1] = lista[i+1] + 1
    return lista

def translate(dic, ind):
    word = ""
    for i in range(len(dic)):
        word = word + dic[i][ind[i]]
    return word

def fuzzword(word):
	global rules_db
	global verbose
	fuzz_lists = [] #lista com listas para realizar o fuzzy
	maxi_lists = [] #lista com o máximo de cada iteração
	inde_lists = [] #lista de iteração
	loop = 1
	fuzzywords = [] #return list
	for i in word:
		if i in rules_db.keys():
			fuzz_lists.append(rules_db[i])
			maxi_lists.append(len(rules_db[i])-1)
			inde_lists.append(0)
		else:
			fuzz_lists.append([i])
			maxi_lists.append(0)
			inde_lists.append(0)
	for i in maxi_lists:
		loop = loop*(i+1)

	for i in range(loop):
		word = translate(fuzz_lists, inde_lists)
		fuzzywords.append(word)
		if mirror:
			fuzzywords.append(word[::-1])
		if i != (loop-1):
			inde_lists=add(inde_lists,maxi_lists)

	for word in fuzzywords:
		print(word)

	return fuzzywords

def write():
	global output_
	global passlist
	global passfile

	if output_ != "":
		fileo = open(output_, "w")

	if passlist != []:
		for word in passlist:
			fuzzlist = fuzzword(word)
			if output_ != "":
				for fword in fuzzlist:
					fileo.write(fword+'\n')

	if passfile != "":
		try:
			filei = open(passfile, 'r')
		except:
			print("Can not open " + passfile)
			quit()
		for word in filei:
			word = word[:-1]
			fuzzlist = fuzzword(word)
			if output_ != "":
				for fword in fuzzlist:
					fileo.write(fword+'\n')
		filei.close()

	if output_ != "":
		fileo.close()

def main(argv):
	global passfile
	global output_
	global fuzzlevel
	global passwords
	global rules
	global rulefile
	global ego
	global listing
	global fuzzlevel
	global verbose
	global mirror
	if len(argv) == 2:
		return 1

	try:
		opts, args = getopt.getopt(argv[2:], "p:P:t:o:r:R:elLvm")
	except getopt.GetoptError as err:
		print(str(err))
		return 1

	for o, a in opts:
		if o == "-h":
			return 1;
		elif o == "-p":
			passwords = str(a)
		elif o == "-P":
			passfile = str(a)
		elif o == "-t":
			fuzzlevel = int(a)
		elif o == "-o":
			output_ = str(a)
		elif o == "-r":
			rules.append(str(a))
		elif o == "-R":
			rulefile = str(a)
		elif o == "-e":
			ego = 1
		elif o == "-l":
			listing = 1
		elif o == "-L":
			listing = 2
		elif o == "-v":
			verbose = True
		elif o == "-m":
			mirror = True

	if passfile == "" and passwords == "":
		return 2;

	if ego == 1:
		if rulefile == "" and rules == []:
			return 3;

	prepare_rules(fuzzlevel)
	if passwords != "":
		prepare_passwords()

	if listing != 0:
		list_rules(listing)

	write()

