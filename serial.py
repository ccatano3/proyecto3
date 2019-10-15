def hamming_distance(string1, string2):
    distance = 0
    for i,j in zip(string1,string2):
        if i != j:
            distance += 1
    return distance

def hamming_distance_reduced(s1, s2):
    return sum(ch1 != ch2 for ch1,ch2 in zip(s1,s2))

if __name__ == "__main__":
    inp = open('in','r')
    sett=['','']
    i=0
    for each in inp.readlines():
        each=each.replace('\n','')
        if each=='sequence1':
            i=0
        if each=='sequence2':
            i=1
       
        sett[i]=sett[i]+each

    print(hamming_distance(sett[0],sett[1]))
