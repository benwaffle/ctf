import subprocess, string
target = '221.164.100.10.237.97.167.177.205.54.30.53.124.232.78.134.215.10.37.45.30.244.131.235.116.131.237.237.85.27.210.205.35.76.5.5.210.102.157.157.3.96.114.25.91.238.192'.split('.')

flag=''

def run(arg):
    return subprocess.check_output('./pizazz ' + arg, shell=True).split('.')[:-1]

while len(flag) < len(target):
    print flag
    for c in string.printable:
        if c in '\'"()$<>`|\r\v\n':
            continue
        if run(flag+c) == target[:len(flag)+1]:
            flag += c
            break

print flag
