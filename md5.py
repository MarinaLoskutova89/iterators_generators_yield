import hashlib

def MD5_hash(string, encoding='utf-8'):
    md5_hasher = hashlib.md5()
    md5_hasher.update(string.encode(encoding))
    return md5_hasher.hexdigest()

with open('country_link.json') as file:
    for line in file:
        print(MD5_hash(line))