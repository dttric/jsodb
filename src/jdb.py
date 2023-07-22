import json

def changekey(key, val):
	data[f'{key}'] = val

def getkeyval(key):
	return data[f'{key}']

def addkey(**kwargs):
	for key, val in kwargs.items():
		data[f'{key}'] = val

def createjson(filepath):
	with open(f"{filepath}.json", "w") as f:
		file.write("{}")

def json(func, file):
    def wrapper(*args, **kwargs):
		with open(f'{file}') as f:
			data = json.load(f)
        func(*args, **kwargs)
        with open(f'{file}', "w") as f:
			json.dump(data, f)
    return wrapper