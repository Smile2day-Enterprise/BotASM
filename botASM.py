#!/usr/bin/python

## BotScript 2015
## A simple scripting language that is useful for creating bots.


## Imports:
import re,urllib,urllib2,time,sys,shlex,os,cookielib,getpass
#print "source/"+os.path.basename(__file__).replace(".exe","").replace(".py","")
Script = sys.argv[1]
Instructions = [line.strip() for line in open(Script)]
Stack = dict()
postStack = dict()
codePointer = 0
## Declare opener
cj = cookielib.CookieJar()
web = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))



##
def load(name):
    Stack[name] = open("\\Saves\\"+name+".botasmdata").read()
    if Stack[name].strip() == "":
        # nothing was loaded.
        # write new data to file
        open("\\Saves\\"+name+".botasmdata","w+").write(raw_input("\n"+name+": "))
        # Recursive load :)
        load("\\Saves\\"+name+".botasmdata")

def save(name,data):
    # write data to file
    open("\\Saves\\"+name+".botasmdata","w+").write(data)
def GetUsernameFromID(username):
    url = "http://www.marapets.com/login.php?do=dologin"
    values = {'username' : username}
    strHTML = HoHo(url,values)
    idMatch = re.compile("<input type='hidden' name='id' value='(.*?)'>")
    try:
        UserID = idMatch.findall(strHTML)
        return UserID[0]
    except:
        print "User does not exist."
        Marapets_Login()

def Marapets_Login():
    m_username = load("marapets_username")
    m_password = load("marapets_password")
    if m_username.strip() == "":
        save(raw_input("Marapets Username:"),"marapets_username")
        save(raw_input("Marapets Password:"),"marapets_password")
        m_username = load("marapets_username")
    if m_password.strip() == "":
        save(getpass.getpass(m_username+"'s password:"),"marapets_password")
    UserID = GetUsernameFromID(username)
    print UserID
    loginData = {'id' : UserID, 'password' : PasswordControl.GetValue()}
    url = "http://www.marapets.com/dologin.php"
    SetStatus(UsernameControl.GetValue()+" - ******")
    if web(url,loginData) == "Bad Username":
        SetStatus("User does not exist.")
        #Stop()
    time.sleep(1)
def Regex(pattern,string):
    pattern = re.compile(pattern)
    try:
        return pattern.findall(string)
    except:
        return None

def HoHo(url):
    try:
        data = web.open(url).read()
    except:
        data = "error"
    return data
def pastebinupdate(pastebinurl):
    page = HoHo(pastebinurl)
    regex = re.compile("\)\">(.*?)</textarea>",re.MULTILINE|re.DOTALL)
    pscript = regex.findall(page)[0].replace("&quot;","\"").replace("&amp;","&")
    if open(Script).read() != pscript:
        open(Script,"w+").write(pscript)
        raw_input("Program updated. Please re-open! Press [ENTER] to close.")
        sys.exit(0)
        
def HoHoHo(url,postdata):
    try:
        data = web.open(url,postdata).read()
    except:
        data = "error"
    return data

while codePointer <= len(Instructions):
    try:
        i = shlex.split(Instructions[codePointer])
    except:
        break
    try:
        i[0] = i[0].lower()
    except:
        print codePointer
    if i[0] == "wait":
        time.sleep(int(i[1]))
        
    elif i[0] == "print":
        sys.stdout.write(i[1])
        
    elif i[0] == "printf":
        print i[1]
        
    elif i[0] == "printv":
        sys.stdout.write(Stack[i[1]])

    elif i[0] == "py":
        code = compile(i[1], '<string>', 'exec')
        exec code
    elif i[0] == "v":
        Stack[i[2]] = i[1]
    elif i[0] == "exit":
        sys.exit(0)
    elif i[0] == "input":
        Stack[i[2]] = raw_input(i[1])
    elif i[0] == "password":
        Stack[i[2]] = getpass.getpass(i[1])
    elif i[0] == "getset":
        Stack[i[2]] = HoHo(i[1])
    elif i[0] == "get":
        HoHo(i[1])
    elif i[0] == "load":
        load(i[1])
    elif i[0] == "save":
        save(i[1],Stack[i[2]])
    elif i[0] == "jmpif":
        if i[2] == "=" or i[2] == "==":
            if Stack[i[1]] == i[3]:
                codePointer += inti[4]
    elif i[0] == "jmpifv":
        if i[2] == "=" or i[2] == "==":
            if Stack[i[1]] == Stack[i[3]]:
                codePointer += int(i[4])
                codePointer = codePointer - 1
    elif i[0] == "loop":
        codePointer = codePointer - int(i[1])
        codePointer = codePointer - 1
    elif i[0] == "post": 
        url = i[1]
        data = urllib.urlencode(postStack)
        postStack.clear()
        junk = HoHoHo(url,data)
        
    elif i[0] == "postset":
        url = i[1]
        data = urllib.urlencode(postStack)
        postStack.clear()
        Stack[i[2]] = HoHoHo(url,data)
    elif i[0] == "poststack":
        postStack[i[1]] = i[2]
    elif i[0] == "pastebin_update":
        pastebinupdate(i[1])
    elif i[0] == "poststackv":
        postStack[i[1]] = Stack(i[2])
    elif i[0] == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif i[0] == "json":
        web.addheaders = [('Content-type','application/json')]
    elif i[0] == "useragent":
        if i[1] == "firefox":
            web.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0')]
        elif i[1] == "chrome":
            web.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
        elif i[1] == "ie" or i[1] == "internet explorer":
            web.addheaders = [('User-agent', 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko')]
    codePointer += 1
raw_input("\nPress [ENTER] to exit.")
