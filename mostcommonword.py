def most_common_word(d):
    l=[]
    for i in d:
        l.append([i,d[i]])
     
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i][1]<l[j][1]:
                l[i] , l[j] = l[j] , l[i]
        
    common_d={}
    for k in range(20):
        common_d[l[k][0]]=l[k][1]
    return common_d
