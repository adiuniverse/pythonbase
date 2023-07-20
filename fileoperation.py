try:
    f = open('sample.txt', 'r')
    a = f.read(print)
    print(a)
except FileNotFoundError :
    print('file does not exist')    