import random
import string
random.seed(1059343)


# encoding: utf-8
def hash_djb2(s):
    hash = 5381
    for x in s:
        hash = ((hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF


def Key_creation():
    s = random.randint(1000000000000000,9999999999999999)
    s=list(str(s))
    array=['X','Y','Z','W']
    p=3
    for position in random.sample(range(15), 4):
        i=random.randint(0,p)
        s[position] = random.choice(array[i])
        array.remove(array[i])
        p=p-1
    s="".join(s)
    return s



def primeGreaterThan2(num):
    while True:
        if num % 2 == 1:
            isPrime = True
            for x in range(3, int(num ** 0.5), 2):
                if num % x == 0:
                    isPrime = False
                    break
            if isPrime:
                return num
        num = num + 1
    return num


def create_hash(N):
    Htable = [None] * N
    return Htable


def rehash(N, array):
    new_N = primeGreaterThan2(N * 2)
    Htable = create_hash(new_N)

    for i in range(0, N):
        if array[i] != None:
            slot = hash_djb2(array[i][0][0]) % new_N
            Htable[slot] = array[i]
    return Htable


def collision(key, N, Hash_table):
    i = 0
    slot = (hash_djb2(key) + i * i) % N
    while (Hash_table[slot] != None):
        slot = (hash_djb2(key) + i * i) % N
        i = i + 1
    return slot

def question5(N, array):
    #new_N = primeGreaterThan2(N * 2)
    Htable = create_hash(N*2)
    # Htable , new_N = create_hash(new_N)
    for i in range(0, N):
        if array[i] != None:
            slot = hash_djb2(array[i][0][0]) %(N*2)
            Htable[slot] = array[i]
    return Htable