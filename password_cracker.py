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
