import os
import pandas as pd

op_name=os.name


if(op_name=='posix'):
    print("Running Linux shell commands")
    cmd='ls -lht >linx.txt'
    os.system(cmd)
    # you can also store the output of a command in a variable
    temp=os.popen('ls -la').read()
    print("out of command ls -la is \n")
    print(temp)

elif(op_name=='nt'):
    print("Running commands on windows")
    os.system('dir >win.txt')
    temp=os.popen('dir').read()
    print("output of dir command is \n")
    print(temp)
else:
    print("os not recognised")

print("hello code updated")