import json as jsonlib

def changekey(key, val):
	data[f'{key}'] = val

def getkeyval(key):
	return data[f'{key}']

def addkey(**kwargs):
	for key, val in kwargs.items():
		data[f'{key}'] = val

def createjson(filepath):
	with open(f"{filepath}.json", "w") as f:
		f.write("{}")

def addtokey(key, val):
	try:
		data[f'{key}'] += int(val)
	except TypeError:
		print("TypeError! Only use int.")

def subfromkey(key, val):
	try:
		data[f'{key}'] -= int(val)
	except TypeError:
		print("TypeError! Only use int.")

def addmultikey(multikey, **values):
	def multikey_func(**kwargs):
		return values
	data[f'{multikey}'] = multikey_func(**values)


def json(file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file) as f:
                data = jsonlib.load(f)
            func(*args, **kwargs)
            with open(file, "w") as f:
                jsonlib.dump(data, f)
        return wrapper
    return decorator