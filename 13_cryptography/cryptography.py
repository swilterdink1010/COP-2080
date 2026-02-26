import hashlib
import string
checkWord = 'ca'
lets = string.ascii_lowercase
for l1, l2, l3 in [(l1, l2, l3) for l1 in lets for l2 in lets for l3 in lets]:
    h = hashlib.new('md5', (l1 + l2 + l3).encode("utf-8")).hexdigest()
    if h == "d077f244def8a70e5ea758bd8352fcd8":
        print(f'hash {h} found for string "{l1 + l2 + l3}"')