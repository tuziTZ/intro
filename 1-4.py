import re
s=input("请输入一个字符串：")
s1=re.sub(pattern=" ",repl="",string=s)
print(s1)