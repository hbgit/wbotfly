import os

start_path = 'Dir_ALLClasses' # current directory
for path,dirs,files in os.walk(start_path):
    print(dirs)    
    for filename in files:
        print("python classify.py --image_file " + os.path.join(path,filename))
        print(str(dirs) + "==" + "panda")
