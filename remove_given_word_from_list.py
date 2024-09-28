# Wap to remove  a given word from a list and stript it at the same 


def rem(l,word):
    q=[]
    for item in l:
        if not(item==word):
            q.append(item.strip(word))   
    return q

l=["Shashi","Rohan","Rishi"]
print(rem(l,"hi"))