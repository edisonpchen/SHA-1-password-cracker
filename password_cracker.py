import hashlib

def crack_sha1_hash(hash, use_salts = False):
    pass_file = open('top-10000-passwords.txt', 'r')
    pass_list = pass_file.readlines()
    pass_file.close()
    pass_list = [s.replace('\n', '') for s in pass_list]
    if not use_salts:
        for i in range(len(pass_list)):
            password = pass_list[i]
            digest = hashlib.sha1(password.encode()).hexdigest()
            if digest == hash:
                return password
        return 'PASSWORD NOT IN DATABASE'
    else:
        salt_file = open('known-salts.txt', 'r')
        salt_list = salt_file.readlines()
        salt_list = [s.replace('\n', '') for s in salt_list]
        for i in range(len(salt_list)):
            salt = salt_list[i]
            for j in range(len(pass_list)):
                password = pass_list[j]
                digest1 = hashlib.sha1((password + salt).encode()).hexdigest()
                digest2 = hashlib.sha1((salt + password + salt).encode()).hexdigest()
                digest3 = hashlib.sha1((salt + password).encode()).hexdigest()
                if digest1 == hash or digest2 == hash or digest3 == hash:
                    return password
        return 'PASSWORD NOT IN DATABASE'