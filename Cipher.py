# Friday, ‎August ‎19, ‎2016, ‏‎7:24:26 PM by Himanshu Sharma
import os
os.system("mode con:cols=100 lines=50")
os.system("color 0A")
os.system("title Transposition Cipher")
class tp():

    def __init__(self):
        self.i = 1
        self.addr = ''

    def fill(self, msg, key):
        if key > 0:
            parent = []
            
            if len(msg) % key == 0:
                for i in range(len(msg)/key):
                    char = ''
                    for j in range(key):
                        #print i, j
                        char+=msg[(key)*i + j]
                    parent.append(list(char))


            else:
                
                for i in range(len(msg)/key):
                    char = ''
                    for j in range(key):
                        #print i, j
                        #print "doing"
                        char+=msg[(key)*i + j]
                    parent.append(list(char))
                new = ''
                for k in range(len(msg) % key):
                    new += msg[(key)*(len(msg)/key) + k]
                parent.append(list(new))
                
                for m in range(key - len(msg) % key):
                    parent[-1].append('')
            return parent

        else:
            return False


    def fillFormatly(self, msg, key):

        org = key
        if len(msg) % key <> 0:
            key = len(msg)/key + 1
        else:
            key = len(msg)/key
        shade = org*key - len(msg)
        criticalIndex = (key - 1)*(shade)
        req = len(msg) - 1 - criticalIndex
        mainCode = msg[0:req+1:1]
        formated = msg[req+1:]
        parent = []
        for i in range(len(mainCode)/key):
            char = ''
            for j in range(key):
                #print i, j
                char+=mainCode[(key)*i + j]
            parent.append(list(char))

        for i in range(len(formated)/(key - 1)):
            char = ''
            for j in range(key - 1):
                #print i, j
                char+=formated[(key - 1)*i + j]
            parent.append(list(char))

        for m in range(key - len(formated) % key):
            parent[-m-1].append('')

        return parent

    def encrypt(self, msg, key):

        myList = self.fill(msg, key)
        code = ''
        
        lastList = myList[-1]
        maxIndexforall = len(lastList)
        #print maxIndexforall

        maxIndex = len(myList[0])
        mainList = myList[-2::-1]
        mainList = mainList[-1:-len(mainList)-1:-1]

        for i in range(maxIndex):
            for j in myList:
                code+=j[i]
        #print myList
        return code


    def decrypt(self, msg, key):
        
        myList = self.fillFormatly(msg, key)
        code = ''
        
        lastList = myList[-1]
        maxIndexforall = len(lastList)
        #print maxIndexforall

        maxIndex = len(myList[0])
        mainList = myList[-2::-1]
        mainList = mainList[-1:-len(mainList)-1:-1]

        for i in range(maxIndex):
            for j in myList:
                code+=j[i]
        #print myList
        return code
        

    def encrypt__(self, address, key):

        f = open(address, 'r')
        s = f.read()
        f.close()

        f1 = open('temp.txt', 'w')
        f1.write(s+'\n Credits Transposition Cipher')
        f1.close()


        f2 = open('temp.txt', 'r')
        s1 = f2.read()
        f2.close()

        os.remove('temp.txt')
        
        return self.encrypt(s1, key)

    def decrypt__(self, address, key):

        f = open(address, 'r')
        s = f.read()
        f.close()

        return self.decrypt(s, key)

    def bruteforce(self, address):

        self.addr = address
        f = open(address, 'r')
        s = f.read()
        f.close()
        try:

            while 1:
                my = self.decrypt(s, self.i)

                if "Transposition" in my:
                    break
                else:
                    self.i+=1

            return self.i

        except:
            self.i+=1
            return self.bruteforce(self.addr)
t = tp()

def run():
    try:
        x = raw_input("> ")

        if x == "encrypt":
            text = raw_input("Enter plain text: ")
            key = input("Enter a key: ")
            print t.encrypt(text, key)

        elif x == "decrypt":
            coded = raw_input("Enter coded text: ")
            key = input("Enter a key: ")
            print t.decrypt(coded, key)

        elif x[0:8] == "encrypt ":
            key = ''
            for i in x[8:]:
                if i <> ' ':
                    key += i
                else:
                    ind = x[8:].index(i)
                    #print ind
                    break
            addr = x[8:][ind + 1:]

            f = open(addr+" coded.txt", 'w')
            f.write(t.encrypt__(addr, int(key)))
            f.close()
            print "Done"
            print "Your decrypt code for file "+ addr + " is '" + str(addr)+" coded.txt'."
            

        elif x[0:8] == "decrypt ":

            key = ''
            for i in x[8:]:
                if i <> ' ':
                    key += i
                else:
                    ind = x[8:].index(i)
                    #print ind
                    break
            addr = x[8:][ind + 1:]

            print t.decrypt__(addr, int(key))

        elif x == "about":

            f = open("about.txt", 'r')
            s = f.read()
            f.close()

            print s

        elif x == "help":
            f = open("helpfile.txt", 'r')
            s = f.read()
            f.close()

            print s

        elif x[0:11] == "bruteforce ":
            print t.bruteforce(x[11:])

        elif x == '':
            pass

        elif x[0:5] == "kill ":
            os.remove(x[5:])
            print "Killed"

        else:
            print "Invalid command!!"


        run()

    except:
        print "Fatal Error!!"
        run()

run()


        
