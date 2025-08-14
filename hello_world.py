from sys import argv 
def hello(name):
    x = f"hello {name}!"
    return x
print(hello(argv[1]))
