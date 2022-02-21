import subprocess
cmd="dir"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(f"The return code is {rc}")
print(f"The output is :{out}")
print(f"The error is : \n{err}")