import getopt

separators = ['','@','#','$','&']
filename1 = ""
filename2 = ""
outputfile = ""


def help(code):
    print("mode mix files")
    print("--------------")
    print("     -h        : Show this help")
    print("     -f file   : first file")
    print("     -F file   : second file")
    print("     -o file   : Output file")
    print("     -s 'char' : Character to be used as separator")
    print("               : Example: -s : means word1:word2")
    print("               : If no char is set by option -s, mix")
    print("               : will use '',@,#,$,&...")
    print("--------------")
    print("  Usage: wed.py mix -f file1.txt -F file2.txt -s \"@\"")
    

def mix(filename1, filename2, outputfile):
    global separators

    try:
        file1 = open(filename1,'r')
    except:
        print("Failed to read " + filename1 )
        exit()
    try:
        file2 = open(filename2,'r')
    except:
        print("Failed to read " + filename2 )
        exit()
    if outputfile != "":
        o = open(outputfile,'w')
        for line1 in file1:
            file2 = open(filename2,'r')
            str1 = line1.strip()
            for line2 in file2:
                str2 = line2.strip()
                for s in separators:
                    o.write(str1 + s + str2 + "\n")
            file2.close()
        o.close()
    else:
        for line1 in file1:
            str1 = line1.strip()
            for line2 in file2:
                str2 = line2.strip()
                for s in separators:
                    print(str1 + s + str2)


def main(argv):
    global filename1
    global filename2
    global outputfile
    global separators
    if len(argv) == 2:
        return 1

    code = 0
    if len(argv) == 2:
        return 1
    try:
        opts, args = getopt.getopt(argv[2:], "hf:F:s:o:",[])
    except getopt.GetoptError as err:
        print(str(err))
        return 1

    for o, a in opts:
        if o == "-h":
            help()
            exit()
        elif o == "-f":
            filename1 = str(a)
        elif o == "-F":
            filename2 = str(a)
        elif o == "-o":
            outputfile = str(a)
        elif o == "-s":
            separators = [a]

    mix(filename1,filename2,outputfile)
    return 0

