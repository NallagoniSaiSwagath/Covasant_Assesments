#Recursively go below a dir and based on filter, dump those files in to  single file 
import os
path=r"C:\Users\N. Sai Swagath\Desktop\example"

for root,dir,files in os.walk(path):
    for file in files:
         if file.endswith(".txt") and file != "merge.txt":

            fullpath=os.path.join(root,file)
            with open(fullpath,"rt") as f1:
                content=f1.readlines()
                with open(path+"\merge.txt","a") as f2:
                    f2.write(f"\n--- From: {file} ---\n")
                    f2.writelines(content)

                







