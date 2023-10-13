f = open("test.txt", 'r')
print("readline() method")
print(f.readline())
print(f.readline())
f.close()

f = open("test.txt", 'r')
print("readlines() method")
lines = f.readlines()
for line in lines:
    print(line.strip())
f.close()


f = open("test.txt", 'r')
print("read() method")
data = f.read()
print(data)
f.close()