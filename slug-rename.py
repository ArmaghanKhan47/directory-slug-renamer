import os

def slug(name):
    return '-'.join(name.lower().split(' '))

def rename(name):
    sl = slug(name)
    print('{0} --> {1}'.format(name, sl))

    try:
        os.rename(name, sl)
    except(PermissionError):
        print('!!! Permission Error !!!')
print('!!! Process Starting !!!')

cwd_path = os.getcwd()
dir_list = [x for x in os.listdir() if os.path.isdir(x)]

for x in dir_list:
    rename(x)

input('!!! Process Completed !!!')
