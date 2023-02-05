import os

old_name = "sampleEx9.11"
new_name = "Ex9.11"
with open(old_name)as f:
    content = f.read()

with open(new_name, 'w')as f:
    f.write(content)

os.remove(old_name)
