import subprocess
import os

subprocess.Popen('echo "hi world"',shell=True)

subprocess.run(["sh","pwd"],shell=True)

'''os.system('pwd')
#print("------------------------------------")

os.system('echo "======================================="')

#os.system('cat sub_os.py')


#subprocess.call(['sh','./test.sh'])

os.system("sh test.sh")'''