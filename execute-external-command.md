在python环境下执行外部程序，或者shell命令
```python
import os
os.system("some_command with args")
```
但是这种操作并不会返回shell命令在stdout的输出，返回的是命令执行是否成功。如果需要返回命令执行后的输出结果，
```python
import subprocess
output = subprocess.check_output(["command", "arg1", "arg2", ...])
```
