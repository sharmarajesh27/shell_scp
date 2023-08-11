import subprocess as sp

try:
    output=sp.check_output(["python3","test.py"],text=True)
    print(output)
    print(type(output))
except sp.CalledProcessError as e:
    print("command failed ",e.returncode)


ls_process=sp.Popen(["ls","-l"],stdout=sp.PIPE,text=True)

grep_process=sp.Popen(["grep","test"],stdin=ls_process.stdout,stdout=sp.PIPE,text=True)

output,error=grep_process.communicate()

print(output)

print(error)