import simplejson
x={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20"
        }, 
}
print(type(x))
with open("j.json","w") as f:
    simplejson.dump(x,f,indent=4)
name=input("which you want to buy  ")
items=int(input("how many item you want  ")) 
for keys in x:
    for value in x:
        for i ,k in x[keys].items():
            if i==name:
                t=int(k).items
                print(t)


