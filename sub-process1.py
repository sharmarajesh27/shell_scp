
#subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)


import subprocess as sp

#sp.call(['pwd'],shell=True)


result=sp.run(['pwd'],shell=True,capture_output=True,text=True)

print("================")

print("Result",result)

print("stdout ",result.stdout)

print("================")
print("stderr ",result.stderr)

print("return code ",result.returncode)

print("hello")



print("hello there")
temp=sp.run(["sh", "/home/rajesh/shell_scp/test.sh"],capture_output=True,text=True)
print(temp.stdout)

new=sp.run(["python3","test.py"],capture_output=True,text=True)

print(new.stdout)
print(type(new.stdout))
print(new.returncode)

