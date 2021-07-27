import simplejson
a=["neelam","programer",24,2400,]
b=["komal","trainer",24,20000]
c=["anuradha","HR",25,40000]
d=["Abhishek","manager",29,63000]
key=["name","degination","age","salary"]
dict1={}
dict2={}
dict3={}
dict4={}
dict5={"dict1":dict1,"dict2":dict2,"dict3":dict3,"dict4":dict4}
for i in range(len(a)):
    dict1.update({key[i]:a[i]})
for j in range(len(b)):
    dict2.update({key[i]:b[i]})
for k in range(len(c)):
    dict3.update({key[i]:c[i]})
for l in range(len(d)):
    dict4.update({key[i]:d[i]})

with open("q8.json","w") as f:
    simplejson.dump(dict5,f,indent=4)
    
    
# out_file=open("pranjufile.json","w")
# json.dump(dict,out_file,indent=6)
# out_file.close()
# import json
# dict5={"dict1":"dict1","dict2":"dict2","dict3":"dict3","dict4":"dict4"}
# with open("dict5.json","w") as f:
#     json.dump(dict5,f,indent=4)