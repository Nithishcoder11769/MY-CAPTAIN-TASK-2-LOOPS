S="mississipi"
def repetition(word):
    d=dict()
    for key in word:
        if(key not in d):
            d[key]=1
        else:
            d[key]=d[key]+1
    return d  
R=repetition(S)
sorted_R=sorted(R.items(), key=lambda x:x[1], reverse=True)
print(sorted_R)
