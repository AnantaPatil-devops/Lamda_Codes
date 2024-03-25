def get_keys(obj, key):
    keys = key.split('/')
    print(key)
    current_obj = obj
    for ikey in keys:
        if ikey in current_obj:
            current_obj = current_obj[ikey]
        else:
            return None
    return current_obj

object1 = {"a": {"b": {"c": "d"}}}
key1 = "a/b/c"
print(get_keys(object1,key1))
object2 ={"x":{"y":{"z":"a"}}}
key2 = "x/y/z"
print(get_keys(object2,key2))
object3 ={"x":{"y":{"z":"a"}}}
key3 = "x/y/a"
print(get_keys(object3,key3))
