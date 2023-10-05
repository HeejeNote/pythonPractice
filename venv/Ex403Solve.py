String = input("7문자 이상 문자열을 입력하시오 :")
m = (String[0:3]+String[-3:]) # 처음 셋 마지막 셋 합쳐서 출력
print(m)