asia = {'한국', '중국', '일본'}
asia.add('베트남') # 한국 중국 일본 베트남
asia.add('중국') # 한국 중국 일본 베트남
asia.remove('일본') # 한국 중국 베트남
asia.update({'한국', '홍콩', '태국'}); # 한국 중국 베트남 홍콩 태국
print(asia)