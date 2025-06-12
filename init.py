import os

def vcs_init(path='.'):
    vcs_dir = os.path.join(path, '.vcs')

    if os.path.exists(vcs_dir):
        print("Repository already initialized.")
        return

    os.makedirs(os.path.join(vcs_dir, 'objects'))    
    os.makedirs(os.path.join(vcs_dir, 'refs'))        
    with open(os.path.join(vcs_dir, 'HEAD'), 'w') as f:
        f.write('ref: refs/heads/main\n')           
    with open(os.path.join(vcs_dir, 'config'), 'w') as f:
        f.write('[core]\n\trepositoryformatversion = 0\n')

    print(f"Initialized empty VCS repository in {os.path.abspath(vcs_dir)}")


# vcs_init()