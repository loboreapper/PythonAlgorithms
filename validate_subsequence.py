def isValidSubsequence2(array, sequence):
    # Write your code here.
    comparison_index = 0
    for i in range(0, len(sequence)):
        found = False
        for j in range(comparison_index, len(array)):
            print('s', sequence[i] , array[j], 'a')
            if sequence[i] == array[j] and comparison_index < len(array):
                found = True
                comparison_index = j + 1
                break
        if not found:
            return False
    return True

def isValidSubsequence(array, sequence):
    # Write your code here.
    count_possition_array=0
    finished_sequence=0
    for number in range(count_possition_array,len(array)):
        if array[number] == sequence[finished_sequence]:
            finished_sequence+=1
            if finished_sequence == len(sequence):
                return True
    return False

#array = [5, 1, 22, 25, 6, -1, 8, 10]
#sequence= [1, 6, -1, 10]

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence=[22, 25, 6]


isValidSubsequence(array,sequence)

