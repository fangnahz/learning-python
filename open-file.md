Nobody has given the correct, fully Pythonic way to read a file. It's the following:
```python
with open(...) as f:
    for line in f:
        <do something with line>
```
The `with` statement handles opening and closing the file, 
including if an exception is raised in the inner block. 
The `for line in f` treats the file object `f` as an iterable, 
which automatically uses buffered IO and memory management so you don't have to worry about large files.