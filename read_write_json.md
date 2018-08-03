JSON文件有解析要求，需要用双引号，

用`json.dump()`可以确保格式格式正确，可以用`json.loads()'解析。
```python
# Writing JSON data
with open('data.json', 'w') as f:
     json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
     data = json.load(f)
```
`load()` loads JSON from a file or file-like object

`loads()` loads JSON from a given string or unicode object
```python
with open('data.json') as f:
    for l in f:
        data = json.loads(l)
```