a={1:'hello','hi':,445.78,34.56:2+9j}
# acces the valuse from disc
# no indexing in dic
print(a[1],a['hi'],a[445.78])
print(a)
a[1]="am changed"
a['key']='values'
#dics are lifo process
del a['key']
print(a)
# vkupadhyay@digitallynctech.com
inbuilt methods
a.pop('hi')
#a.remove()
a.popitem()
a.update({    })
print(a.keys())
print(a.values())
print(a.items())
a.clear()
print(a)
    #   .fromkeys()
a=[key1,key2,key3]
dic=dict.fromkeys(a,1)
print(dic)






#   dict comprehension



d={a:a**3 for a in range(0,1)}
print(d)





print(len(d))
#print(min(d))
#print(max(d))

