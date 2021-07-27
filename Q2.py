# import simplejson
# python_object={"name":"pranju","class":"I","age":21}
# json_object=simplejson.dumps(python_object)
# print(json_object)



import simplejson
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = simplejson.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"])






# import simplejson
# # a Python object (dict):
# python_obj = {
#   "name": "David",
#   "class":"I",
#   "age": 6  
# }
# print(type(python_obj))
# # convert into JSON:
# j_data =simplejson.dumps(python_obj)

# # result is a JSON string:
# print(j_data)




