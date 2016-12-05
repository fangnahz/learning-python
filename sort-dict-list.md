对dict的列表按照某个key的值排序。
```python
s="{'status': 'ok', 'running': [], 'finished': [{'spider': 'weibo', 'start_time': '2016-11-26 22:23:51.362071', 'end_time': '2016-11-27 07:24:55.670725', 'id': 'f20cd858b3e311e6b88100163e0c9a77'}, {'spider': 'baidulaw', 'start_time': '2016-11-28 13:29:41.362183', 'end_time': '2016-11-28 13:29:48.500329', 'id': 'a97171fab52b11e6b88100163e0c9a77'}, {'spider': 'amazon', 'start_time': '2016-11-28 14:17:36.362261', 'end_time': '2016-11-29 23:17:47.856086', 'id': '59fcafacb53211e6b88100163e0c9a77'}, {'spider': 'amazonus', 'start_time': '2016-12-01 00:32:36.361515', 'end_time': '2016-12-02 09:32:49.661597', 'id': '99f68a9eb71a11e6b88100163e0c9a77'}, {'spider': 'taobao', 'start_time': '2016-12-01 17:51:21.364209', 'end_time': '2016-12-02 11:33:05.401073', 'id': 'b6adef2eb7ab11e6b88100163e0c9a77'}], 'pending': [], 'node_name': 'iZ230xu977wZ'}"
import ast
status = ast.literal_eval(s)
```
`status['finished']`是dict列表，每一个列表元素对应一个spider执行情况的描述。
按照`key='spider'`对这个列表排序后print到stdout，
```python
print('Finished spiders:')
from operator import itemgetter
status['finished'].sort(key=itemgetter('spider'))
for f_spiders in status['finished']:
    print(f_spiders['spider']+': '+f_spiders['id'])
```
输出是
```
Finished spiders:
amazon: 59fcafacb53211e6b88100163e0c9a77
amazonus: 99f68a9eb71a11e6b88100163e0c9a77
baidulaw: a97171fab52b11e6b88100163e0c9a77
taobao: b6adef2eb7ab11e6b88100163e0c9a77
weibo: f20cd858b3e311e6b88100163e0c9a77
```