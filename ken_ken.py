class KenGame():
    def __init__(self, f_size):
        self.f_size = f_size
        self.full_node = []
        self.field = []
        
    def create_field(self):
        self.field = [[0]*self.f_size for row in range(self.f_size)]
        
    def to_matr(self, condition):
        cond_matr = condition.split("\n")
        cond_matr = [row.split(" = ") for row in cond_matr]
        for row in cond_matr:
            row[0] = row[0].split("; ")
            for i in range(len(row[0])):
                row[0][i] = row[0][i].split(",")
                row[0][i][0] = int(row[0][i][0])
                row[0][i][1] = int(row[0][i][1])
        self.cond_matr = cond_matr
        
    def freebies(self):
        for cond in self.cond_matr:
            if len(cond[0]) == 1:
                i, j = cond[0][0]
                self.field[i-1][j-1] = int(cond[-1][0])
        
    def check_cage(self, cond, i, j):
        cells = cond[0]
        target = cond[1]
        if [i, j] not in cells:
            return True
        if len(cells) == 1:
            i, j = cells[0]
            if self.field[i-1][j-1] == int(target):
                return True
        
        op = target[-1]
        tval = int(target[:-1])
        
        nums =[self.field[i-1][j-1] for (i, j) in cells]    
        
        if 0 in nums:
            return True
        
        if op == "+":
            if sum(nums) == tval:
                return True
        
        if op == "*":
            prod = 1
            for n in nums:
                prod*=n
            if prod == tval:
                return True
        
        if op == "-":
            if abs(nums[0]-nums[1]) == tval:
                return True
        
        if op == "/":
            if (nums[0]/nums[1] == tval) or (nums[1]/nums[0] == tval):
                return True
            
        return False
    
    
    
    def mapper(self, i, j):
        if i == self.f_size:
            c_field = [row[:] for row in self.field]
            self.full_node.append(c_field)
            return   
                    
        ni = i + (j+1)//self.f_size
        nj = (j+1)%self.f_size
        
        checker = []
        for cond in self.cond_matr:
            state = self.check_cage(cond, i, j)
            checker.append(state)
        
        if not all(checker):
            return
        
        if self.field[i][j] != 0:
            self.mapper(ni, nj)
            return
            
        node_hor = set(self.field[i])
        node_vert = set(self.field[i0][j] for i0 in range(self.f_size))
        
        for cand in range(1, self.f_size+1):
            if (cand not in node_hor) and (cand not in node_vert):
                self.field[i][j] = cand
                self.mapper(ni, nj)
                self.field[i][j] = 0
                
    
        
cond = """1,1; 1,2 = 1-
1,3; 1,4 = 2/
1,5; 2,5 = 1-
2,1; 3,1 = 3-
2,2; 3,2 = 2-
2,3; 3,3 = 6+
2,4; 3,4 = 1-
3,5 = 2
4,1; 5,1 = 3-
4,2; 5,2 = 1-
4,3; 5,3 = 12*
4,4; 4,5 = 5+
5,4; 5,5 = 2-"""

cond_matr = [
    [[[1,1], [1,2]], ["4-"]],
    [[[2,1], [3,1]], ["2-"]],
    [[[4,1], [5,1], [5,2]], ["32*"]],
    [[[2,2], [3,2], [3,3]], ["6*"]],
    [[[4,2], [4,3]], ["2/"]],
    [[[1,3], [2,3], [2,4]], ["8+"]],
    [[[5,3], [5,4]], ["2-"]],
    [[[1,4], [1,5]], ["2-"]],
    [[[3,4]], ["2"]],
    [[[2,5], [3,5]], ["1-"]],
    [[[4,4], [4,5], [5,5]], ["9+"]]
]




kg = KenGame(5)

kg.create_field()
kg.to_matr(cond)
kg.freebies()

kg.mapper(0,0)



for f in kg.full_node:
    for row in f:
        print(row)
    print()
