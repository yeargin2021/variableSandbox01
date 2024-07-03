import os

os.mkdir("temp")
os.chdir("temp")

for i in range(1, 4):
    with open(f"fileNumber0{i}", "w") as file:
        pass


"""
Result:

temp
├── fileNumber01
├── fileNumber02
└── fileNumber03

1 directory, 3 files
"""