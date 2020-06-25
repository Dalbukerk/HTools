import getopt


global usernames
usernames = []
global userfile
userfile = ""
global passwords
passwords = []
global passfile
passfile = ""
global bigfile
bigfile = ""
global output
output = ""
global form
form = ""
global decimal
decimal = ["0","1","2","3","4","5","6","7","8","9"]
#FORMAT
global maker
maker = [] #List with lists
global ind_max
ind_max = [] #List with maxs
global iterators
iterators = []
global separator
separator = " "
global days
days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','21','22','23','24','25','26','27','28','29','30','31']
global months
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
global mon_letter
mon_letter = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']

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
        print("mode userpass options")
        print("---------------------")
        print("     -h        : Show this help")
        print("     -l login  : Select usernames separeted by ','")
        print("     -L file   : Select a file with usernames in each line")
        print("     -p pass   : Select a password to put with each username")
        print("     -P file   : Select a password to put with each username")
        print("               : Use files with less than 100 passwords")
        print("               : This options catches only 100 passwords in a file")
        print("     -B file   : Use if the wordlist (passwords) have more than 100 lines")
        print("     -o file   : Select the name for the output file")
        print("     -s char   : Select the char to separate the username from password")
        print("               : Default is ' ', it could be :,%$ etc...")
        print("     -f format : Select the format of password")
        print("               : %u -- username")
        print("               : %0 -- digit 0 to 9")
        print("               : %p -- password")
        print("               : %m -- months -- 01,02, ... ,12")
        print("               : %d -- days -- 01,02, ... ,31")
        print("               : %M -- months -- jan, fev, ... ,dez")
        print("               : Default is %p, only passwords passed by -p, -P or -B")
    elif code == 2:
        print(bcolors.FAIL+"Bad format given by -f"+bcolors.ENDC)
        print("     -f format : Select the format of password")
        print("               : %l -- username, passed by -l or -L")
        print("               : %0 -- digit 0 to 9")
        print("               : %p -- password, passed by -p, -P or -B")
        print("               : Default is %p, only passwords passed by -p, -P or -B")
        print("     Ex:%l%0%0 : Password will go from 'user00' to 'user99'")
    elif code == 3:
        print(bcolors.FAIL+"Incompatible options -B and -P"+bcolors.ENDC)
    elif code == 4:
        print(bcolors.FAIL+"You must give at least one username with options -l or -L"+bcolors.ENDC)
    if code != 0:
        exit()

def count(word, l):
    c = 0
    for i in word:
        if i == l:
            c+=1
    return c

def scan_format(form):
    size_f = len(form)
    if (size_f%2) != 0:
        return 1
    for i in range(0,size_f,2):
        if form[i] != "%" or (form[i+1] not in ["l", "p", "0","m","M","d"]):
            return 1
    if count(form, "l") > 1:
        return 1
    if count(form, "p") > 1:
        return 1
    return 0

def sumit():
    global iterators
    global ind_max
    size = len(iterators)
    iterators[-1] += 1
    for i in range(0,size-1):
        if iterators[size-i-1] == ind_max[size-i-1]:
            iterators[size-i-1] = 0 
            iterators[size-i-2] += 1
    #print(str(iterators)+" "+ str(ind_max))
    return 0

def iteratorz():
    global iterators
    for i in range(len(iterators)):
        iterators[i]=0;

def getpass():
    global iterators
    global maker
    passwd = ""
    for i in range(len(iterators)):
        passwd = passwd + maker[i][iterators[i]]
    return passwd 

def write():
    global output
    global form
    global usernames
    global passwords
    global separator
    global ind_max
    global iterators
    global maker

    if form == "":
        if output != "":
            fileo = open(output, "w")
            for user in usernames:
                for passwd in passwords:
                    fileo.write(user+separator+passwd+"\n")
            fileo.close()
        else:
            for user in usernames:
                for passwd in passwords:
                    print(user+separator+passwd)
    else:    
        if output == "":
            total = 1
            for i in ind_max:
                total = total*i
            for user in usernames:
                for i in range(total):
                    passwd = getpass()
                    print(user+separator+passwd)
                    sumit()
                iteratorz()
        else:
            fileo = open(output, "w")
            for i in ind_max:
                total = total*i
            for user in usernames:
                for i in range(total):
                    passwd = getpass()
                    fileo.write(user+separator+passwd)
                    sumit()
                iteratorz()
            fileo.close()



def prepare():
    global usernames
    global userfile
    global passwords
    global passfile
    global form
    global maker
    global ind_max
    global iterators
    global decimal
    global months
    global mon_letter
    global days

    if len(usernames) == 1:
        logins = usernames[0]
        usernames = []
        logins = logins.split(",")
        for login in logins:
            usernames.append(login)

    if len(passwords) == 1:
        passs = passwords[0]
        passwords = []
        passs = passs.split(",")
        for pas in passs:
            passwords.append(pas)

    if passfile != "":
        passin = open(passfile, "r")
        n = 0;
        for word in passin:
            if n < 100:
                passwords.append(word)
            n+=1

    if userfile != "":
        userin = open(userfile, "r")
        n = 0;
        for word in userin:
            if n < 100:
                usernames.append(word)
            n+=1

    if form != "":
        for i in form:
            if i == "l":
                maker.append(usernames)
                ind_max.append(len(usernames))
                iterators.append(0)
            elif i == "p":
                iterators.append(0)
                maker.append(passwords)
                ind_max.append(len(passwords))
            elif i == "0":
                maker.append(decimal)
                ind_max.append(len(decimal))
                iterators.append(0)
            elif i == "m":
                maker.append(months)
                ind_max.append(len(months))
                iterator.append(0)
            elif i == "d":
                maker.append(days)
                ind_max.append(len(days))
                iterator.append(0)
            elif i == "M":
                maker.append(mon_letter)
                ind_max.append(len(mon_letter))
                iterator.append(0)

def main(argv):
    global usernames
    global userfile
    global passwords
    global passfile
    global bigfile
    global output
    global form
    global separator
    code = 0

    if len(argv) == 2:
        return 1

    try:
        opts, args = getopt.getopt(argv[2:], "hl:L:p:P:B:o:f:s:",[])
    except getopt.GetoptError as err:
        print(str(err))
        return 1

    for o, a in opts:
        if o == "-h":
            return 1
        elif o == "-l":
            usernames.append(str(a))
        elif o == "-L":
            userfile = str(a)
        elif o == "-p":
            passwords.append(a)
        elif o == "-P":
            passfile = str(a)
        elif o == "-B":
            bigfile = str(a)
        elif o == "-o":
            output = str(a)
        elif o == "-f":
            form = str(a)
        elif o == "-s":
            separator=str(a)

    if form != "":
        code = scan_format(form);
        if code == 1:
            return 2

    if passfile != "" and bigfile !="":
        return 3

    if usernames == [] and userfile == "":
        return 4

    prepare() 

    write()


    return 0
