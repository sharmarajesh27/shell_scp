import subprocess as sp

cm1=sp.run(["cat","json1.txt"],stdout=sp.PIPE,text=True)

cm2=sp.run(["grep","-n","Munish"],input=cm1.stdout,text=True,capture_output=True)


#cm3=sp.run(["grep","-ztf","Munish"],input=cm1.stdout,text=True,stderr=sp.DEVNULL)





print("out for ",cm2.stdout)
print("error is ",cm2.stderr)
print("reson code ",cm2.returncode)

with open("json1.txt","r") as f:
    cm4=sp.run(["grep","-n","Pyth"],stdin=f,text=True)
