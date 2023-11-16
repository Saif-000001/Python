#A
"""
t = int(input())
while t>0 :
    i = int(input())
    str = input()
    print(str[len(str)-1])
    t = t - 1
"""

#B
"""
t = int(input())
while t>0 :
    n = int(input())
    a = [int(i)for i in input().split()]
    # print(*a)
    mp = {}
    for i in range(n):
        mp[a[i]] = mp.get(a[i],0)+1
    # for key,value in mp.items():
    #     print(f"{key}: {value}")
    add = []
    for key, value in mp.items():
        if(value>=2):
            add.append(key)
    if(len(add)<2):
        print(-1)
    else :
        ans = []
        f1, f2 = False, False
        for i in a:
            if i == add[0]:
                if f1:
                    ans.append(2)
                    f1 = True
                else :
                    ans.append(1)
                    f1 = True
            elif i == add[1]:
                if f2:
                    ans.append(3)
                    f2 = True
                else :
                    ans.append(1)
                    f2 = True
            else : 
                ans.append(1)
        
        print(*ans)  
    t-=1
"""

"""
def fn():
    n =int(input())
    a = [int(i) for i in input().split()]
    if n == 1:
        print(-1,"\n")
        return
    if n==2:
        x , y = a[0], a[1]
        if(x==y):
            print(-1)
            return
        else :
            print(1)
            print(1)
            return
    mx = 0
    cnt = 0
    for i in a:
        if i < a[mx] :
            mx = cnt
        cnt+=1
    print(1)
    print(mx+1)
fn()
"""

# Sonya_and_Hotels
"""
n, m = input().split()
a = [int(i)for i in input().split()]
d = int(m)
d+=d
ans = 2
for i in range(0,int(n)-1):
    if a[i+1]-a[i]==d:
        ans+=1
    elif a[i+1]-a[i]>d:
        ans+=2
print(ans)
"""

# Stages

"""
n, m = map(int, input().split())
s = input().strip()

s = ''.join(sorted(s))

ch = ord('a')-2
ans = 0
l = 0
f = False
for i in range(n):
    if ord(s[i]) >= ch+2:
        ch = ord(s[i])
        ans += ord(s[i])-ord('a')+1
        l+=1
        if l>=m:
            f = True
            break
if f:
    print(ans)
else :
    print(-1)
"""

# Piles With Stones

"""
n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

f ,l= 0, 0

for i in a:
    f+=i
for i in b:
    l+=i

if f >= l:
    print("YES")
else :
    print("NO")
"""