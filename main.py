
import sys
import os
import colorama


def progress_bar(total, progress):
    percent = 100*(progress/float(total))
    bar = '#'*int(percent) + '-'*int((100-percent))
    # print(percent)
    if total==progress:
        print(f"{colorama.Fore.GREEN} \r[{bar}] {percent:.2f}%", end="\r")
    else:
        print(f"{colorama.Fore.YELLOW} \r[{bar}] {percent:.2f}%", end="\r")

args = sys.argv

if len(sys.argv)<4:
    print(f'{colorama.Fore.RED} Usage: ')
    print(f"{colorama.Fore.GREEN}      python main.py <text to look for> <file name to store results> <path to the data directory in BreachCompilation>")
    print(f'{colorama.Fore.RED} Example: ')
    print(f'{colorama.Fore.GREEN}      python main.py gmail.com gmail C:\\Downloads\\BreachCompilation\\data')
    print(colorama.Fore.RESET)
    exit()
query_string = args[1]
filename = args[2]
data_path = args[3]




files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(data_path):
    for file in f:
        files.append(os.path.join(r, file))
print(len(files))
progress_bar(total=len(files), progress=0)

for i, f in enumerate(files):
    with open(f, 'r', encoding="latin-1") as file:
        l=file.readlines()
    
    with open(f'{filename}-master.txt', 'a', encoding="latin-1") as wfile:
        for line in l:
            if query_string in line:
                wfile.write(line)
    progress_bar(total=len(files), progress=i+1)
print('\n')

print(f'{colorama.Fore.RED} [+] Writing to {filename}-users.txt and {filename}-password.txt')


with open(f'{filename}-master.txt', 'r', encoding='latin-1') as mfile:
    lines = mfile.readlines()
    progress_bar(total=len(lines), progress=0)
    for i, line in enumerate(lines):
        if len(line.split(':')) == 2:
            user = line.split(':')[0]
            password = line.split(':')[1]
        else:
            user = line.split(':')[0]
            password = ' \n'
        with open(f'{filename}-users.txt', 'a', encoding='latin-1') as ufile:
            ufile.write(user+'\n')
        with open(f'{filename}-passwords.txt', 'a', encoding='latin-1') as pfile:
            pfile.write(password)
        progress_bar(progress=i+1, total=len(lines))
        

print(colorama.Fore.RESET)
