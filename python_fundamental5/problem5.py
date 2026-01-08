try:
    with open("Data.txt","r") as f:
        data=f.read()
        print(data)
except FileNotFoundError:
    print("File not Found!")

    