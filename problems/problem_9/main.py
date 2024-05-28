def solution(L=1000):
    for m in range(L):
        for n in range(L):
            a = 2*m*n
            b = abs(m**2 - n**2)
            c = m**2 + n**2 
            if a + b + c == L:
                print(a,b,c)
                return a*b*c
