import hashlib as hash

# in this case, the rockyou.txt is in the same folder as the script
with open('/usr/share/wordlists/rockyou-utf8.txt', 'r') as file:
    for line in file:
            #word = re.findall('\w+', open('rockyou.txt', encoding='latin-1').read().lower())
            word = hash.md5(line.strip().encode('utf-8')).hexdigest()
            if word[-3:] == "001":
                print(word[-3:])
                print(line)