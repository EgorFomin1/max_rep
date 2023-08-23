rs = input('введите слово:')
def pal():
    return rs == rs[::-1]
if rs == rs[::-1]:
    print('True')
else:
    print('False')

