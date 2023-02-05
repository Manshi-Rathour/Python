story = "Once upon a time there was a youtuber named Harry who uploaded python course with notes"
print(len(story))
print(story.endswith("notes"))    # True
print(story.count('c'))
print(story.replace("Harry", "Code with Harry"))

# Slicing
name = "Manshi"
print(name[0:3])  # Man
print(name[2:5])  # nsh
print(name[:5])   # Mansh
print(name[4:])   # hi
print(name[0:4:2])  # Mn