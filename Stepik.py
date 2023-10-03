def is_pangram(s):
    s = set(s.lower())
    s.discard(' ')
    s.discard('.')
    s.discard(',')
    s.discard('!')
    print(sorted(s))
    if s == set('abcdefghijklmnopqrstuvwxyz'):
        return True
    else:
        return False
is_pangram('The quick, brown fox jumps over the lazy dog!')