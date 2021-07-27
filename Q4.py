import simplejson
j_str={
    "4":5,
    "6":7,
    "1":3,
    "2":4
}
print("Orignal String")
print("j_str")
print("JSON data:")
simplejson.dumps(j_str,sort_key=True,indent=4)
