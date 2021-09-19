import hashlib

def MD5_hash(path):
    with open(path) as file:
        for line in file:
            md5_hasher = hashlib.md5()
            md5_hasher.update(line.encode(encoding='utf-8'))
            yield md5_hasher.hexdigest()

for lines in MD5_hash('country_link.json'):
    print(lines)


