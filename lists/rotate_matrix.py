import copy

def rotate_90_deg_slow(matrix):
    rotated_matrix = copy.deepcopy(matrix)
    n = len(matrix)
    
    for i in range(n):
        for j in range(n):
            rotated_matrix[i][j] = matrix[n-j-1][i]
            
    print(rotated_matrix)
    print(matrix)
    

def rotate_90_fast(matrix):
    
    for row in matrix:
        pass
        

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(list(zip(*matrix[::-1])))
rotate_90_deg_slow(matrix)