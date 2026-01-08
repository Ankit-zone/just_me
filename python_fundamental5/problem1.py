name=5
i=0
with open("names.txt","r") as f:
    # while(i<name):
    #     f.writelines(input("Enter names:"))
    #     f.write("\n")
    #     i+=1
    names=f.read()
    print(names)
