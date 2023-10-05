x = input('입력 :') # 입력값 xyz321
a = [ 'abc123', 'def456', 'ghi789' ]
a.append(x)
a.remove('def456') # [ 'abc123', 'ghi789', 'xyz321' ]
print(a[1][-3:], a[2][:-3], sep =',') # -3: 뒤에서 세번째부터 끝까지  sep : print 함수 결과값들을 지정한 값으로 구분
# 789,
for i in range(3, 6): # 3 ~ 5
    print(i, end = ' ') # end : 반복 출력된 값들 공백으로 출력