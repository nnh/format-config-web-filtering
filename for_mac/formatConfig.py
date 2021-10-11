import re
with open('/Users/mariko/Downloads/input.conf') as f:
    config = f.readlines()
targetList = ['URL\n']
targetFlag = False
for line in config:
    line = line.rstrip()
    if targetFlag and re.search(r'^ *set url "\*"$', line):
        break  
    if targetFlag and re.search(r'^ *set url .*', line):
        temp = line.replace('set url', '')
        temp = temp.replace('"', '')
        temp = temp.split()
        targetList.append(temp[0] + '\n')
    if line == '        set name "NMCCRC_Filter"':
        targetFlag = True
with open('/Users/mariko/Downloads/output.txt', 'w', encoding='utf-8', newline='\n') as wf:
    wf.writelines(targetList)
