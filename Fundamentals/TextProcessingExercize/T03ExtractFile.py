line=input().split("\\")
document=line[3]
title, extension=document.split(".")
print(f"File name: {title}")

print(f"File extension: {extension}")