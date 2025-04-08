D1={"Ravi":75,"Krishna":76,"Rahul":72,"Divyanka":74}
name=input("Enter the students name:")
if name in D1:
    print(name + "'s marks:" + str(D1[name]))
else:
    print(name+" not found ")