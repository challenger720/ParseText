with open('file.txt', 'r') as f:
    i = 0
    for line in f:
        i += 1
        values = line.strip().split(' ')
        print(f'Line: {i}')
        print(f'Name: {values[0]}')
        print(f'Points: {values[1]}\n')
