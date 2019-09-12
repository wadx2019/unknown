import json
e=input().split(",")
d={}
d["姓名"]=e[0]
d["手机"]=e[1]
d["地址"]=e[2:]
save=json.dumps(d)
print(save)
