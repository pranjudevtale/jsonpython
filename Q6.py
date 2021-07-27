import simplejson
python_obj={'{"a":  1,"a":  2,"a":  3, "a": 4, "b": 1, "b": 2}'}
print("original python object ")
print(python_obj)
json_obj=simplejson.dumps(python_obj)
print("\nUnique key in a Json object:")
print(json_obj)


