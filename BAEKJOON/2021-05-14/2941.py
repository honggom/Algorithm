data = input()
ds = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
newD = ""
while True:
    for s in ds:
        newD = data.replace(s, '', 1)
        if newD != data:
            data = newD
            count += 1
    if newD == data:
        if data != '':
            count += len(data)
        print(count)
        break
