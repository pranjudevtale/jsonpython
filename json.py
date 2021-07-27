# import simplejson
# json_obj='{"name":"pranju","class":"I","age":21,"s":8}'
# python_obj=simplejson.loads(json_obj)
# print("json data:")
# print(python_obj)
# print("name:",python_obj["s"])
# print("class:",python_obj["class"])
# print("age:",python_obj["age"])


import simplejson
x='{"name":"pranju","class":"I","age":21,"s":8}'
y=simplejson.loads(x)
print(y["name"])
print(y["age"])



