import os
path=input("Please enter your directory path : ")
if os.path.exists(path):
    dircntnt=os.listdir(path)
    if bool(dircntnt) == False:
        print("The Directory Is Empty")
    else:
        print(f"The content of directory : {dircntnt}")
else:
    print("The Directory doesn't exists")