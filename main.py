import hashlib

#print(hashlib.algorithms_available)
#print(hashlib.algorithms_guaranteed)


def md5_generator(path):
    with open(path, encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            md5 = hashlib.md5(line.encode('utf-8')).hexdigest()
            yield md5

if __name__ == '__main__':
    for line in md5_generator('temp.txt'):
        print(line)
