```python
#argecho.py
import sys

for arg in sys.argv:
    print arg
```
```
$ python argecho.py
argecho.py
$ python argecho.py abc def
argecho.py
abc
def
$ python argecho.py --help
argecho.py
--help
$ python argecho.py -m kant.xml
argecho.py
-m
kant.xml
```
`sys.argv[0]`: python script文件名

`sys.argv[1:]`: 命令行中python脚本名称后的其他参数列表
