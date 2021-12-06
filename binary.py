def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index+(end_index-begin_index) // 2

midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint-1
        else:
            begin_index = midpoint+1
    return None


sequence_a = [2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
sequence_b = [13, 123, 5, 12, 5, 6, 7, 12, 4, 15, 6, 7, 20]
item_a = 123
print(binary_search(sequence_b, item_a))
