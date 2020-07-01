import random
# comment
age = 10

if age > 17 :
    status = 'You can get in'
else:
    status = 'You are too young, hence, you cannot get in.'

print(status)

# time complexity is 5 BIG O O(C) O(1)


max_range = random.randint(0, 20)

for n in range(0, max_range):
    print(n)

# 1 + n*2 then O(n)

def print_element(my_list):
    for n in len(my_list):
        print(n)




my_matrix = [[1,2,3],
             [4,5,6],
             [7,8,9]]


print(my_matrix[2][2])


def print_matrix(my_matrix):

    n_rows = len(my_matrix)
    n_columns = len(my_matrix[0])

    for r in range(0, n_rows):
        for c in range(0, n_columns):
            print(my_matrix[r][c])

print_matrix(my_matrix)