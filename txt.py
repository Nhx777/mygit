with open('jihua.txt',encoding='utf-8') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('jihua.txt', 'w',encoding='utf-8') as file_object:
    file_object.write("i love you")
    contents = file_object.read()
print(contents)
