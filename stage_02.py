with open("artifacts.txt" , "r") as f:
    text = f.read()


print(text)
lst = []
for i in text:
    lst.append(i)

