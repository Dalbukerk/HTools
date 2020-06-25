# WordlistEditor
A simple tool to edit and create some wordlists easily.

This script is sapareted in 3 modules:
#userpass
#addends
#fuzzy

## USERPASS
The userpass module is design to create wordlists with user and pass in each line.
For example, the command:

```bash
$ ./wed.py userpass -l davi -p pass -f %p%0%0
```

will create a wordlist with "davi pass00" in each line, where 0 is representing a number of one to ten:

```bash
davi pass00
davi pass01
davi pass02
davi pass03
davi pass04
davi pass05
```

It can be used to create a sequence of single password line using the option "-s":
```bash
$ ./wed.py userpass -l password -s @ -f %0%0
password@00
password@01
password@02
password@03
password@04
password@05
password@06
...
password@96
password@97
password@98
password@99
```

## ADDENDS

the addends module was design for add commons endings of passwords such as 123, !@#, 12, 12345, etc.

For example:
```bash
$ ./wed.py addends -p password -c -v -f %p%e
password
password123
password!@#
password12
password12345
password!@!
$ ./wed.py addends -p password -c -v -f %p%0
password0
password1
...
password7
password8
password9
$ ./wed.py addends -p password -c -v -f %p%0%e
password0
password0123
password0!@#
password012
...
password9!@#
password912
password912345
password9!@!
```

## FUZZY

This modulo was made to create variations of a word like:
ricardo -- r1c4rd0 -- r!c@rd0 -- ...

You can select a type of fuzzing, which is a number among 1,2 or 3:
```bash
1 - 1337 on vowels
2 - 1337 on consonants
3 - More symbols
```
The output examples:

```bash
$ ./wed.py fuzzy -p password -v -t 1
p4ssword
password
p4ssw0rd
passw0rd

$ ./wed.py fuzzy -p password -v -t 3
p4ssword
password
p@ssword
...
p@5$w0rd
p4$$w0rd
pa$$w0rd
p@$$w0rd
```
You can create your own rules with option '-r':
```bash
$ ./wed.py fuzzy -p password -v -t 1 -r p:p,P
p4ssword
P4ssword
password
Password
p4ssw0rd
P4ssw0rd
passw0rd
Passw0rd
```
Here we notice: the rule must be something like p:p,P. This means that the letter p will be substituted by p and P. If the rule is p:P, the output is:

```bash
$ ./wed.py fuzzy -p password -v -t 1 -r p:P
P4ssword
Password
P4ssw0rd
Passw0rd
```



In case of doubts or sugestions, I'm available in my email: davigalbuquerque@gmail.com
