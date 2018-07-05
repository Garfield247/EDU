import json

# json.loads(): 是将json格式的字符串转化为python对象
json_str = '[{"a":"1","b":"2","c":"3"},{"a":"1","b":"2","c":"3"},{"a":"1","b":"2","c":"3"}]'
print(type(json_str))
py_obj = json.loads(json_str)
print(py_obj)
print(type(py_obj))
# json.dumps(): 将python对象转化为json格式的字符串
py_obj2 = [{'a': '1', 'b': '2', 'c': '3'}, {'a': '1', 'b': '2', 'c': '3'}, {'a': '1', 'b': '2', 'c': '3'}]
print(type(py_obj2))
json_str2 = json.dumps(py_obj2)
print(json_str2)
print(type(json_str2))


# json.dump(): 将python对象写入到文本中
# json_fp = open('json.json','a',encoding='utf-8')
# json.dump(py_obj,json_fp)


# json.load(): 读取json格式的文本，转化为python对象
json_fp2 = open('json.json','r',encoding='utf-8')
py_obj3 = json.load(json_fp2)
print(py_obj3)
print(type(py_obj3))