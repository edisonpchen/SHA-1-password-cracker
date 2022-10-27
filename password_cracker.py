import hashlib

def crack_sha1_hash(hash, use_salts = False):
    pass_file = open('top-10000-passwords.txt', 'r')
    pass_list = pass_file.readlines()
    pass_file.close()
    pass_list = [s.replace('\n', '') for s in pass_list]
    