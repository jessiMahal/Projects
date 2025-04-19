file = open('file.txt','r')
content = file.read()
file.close()
print(f"content of 'file.txt': {content}")