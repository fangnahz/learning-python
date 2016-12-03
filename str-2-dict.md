```
>>> subprocess.check_output(["curl", "http://localhost:6800/listjobs.json?project=default"])
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   946  100   946    0     0   131k      0 --:--:-- --:--:-- --:--:--  153k
'{"status": "ok", 
"running": [{"start_time": "2016-12-01 17:51:56.397268", "id": "cb595792b7ab11e683a400163e0cb504", "spider": "baidulaw"}], 
"finished": [{"start_time": "2016-12-01 17:14:16.398496", "end_time": "2016-12-01 17:30:21.958770", "id": "87662b8cb7a611e683a400163e0cb504", "spider": "weibo"}, {"start_time": "2016-12-01 16:17:46.397379", "end_time": "2016-12-01 17:43:59.304593", "id": "a261b18eb79e11e683a400163e0cb504", "spider": "baidulaw"}, {"start_time": "2016-12-01 17:43:31.398462", "end_time": "2016-12-01 17:45:55.355636", "id": "9bd58aa0b7aa11e683a400163e0cb504", "spider": "weibo"}, {"start_time": "2016-12-01 17:45:46.399098", "end_time": "2016-12-01 17:45:57.070236", "id": "ee29d176b7aa11e683a400163e0cb504", "spider": "weibo"}, {"start_time": "2016-12-01 17:46:31.398139", "end_time": "2016-12-03 00:32:53.614042", "id": "09c8e188b7ab11e683a400163e0cb504", "spider": "weibo"}], 
"pending": [], 
"node_name": "iZ23zlxjhclZ"}\n'
>>> import ast
# check_output的返回值是字符串string，满足转换成dict的格式要求。
>>> status = ast.literal_eval(subprocess.check_output(["curl", "http://localhost:6800/listjobs.json?project=default"]))
>>> type(status)
<type 'dict'>
>>> status.keys()
[u'status', u'running', u'finished', u'pending', u'node_name']
>>> type(status['running'])
# 这个dict有五个keys，每个对应的值都是一个列表，列表的元素都是dict
<type 'list'>
>>> len(status['running'])
1
>>> type(status['running'][0])
<type 'dict'>
>>> status['running'][0].keys()
[u'start_time', u'id', u'spider']
>>> status['running'][0]['spider']
u'baidulaw'
>>> status['running'][0]['id']
u'cb595792b7ab11e683a400163e0cb504'
```
