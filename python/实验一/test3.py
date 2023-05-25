s = {"AAA": "男",
     "BBB": "女",
     "CCC": "女",
     "DDD": "男",
     "EEE": "男",
     "FFF": "女"}
snew = {}
k = s.keys()
for i in k:
    if s[i] == "女":
        snew[i] = '女'
print(f"删除前：{s}")
print(f"删除后：{snew}")
