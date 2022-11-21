mydata = ["Pedro 7\n" "Egern 1\n" "Fine 2\n"]
myfile = "data/bttx.txt"

with open(myfile, "w") as file:
    file.writelines(mydata)

with open(myfile) as file:
    lines = file.readlines()
line_number = 0
for line in lines:
    line_number += 1
    print(f"Line {line_number}: {line.strip()}")
print()

line_number = 0
with open(myfile) as file:
    for line in file:
        line_number += 1
        print(f"line {line_number}: {line.strip()}")
    print()