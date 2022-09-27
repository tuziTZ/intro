s=input("请输入一个字符串：")
a=[s[0]]
cnt=0
for i in range (1,len(s)):


    if s[i]!=s[i-1]:
        a.clear()
    a.append(s[i])
    if cnt<len(a):
        cnt=len(a)
print ("最长的字符串的长度是:",cnt)