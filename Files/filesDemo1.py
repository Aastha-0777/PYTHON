#alway remember to close the file it is not compulsury but not doing will case data leackage
file = open("./Files/demo1.txt", "w")
file.write("Hello This Context Is From Python!!")
file.close()

file2 = open("./Files/demo2.txt", "w")
file2.writelines(["hi", "this", "is", "list"])
file2.close()