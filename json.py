import simplejson

def is_complex_num(onject):
    if complex in object:
        return complex(object['real'],object['img'])
    return object
complex_object=simplejson.loads('{"complex":true,"real":4,"img":5}',object_hook=is_complex_num,)
simple_object=simplejson.loads('{"real":4,"img":5}',object_hook=is_complex_num)
print("complex_object",complex_object)
print("simple_object",simple_object)

# import json
# python_object='{"4":"pranju","1":"ankita"}'