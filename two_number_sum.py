def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(0, len(array)): #n
        for j in range(i + 1, len(array)): # n*m
            inner_sum = array[i] + array[j] # n*m
            print('inner_sum: ', inner_sum, "targetSum", targetSum)
            if inner_sum == targetSum: #n*m
                return [array[i], array[j]] # 1
    return [] # 1

# n + n*m + n*m + n*m = n + 3*n*m = n*2 + 1



array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

twoNumberSum(array, targetSum)

def fastTwoNumberSum(array, targetSum):
    numbers_dict = {}
    for number in array:
        to_find = targetSum - number
        if to_find in numbers_dict:
            return [number, numbers_dict[number]]
        else:
            numbers_dict[number] = to_find
    return []