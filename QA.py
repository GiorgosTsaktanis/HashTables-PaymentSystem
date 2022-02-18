def max_cost(Hash_table):
    max=-1
    for i in range(0,len(Hash_table)):
        sum=0
        if(Hash_table[i]!=None):
            for p in range(0,len(Hash_table[i])):
                sum=sum+Hash_table[i][p][1]
                if sum>max:
                    max=sum
                    key=Hash_table[i][p][0]

    return key

def max_freq_card(Hash_table):
    max=0
    for i in range (0,len(Hash_table)):
        if (Hash_table[i] != None):
            if len(Hash_table[i])>max:
                max=len(Hash_table[i])
                key=Hash_table[i][0][0]
    return key

def max_frec_day(Hash_table):
    counters=[0]*6
    dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'friday', 'Suturday']
    for i in range (len(Hash_table)):
        if(Hash_table[i]!=None):
            for p in range(0,len(Hash_table[i])):
                if(Hash_table[i][p][2]=='Monday'):
                    counters[0]=counters[0]+1
                if (Hash_table[i][p][2] == 'Tuesday'):
                    counters[1]=counters[1]+1
                if (Hash_table[i][p][2] == 'wednesday'):
                    counters[2]=counters[2]+ 1
                if (Hash_table[i][p][2] == 'Thursday'):
                    counters[3]=counters[3]+1
                if (Hash_table[i][p][2] == 'Friday'):
                    counters[4]=counters[4]+1
                if (Hash_table[i][p][2] == 'Saturday'):
                    counters[5]=counters[5]+1
    max=0
    for k in range(0,len(counters)):
        if counters[k]>max:
            max=counters[k]
            day=dayList[k]
    return day,max
