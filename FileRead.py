import os
if os.path.exists("practice.txt"):
    with open("practice.txt","r") as file:
        content= file.read()
        print(content)
else:
    print("File Doesn't exist")
