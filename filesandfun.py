data = "Hello everyone!\nHow are you?"
multi = ["Line 1","Line 2","Line 3"]

f1 = open("test2.txt","w")
for eachline in multi:
    f1.writelines(eachline+"\n")
f1.close()

file = open("test.txt","w") #w or write mode will replace the entire file
file.write(data)
file.close()

file = open("test.txt","a") #a or append mode adds to the 
file.write(data)
file.close()

file = open("test.txt","r") #r or read mode reads data from the file.
#filedata = file.read()
a = "1"
while a != "":
    a = file.readline()
    print("The first line of the file is:",a)
file.close()

m2 = []
f2 = open("test2.txt","r")
for line in f2:
    m2.append(line.rstrip("\n"))
print(m2)
f2.close()

s = "This,that,something"
for x in s.split(","):
    print(x)



