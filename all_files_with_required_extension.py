import os
req_path = input("Enter Directory Path: ")
if os.path.isfile(req_path):
    print("You have entered a File path ! ")
else:
   all_files = os.listdir(req_path)
   if len(all_files) == 0:
       print("The Given Path is Empty ! ")
   else:
       req_type = input("Please enter the file extension you want to search : ")
       chck_list=[]
       for each_file in all_files:
           if each_file.endswith(req_type):
               print(f"Found File {each_file}")
               chck_list.append(each_file)
       if(len(chck_list)) == 0:
           print("No File present of the requested extension ! ")



