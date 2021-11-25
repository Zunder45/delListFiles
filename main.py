import os
import conf as c


errs = 0
ok = 0


for pathItem in c.path:

    os.chdir(pathItem)
    lsdir = os.listdir()

    for item in lsdir:

        try:
            if os.path.isfile(item):
                if item in c.file_ignore:
                    print(pathItem + item + " ignore")
                    continue
                os.remove(item)  
                print(pathItem + item + " del")
                ok += 1
                continue
        except:
            errs += 1
            print("err 1")

        try:    
            if os.path.isdir:
                if item in c.file_ignore:
                    print(pathItem + item + " ignore")
                    continue
                os.rmdir(item) 
                print(pathItem + "/" + item + " del")
                ok += 1
                continue
        except:
            errs += 1
            print("err 1")
            
print("OK " + str(ok) + " ERRS " + str(errs))  



