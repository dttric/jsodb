# jsodb
Mine database realization that uses .json files.

### How to work with it?
Instalation:
`python3 -m pip install jsodb`

Basic funcs:
```py
import jdb
getkeyval("key") # returns key val
addkey("key"=val) # adds keys to json
changekey("key", val) # changes key to new val
createjson("/path/to/file") # new .json file (without decorator)
addtokey("key", int) # key += int
subfromkey("key", int) # key -= int
@json("/path/to/file") # main decorator
```

To use all that functions you need function with decorator, json file will be: opened, edited, saved.

Basic usage:
```py
@json("profile.json")
def func():
	print(getkeyval(balance)) ### 1
	changekey(balance, 10) ### {balance=10}
	addkey(deposit=100) ### {balance=10, deposit=100}
	print(f"{getkeyval(balance)}\n{getkeyval(deposit)}")
	"""
	10
	100
	"""

func() ### changes applied
```
