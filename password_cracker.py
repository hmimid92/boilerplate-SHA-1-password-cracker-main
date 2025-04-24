import hashlib

def crack_sha1_hash(hash, use_salts = False):
    returnFunction = ''
    if use_salts:
        with open('top-10000-passwords.txt') as fp:
            for entry in fp:
                ent = f'{entry.rstrip()}'
                with open('known-salts.txt') as salt:
                    for salti in salt:
                        entNew = f'{salti.rstrip()}' + ent + f'{salti.rstrip()}'
                        resultSalt = sign(entNew.encode('utf-8'))
                        if resultSalt == hash:
                           returnFunction = entry
                           fp.close()
                           salt.close()
                           return returnFunction.replace('\n', '')
    else:
        with open('top-10000-passwords.txt') as fp:
            for entry in fp:
                ent = f'{entry.rstrip()}'
                result = sign(ent.encode('utf-8'))
                if result == hash:
                    returnFunction = entry
                    fp.close()
                    return returnFunction.replace('\n', '')
    return "PASSWORD NOT IN DATABASE"
    pass

def sign(passWord):
    hash_object = hashlib.sha1(passWord)
    pbHash = hash_object.hexdigest()
    return pbHash
