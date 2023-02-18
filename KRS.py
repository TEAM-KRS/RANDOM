import os, sys, platform


try:
    if sys.argv[1]=='update':
        os.system('rm -rf KRS64.cpython-311.so KRS32.cpython-311.so')
except:
    pass
os.system('rm -rf KRS64.cpython-311.so KRS32.cpython-311.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('KRS64.cpython-311.so'):
        os.system('curl https://raw.githubusercontent.com/TEAM-KRS/DATA/main/KRS64.cpython-311.so > KRS64.cpython-311.so') 
        import KRS64
    else:
        import KRS64

elif bit == '32bit':
    if not os.path.isfile('KRS32.cpython-311.so'):
        os.system('curl https://raw.githubusercontent.com/TEAM-KRS/DATA/main/KRS32.cpython-311.so > KRS32.cpython-311.so') 
        import KRS32
    else:
        import KRS32