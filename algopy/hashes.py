from hashlib import sha1, md5


def hash_f(element, i, lenght):
    """Função para criar varias funções de hash"""
    h1 = int(md5(element.encode('ascii')).hexdigest(), 16)
    h2 = int(sha1(element.encode('ascii')).hexdigest(), 16)
    return (h1 + i * h2) % lenght

print(hash_f("1", 1, 10 ** 5))
print(hash_f("1", 2, 10 ** 5))
