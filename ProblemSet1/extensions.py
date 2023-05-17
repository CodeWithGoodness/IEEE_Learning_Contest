#prompt the user
fileName = input("File name: ").lower().strip()


if fileName.endswith(".gif"):
    print("image/gif")
elif fileName.endswith(".jpg"):
    print("image/jpg")
elif fileName.endswith("jpeg"):
    print("image/jpeg")
elif fileName.endswith(".png"):
    print("image/png")
elif fileName.endswith(".pdf"):
    print("image/pdf")
elif fileName.endswith(".txt"):
    print("image/txt")
elif fileName.endswith(".zip"):
    print("image/zip")  
else:
    print("application/octet-stream") 

