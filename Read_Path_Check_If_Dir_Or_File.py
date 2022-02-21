import os
while True:
    path = input("Enter your path :  ")
    if os.path.exists(path):
        if os.path.isfile(path):
            print(f"The Given {path} Is File !")
        else:
            print(f"The Given {path} is a directory !! ")
        break
    else:
        print("The Path Doesn't Exists Please Enter The Path Again")
        continue
