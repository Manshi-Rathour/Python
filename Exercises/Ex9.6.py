with open('Ex9.6', 'r')as f:
    content = f.read()

if 'python' in content.lower():
    print("Python is present in log file")
else:
    print("Python is not present")
