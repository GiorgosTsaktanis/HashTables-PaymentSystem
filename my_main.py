import random
from my_imports import *
import time
from QA import *


def main(Repetition):
    counter = 1
    N = primeGreaterThan2(1000)
    #N=1000 for the question 5
    Hash_table = create_hash(N)
    entries = 0
    LF_DEFINED = 0.5
    colision_counter = 0
    dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'friday', 'Suturday']
    for p in range(0, Repetition):

        key = Key_creation()
        money = random.randint(10, 100)
        r = random.randint(0, 5)
        day = dayList[r]

        slot = hash_djb2(key) % N
        customer = [key, money, day]
        if (Hash_table[slot]) == None:
            Hash_table[slot] = [customer]
            entries = entries + 1
        else:
            if key == Hash_table[slot][0]:
                Hash_table[slot].append(customer)
            else:
                entries = entries + 1
                slot = collision(key, N, Hash_table)
                colision_counter = colision_counter + 1

                Hash_table[slot] = [customer]

        if ((entries / N) > LF_DEFINED):
            Hash_table = rehash(N, Hash_table)
            N = len(Hash_table)

    #print(counter)
    print(colision_counter)
    return Hash_table


print("the number of collisions with a load factor=0.5 is :")
HT = main(1000000)
print(HT)
#print("the card which has the maximum money spent is:")
#key=max_cost(HT)
#print(key)
#==========================================================>
#print("the card which has been used the most times  is:")
#key=max_freq_card(HT)
#print(key)
#==========================================================>
#print("the day that the shop haw been visited most times is :")
#day,max=max_frec_day(HT)
#print(day,max)

