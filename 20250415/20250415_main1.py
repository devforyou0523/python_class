#이중 for문을 이용한 별 출력

# for i in range (7):
#     print("*"*i)

output = ""
for i in range (1,15):
    for j in range (14, i, -1):
        output += " "
    for k in range (0, 2*i-1):
        output += "*"
    output += "\n"

print(output)

