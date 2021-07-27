

import simplejson
file="Text.txt"
dict={}
k=open(file)
for i in k:
    key,dic=i.split(None,1)
    dict[key]=dic.strip()
new_file=open("y.json","w")
simplejson.dump(dict,new_file,indent=4)
new_file.close()


