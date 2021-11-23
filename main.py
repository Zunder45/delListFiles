import os
import conf as c


errs = 0
ok = 0

print(c.path)

os.chdir(c.path)
lsdir = os.listdir()

for item in lsdir:

    if os.path.isfile(item):
        if item in c.file_ignore:
            print(item + " ignore")
            continue
        os.remove(item)  
        print(item + "del")
        ok += 1
        continue
    if os.path.isdir:
        if item in c.file_ignore:
            print(item + " ignore")
            continue
        os.rmdir(item) 
        print("/" + item + "del")
        ok += 1
        continue

print("OK " + str(ok) + " ERRS " + str(errs))  



