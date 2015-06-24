f = open("file.txt","r")
contents = f.read().split("\n")
counts = {"Eric":0,"Bryan":0,"Connor":0}
for line in contents:
    for name in counts:
        if name in line:
            counts[name] += 1
print counts
