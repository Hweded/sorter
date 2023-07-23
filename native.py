import os
"""native execution of the copetree function from the shutil library"""
def copytree(src, dst):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            os.makedirs(d)
            copytree(s, d)
        else:
            if not os.path.exists(dst):
                os.makedirs(dst)
            with open(s, 'rb') as f:
                data = f.read()
            with open(d, 'wb') as f:
                f.write(data)