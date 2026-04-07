import random as r

def create_matrix():
    m = r.randint(2, 8)
    n = r.randint(2, 10-m)
    print(n,m)
    d_matr = []
    for i in range(m):
        row = [r.randint(-100, 101) for j in range(n)]
        d_matr.append(row)
    for row in d_matr:
        print(row)
    return m, n, d_matr

def checker(m, n, c_matr):
    ch = []
    for i in range(m):
        if sum(c_matr[i]) > 0:
            ch.append(True)
        else:
            ch.append(False)
            
    for j in range(n):
        col = [c_matr[i_][j] for i_ in range(m)]
        if sum(col) > 0:
            ch.append(True)
        else:
            ch.append(False)
    
    if all(ch):
        return True
    
    return False

def changer(c_matr, i, j, isw, jsw):
    ch_matr = [row[:] for row in c_matr]
    if i == j == -1:
        return ch_matr
    if isw == 1:
        ch_matr[i] = list(map(lambda x: -x, ch_matr[i]))
        
    if jsw == 1:
        for i_ in range(len(ch_matr)):
            ch_matr[i_][j]*=-1        
    return ch_matr
            

        
def searcher(m, n, matr, i, j, c):
    if checker(m, n, matr) and c>1:
        print("Решение:")
        for row in matr:
            print(row)
        return True
    
    if i>=m and j>=n:
        return False
   
    if i == m:
        i_ = i
        j_ = j+1
    elif j == n:
        i_ = i+1
        j_ = j
    else:
        i_ = i+1
        j_ = j+1 
    
    row_vars = [0,1] if i<m else [0]
    col_vars = [0,1] if j<n else [0]
    for isw in row_vars:
        for jsw in col_vars:
            c = c+isw+jsw
            n_matr = changer(matr, i%m, j%n, isw, jsw)
            
            if searcher(m, n, n_matr, i_, j_, c):
                return True
    return False
           

ni = int(input("Введите число матриц: "))

for _ in range(ni):
    m, n, d_matr = create_matrix()
    res = searcher(m, n, d_matr, 0, 0, 0)
    print(res)
    if not res:
        break
    
    
    print()
    