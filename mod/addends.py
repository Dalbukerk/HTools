import getopt

global debugbool
debugbool = False
global verbose
verbose = False
global ends
ends = ['', '123', "!@#", "12", "12345", '!@!']
global bool_common
bool_common = False #Set if option -c is used, to write common_ends, the list above
global numbers_string
numbers_string = ""
global Ends_string
Ends_string = ""
global pass_string 
pass_string = ""
global input_file
input_file = ""
global output_file
output_file = "wordlist.txt"
global Bool_List
Bool_List = False
global form
form = ""
global maker
maker =[]
global ind_max
ind_max = []
global iterator
iterator = []
global decimal
decimal = ['0','1','2','3','4','5','6','7','8','9']
global passes
passes = []
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

def debug(string):
    global debugbool
    global ends
    global numbers_string
    global Ends_string
    global pass_string
    global input_file
    global output_file
    global form
    global maker
    global ind_max
    global iterator
    global passes


    if debugbool:
        print( bcolors.WARNING + "+============ BEGIN DEBUG ============+" + bcolors.ENDC )
        print( bcolors.WARNING + string + bcolors.ENDC )
        print( bcolors.WARNING + "[+] Ends: " + str(ends) + bcolors.ENDC )
        print( bcolors.WARNING + "[+] numbers_string: " + numbers_string + bcolors.ENDC )
        print( bcolors.WARNING + "[+] Ends_string: " + Ends_string + bcolors.ENDC )
        print( bcolors.WARNING + "[+] Input File: " + input_file + bcolors.ENDC )
        print( bcolors.WARNING + "[+] Output File: " + output_file + bcolors.ENDC )
        print( bcolors.WARNING + "[+] FORM: " + form + bcolors.ENDC )
        print( bcolors.WARNING + "[+] IND MAX: " + str(ind_max) + bcolors.ENDC )
        print( bcolors.WARNING + "[+] passes: " + str(passes) + bcolors.ENDC )
        print( bcolors.WARNING + "+=====================================+" + bcolors.ENDC )
    
def help(code):
    if code in [0,1]:
        print("mode addends opetions")
        print("---------------------")
        print("     -h           : Show this help")
        print("     -v           : Print passwords in screen")
        print("     -c           : Add common ends like 123, !@#, 12345 at the end of each password")
        print("                  : No arg, the script will do a list for you")
        print("     -n <numbers> : Add number list at the end of each password")
        print("                  : Ex: '-n 8-10,90' will add the numbers 8,9,10 and 90 at the end of each password")
        print("     -E <ends>    : Add custom ends to each password. The arg must be separated by ','")
        print("     -p <pass>    : Select passwords separated by ','")
        print("     -i <file>    : Select a file with passwords to edit")
        print("     -o <file>    : Select a file to output")
        print("                  : default is wordlist.txt")
        print("     -L           : List all ends to be added")
        print("     -f format    : Select the format of password")
        print("                  : %0 -- digit 0 to 9")
        print("                  : %e -- end (123,!@#) or ends passed with -E option")
        print("                  : %d -- days -- 01,02, ... ,31")
        print("                  : %M -- months -- jan, fev, ... ,dez")
        print("                  : %0 -- digit 0 to 9")
        print("                  : Default is %e, password followed by 'end'")
        print("     Ex:%p%0%0    : Password will go from 'pass00' to 'pass99'")
    if code == 2:
        print("==> YOU MUST GIVE AT LEAST ONE PASSWORD WITH -p OR -i OPTIONS <==")
        print("mode addends opetions")
        print("---------------------")
        print("     -h           : Show this help")
        print("     -c           : Add common ends like 123, !@#, 12345 at the end of each password")
        print("                  : No arg, the script will do a list for you")
        print("     -n <numbers> : Add number list at the end of each password")
        print("                  : Ex: '-n 8-10,90' will add the numbers 8,9,10 and 90 at the end of each password")
        print("                  : Ex: '-N 6-10' will add the number 06,07,08,09 and 10 at the end of each password")
        print("     -E <ends>    : Add custom ends to each password. The arg must be separated by ','")
        print("     -p <pass>    : Select passwords separated by ','")
        print("     -i <file>    : Select a file with passwords to edit")
        print("     -o <file>    : Select a file to output")
        print("                  : default is wordlist.txt")
        print("     -L           : List all ends to be added")
        print("     -f format    : Select the format of password")
        print("                  : %m -- months -- 01,02, ... ,12")
        print("                  : %d -- days -- 01,02, ... ,31")
        print("                  : %M -- months -- jan, fev, ... ,dez")
        print("                  : %0 -- digit 0 to 9")
        print("                  : %e -- end (123,!@#) or ends passed with -E option")
        print("                  : Default is %p%e, password followed by 'end'")
        print("     Ex:%p%0%0    : Password will go from 'pass00' to 'pass99'")
    if code != 0:
        exit()


def list_what():
    global form
    global ends
    global input_file
    global output_file
    global ind_max 
    global passes

    string = ""
    for item in ends:
        string = string + item + ","

    print("[+] Ends to be added: " + string[:-1])
    
    string = "<password>"
    if form != "":
        for i in form:
            if i == "m":
                string = string + "<01...12>"
            elif i == "M":
                string = string + "<jan...dez>"
            elif i == "d":
                string = string + "<01...31>"
            elif i == "0":
                string = string + "<0...9>"
            elif i == "e":
                string = string + "<123...!@#>"
        print("[+] Password format: " + string)

    print("[+] Passwords will be saved in " + output_file)
    
    string = ""
    for p in passes:
        string = string + p + ','
    print("[+] Passwords passed by -p option: " + string[:-1])


def scan_format(form):
    size_f = len(form)
    if (size_f%2) != 0:
        return 1
    for i in range(0,size_f,2):
        if form[i] != "%" or (form[i+1] not in ["p", "0", "m", "M", "d"]):
            return 1
    if count(form, "l") > 1:
        return 1
    if count(form, "e") > 1:
        return 1
    return 0


def prepare():
    global numbers_string
    global Ends_string
    global pass_string
    global passes
    global form
    global maker
    global ind_max
    global iterator
    global decimal
    global passes
    global ends
    global days
    global months
    global mon_letter

    passwd_to_add = pass_string.split(',')
    for p in passwd_to_add:
        passes.append(p)
    if numbers_string != "": 
        numbers_to_add = numbers_string.split(",")
        for n in numbers_to_add:
            if count(n,"-") == 0:
                ends.append(n)
            else:
                mini = int(n.split("-")[0])
                maxi = int(n.split("-")[-1])
                for i in range(mini,maxi+1):
                    ends.append(str(i))
    
    if Ends_string != "":
        ends_to_add = Ends_string.split(",")
        for end in ends_to_add:
            ends.append(end)

    if form != "":
        for i in form:
            if i == "0":
                maker.append(decimal)
                ind_max.append(10)
                iterator.append(0)
            elif i == "e":
                maker.append(ends)
                ind_max.append(len(ends))
                iterator.append(0)
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

def sumit():
    global iterator
    global ind_max
    size = len(iterator)
    iterator[-1] += 1
    for i in range(0,size-1):
        if iterator[size-i-1] == ind_max[size-i-1]:
            iterator[size-i-1] = 0
            iterator[size-i-2] += 1
    #print(str(iterators)+" "+ str(ind_max))
    return 0

def iteratorz():
    global iterator
    for i in range(len(iterator)):
        iterator[i]=0;

def count(string, char):
    q = 0
    for i in string:
        if i == char:
            q+=1
    return q

def getpass():
    global iterator
    global maker
    passwd = ""
    for i in range(len(iterator)):
        passwd = passwd + maker[i][iterator[i]]
    return passwd
1

def write():
    global form
    global maker
    global ind_max
    global iterator
    global passes
    global ends
    global input_file
    global output_file
    global verbose

    fileo = open(output_file, "w")

    if form == "":
        for p in passes:
            for end in ends:
                fileo.write(p+end+'\n')
                if verbose:
                    print(p+end)
        if input_file != "":
            filei = open(input_file, "r")
            for line in filei:
                for end in ends:
                    fileo.write(line[:-1]+end+'\n')
                    if verbose:
                        print(p+end)
    else:
        total = 1
        for i in ind_max:
            total = total*i
        for p in passes:
            for i in range(total):
                end = getpass()
                fileo.write(p+end+'\n')
                if verbose:
                    print(p+end)
                sumit()
            iteratorz()
        if input_file != "":
            filei = open(input_file, "r")
            for line in filei:
                for i in range(total):
                    end = getpass()
                    fileo.write(p+end+'\n')
                    if verbose:
                        print(p+end)
                    sumit()
                iteratorz()

    fileo.close()


def main(argv):
    global bool_common
    global numbers_string
    global Ends_string
    global pass_string
    global input_file
    global output_file
    global Bool_List
    global form
    global debugbool
    global verbose

    if len(argv) == 2:
        return 1;

    try:
        opts, args = getopt.getopt(argv[2:], "hvcn:E:p:i:o:Lf:d",[])
    except getopt.GetoptError as err:
        print(str(err))
        return 1

    for o,a in opts:
        if o == "-h":
            return 1;
        elif o == "-c":
            bool_common = True;
        elif o == "-n":
            numbers_string=str(a)
        elif o == "-E":
            Ends_string=str(a)
        elif o == "-p":
            pass_string=str(a)
        elif o == "-i":
            input_file = str(a)
        elif o == "-o":
            output_file = str(a)
        elif o == "-L":
            Bool_List = True
        elif o == "-f":
            form = str(a)
        elif o == "-d":
            debugbool = True
        elif o == "-v":
            verbose = True

    if form != "":
        scan_format(form)


    if pass_string == "" and input_file == "":
        return 2;

    debug("Before prepare()")

    prepare()

    debug("After prepare()")

    if Bool_List == True:
        list_what()

    write()
