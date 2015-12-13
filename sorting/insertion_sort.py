def insertion_sort(list):
    """
    Insertion Sort traverses the list starting with a second element and assumes
     that items to the left of the Marker are already sorted. It grabs the next
     element to the right of the Marker in the list and puts it in the right
     position in the array to the left of the Marker. Insertion sort generally
     shows a good performance.
    Complexity: best O(n), average/worst O(n^2)
    """
    for marker in range(1, len(list)):
        cur_value = list[marker]
        cur_index = marker
        print('position', marker, ':', cur_value)
        while cur_index > 0 and list[cur_index - 1] > cur_value:
            list[cur_index] = list[cur_index - 1]
            cur_index -= 1
        if cur_index != marker:
            print(' -> put before', list[cur_index])
        else:
            print(' -> put after', list[cur_index - 1])
        list[cur_index] = cur_value
