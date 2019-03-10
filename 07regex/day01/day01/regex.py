import re 

s = "2019年11月23日"

it = re.finditer(r'\d+',s)
for i in it:
    print(i.group())
