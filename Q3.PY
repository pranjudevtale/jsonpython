import simplejson
p={
    "q":{
        "name":"pranju",
        "age":21,
        "school name":"Eklavya residential public school ramtek",
        "Qualification":"graduation"
    },
}
with open("que.json","w") as f:
    simplejson.dumps(p,f,indent=4)



