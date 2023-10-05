a = 100 # 0110 0100 64+32+4=100
result = 0
for i in range(1,3): # 1~2
    result = a >> i # 0001 1001   16+8+1=25
    result = result + 1 # 25 + 1
print(result) # 26