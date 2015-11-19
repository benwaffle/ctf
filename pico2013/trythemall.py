from Crypto.Hash import MD5
import sys

def md5(s):
    h = MD5.new()
    h.update(s + '4092')
    return h.hexdigest()

words = open('/usr/share/dict/cracklib-small').read()

for w in words.split():
    if md5(w) == '27c2f2aac91034c3faf3a2d0f03116d8':
        print w
        sys.exit(0)

