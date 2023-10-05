lol = [[1,2,3], [4,5], [6,7,8,9]]
print(lol[0]) # [1,2,3]
print(lol[2][1]) # 7
for sub in lol: # lol[0], lol[1], lol[2]
    for item in sub: # lol[0] -> 1 2 3  lol[1] -> 4 5 lol[2] -> 6 7 8 9
        print(item, end=' ')
    print() # 각 서브리스트 줄바꿈
