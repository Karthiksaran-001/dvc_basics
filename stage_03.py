with open("artifacts.txt" , "r") as f:
    text = f.read()


with open("artifacts_1.txt" , "w") as f:
    text = f.write(text + "Added in 2 File")