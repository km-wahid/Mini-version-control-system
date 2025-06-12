import hashlib
import os

def vcs_add(filename):
    with open(filename, 'rb') as f:
        content = f.read()
        
    
    sha1 = hashlib.sha1(content).hexdigest
    
    file_path = os.path.join(".vcs", 'objects', sha1 )
    
    if not os.path.exists(file_path):
        with open(file_path,"wb") as file:
            file.write(content)
         
    with open(os.path.join('.vcs', 'index,','a')) as index:
        index.write(f"{sha1} {filename}\n")
    
    print(f"Added '{filename}' to staging area.")
    
    
