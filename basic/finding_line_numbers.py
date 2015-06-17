f = open("file.txt","r")
contents = f.read().split("\n")
counts = {"Eric":[],"Bryan":[],"Connor":[]}
line_number = 0
for line in contents:
    for name in counts:
        if name in line:
            counts[name].append("foudn on line"+str(line_number))
    line_number+=1
print counts["Eric"][:16]
