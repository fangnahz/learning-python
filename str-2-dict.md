```python
import json
data=[]
with open('tmp.log') as f:
    for line in f:
        data.append(json.loads(line))
```

```
>>> type(data)
<type 'list'>
>>> len(data)
61
>>> type(data[0])
<type 'dict'>
>>> data[0].keys()
[u'url', u'reaseon']
```

```python
with open('tmp.out', 'w') as f:
    for d in data:
        f.write('\''+d['url']+'\',\n')

```