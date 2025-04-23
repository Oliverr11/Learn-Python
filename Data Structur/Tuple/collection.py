print("===========Tuple===========") #Tuple is immutable

data = ("Sengkim",18,False)
print(data[0]) #Sengkim

print(data[-1]) #false

#unpacking
name,age,Single=data
print(f"Name : {name}\nAge : {age}\nSingle : {Single}")


#slicing
print(data[0:2])
print(data[2:])

#data[0] = "Kim" #not working, tuple doesn't support assignt new value


print("===========List===========") # Li st is muttable
data = []   
print(type(data))

names = ["virak","chetra","somnang","pheakdey"]

print(names)
#access index
print(names[0])
#modify item
names[0]="Nita"
print(names[0])
for name in names:
    print(name)

names.append("kim")

print("\n-unpacking:")
n1,n2,n3,n4,n5=names
print(f"N1 : {n1}, N2 : {n2}, N3 : {n3}, N4 : {n4}, N5 : {n5}\n")


names.remove("kim")

n1,*other=names
print(f"N1 : {n1}, other : {other}")
