a = 'ABCDHFHGFHDGDG'
b = 'ASFDBVCDGHDHGFH'

def lcs(a, b):
    n = len(a)
    m = len(b)
    mean_len = (m+n)/2
    l = [[0] * (m+1) for i in range(n+1)]
    for i in range(n+1)[1:]:
        for j in range(m+1)[1:]:
            if a[i-1] == b[j-1]:
                l[i][j] = l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])
    return l[-1][-1]/mean_len   # 取末行末列的值取平均

l = lcs(a=a, b=b)
print(l)