from typing import List

def get_matrix_as_spiral(matrix: List[List[int]]) -> List[int]:
    if matrix is None:
        return None
    if len(matrix) == 0:
        return []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    size = len(matrix) * len(matrix[0])
    
    spiral_elems = []
    while len(spiral_elems) < size:
        # print the top row
        itr = left
        while itr <= right and len(spiral_elems)  < size:
            spiral_elems.append(matrix[top][itr])
            itr += 1
            
        top += 1
        itr = top
        while itr <= bottom and len(spiral_elems) < size:
            spiral_elems.append(matrix[itr][right])
            itr += 1
            
        right -= 1
        itr = right
        while itr >= left and len(spiral_elems) < size:
            spiral_elems.append(matrix[bottom][itr])
            itr -= 1
            
        bottom -= 1
        itr = bottom
        while itr >= top and len(spiral_elems) < size:
            spiral_elems.append(matrix[itr][left])
            itr -= 1
            
        left += 1
            
    return spiral_elems


print('test case...1')
rotated_elements = get_matrix_as_spiral([[1,2,3],[4,5,6],[7,8,9]])
print('rotated elements: ' + str(rotated_elements))
assert rotated_elements == [1,2,3,6,9,8,7,4,5]

print('test case...2')
rotated_elements = get_matrix_as_spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]])
print('rotated elements: ' + str(rotated_elements))
assert rotated_elements == [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

print('test case...3')
rotated_elements = get_matrix_as_spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print('rotated elements: ' + str(rotated_elements))
assert rotated_elements == [1,2,3,4,8,12,11,10,9,5,6,7]

print('test case...4')
rotated_elements = get_matrix_as_spiral([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
print('rotated elements: ' + str(rotated_elements))
assert rotated_elements == [1,2,3,6,9,12,11,10,7,4,5,8]

print('test case...5')
rotated_elements = get_matrix_as_spiral([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print('rotated elements: ' + str(rotated_elements))
assert rotated_elements == [1,2,3,4,5,10,15,14,13,12,11,6,7,8,9]

print('test case...6')
rotated_elements = get_matrix_as_spiral([[1,2,3],[4,5,6],[7,8,9], [10,11,12], [13,14,15]])
print('rotated elements: ' + str(rotated_elements))
assert rotated_elements == [1,2,3,6,9,12,15,14,13,10,7,4,5,8,11]

print('test case...7')
rotated_elements = get_matrix_as_spiral([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]])
print('rotated elements: ' + str(rotated_elements))
assert rotated_elements == [1,2,3,4,5,6,12,18,17,16,15,14,13,7,8,9,10,11]