a = {'apple', 'lemon', 'banana'}
a.update( {'kiwi', 'banana'}) # apple lemon banana kiwi
# print(a)
a.remove('lemon') # apple banana kiwi
# print(a)
a.add('apple') # apple banana kiwi
# print(a)
for i in a:
    print(i)
    # apple
    # banana
    # kiwi