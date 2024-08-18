def read(file):
    with open(file, 'r') as f:
        return f.readlines()
    
def write(file, data):
    with open(file, 'w') as f:
        return f.write(data)
    
def append(file, data):
    with open(file, 'a') as f:
        return f.append(data)