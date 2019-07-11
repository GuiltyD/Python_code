f = open('./day4.py')
for chunk in iter(lambda :f.read(10),''):
        print(chunk)

