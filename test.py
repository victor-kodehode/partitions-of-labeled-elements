# see: https://oeis.org/A000110
# generates a <list> of ways to partition a <set> of <n> labeled elements
# seq_ is a list of lists
# the outer list is the <list> mentioned above
# the inner lists contain the <set>s mentioned above
# looking at a specific inner list:
#   the first index denotes the number of distinct elements in the <set>
#   the rest of the indices denote the <set> itself

# True: print the ways and how many there are (list & number)
# False: print only how many there are (number)
display_list = False

# the number <n> mentioned above
len_ = 4

# initializing the list
seq_ = [[1,0]]

# generating the list
while(True):
    if(len(seq_[0])-1 >= len_):
        if(display_list):
            for i in range(0,len(seq_)):
                print(seq_[i])
        print(len(seq_))
        break
    temp_ = []
    for i in range(0,len(seq_)):
        for j in range(0,seq_[i][0]+1):
            temp2_ = seq_[i].copy()
            temp2_.append(j)
            if(j >= temp2_[0]):
                temp2_[0] += 1
            temp_.append(temp2_)
    seq_ = temp_.copy()