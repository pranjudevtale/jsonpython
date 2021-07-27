import simplejson
json_object='{"Name":"Ram", "Class":"IV", "Age":9 }'
python_object=simplejson.loads(json_object)
print(python_object)

# import simplejson
 
# # {key:value mapping}
# a ={"name":"John",
#    "age":31,
#     "Salary":25000}
 
# with open("data.json","w") as f:
#     simplejson.dump(a,f,indent=3)