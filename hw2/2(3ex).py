s = input()
s0 = s
h = len(s) // 2

ar1 = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
ar2 = ['E', 'J', 'S', 'Z']
ar3 = ['3', 'L', '2', '5']
f = True
f1 = False
for i in range(len(s)):
    if s[i] not in ar1 and s[i] not in ar2 and s[i] not in ar3:
        f = False
        break
    if s[i] in ar2:
        s = s[:i] + ar3[ar2.index(s[i])] + s[i+1:]
        f1 = True
s1 = s[:h]
s2 = s[-1:-h-1:-1]

if f:
    if s1 == s2 and f1:
        print(s0, "is a mirrored string.")
    elif s1 == s2 and not f1:
        print(s0, "is a mirrored palindrome.")
    else:
        print(s0, "is not a palindrome.")
else:
    s1 = s0[:h]
    s2 = s0[-1:-h - 1:-1]
    if s1 == s2:
        print(s0, "is a regular palindrome")
    else:
        print(s0, "is not a palindrome.")

