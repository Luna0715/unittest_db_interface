#encoding=utf-8
import hashlib

def md5_encrypt(text):
    '''md5加密'''
    md5 = hashlib.md5()
    md5.update(text)
    return md5.hexdigest()

if __name__ == "__main__":
    print md5_encrypt("test")


#098f6bcd4621d373cade4e832627b4f6
#098f6bcd4621d373cade4e832627b4f6