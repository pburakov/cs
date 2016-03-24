def merge_sort(list):
    """
    Merge sort is a recursive sorting algorithm that continuously spits a list in
     half, sorts each half with the same method and then merges them into a sorted version.
     Eventually two list containing a single element are sorted. That is the base case for
     a merge sort.

    Complexity: O(n log(n)) in all cases. Log(n) for splitting, n for merge.
     Merge Sort requires additional memory to hold the sliced two halves which can
     be critical for larger sets.
    """

    def merge(left, right):
        """
        This merge helper is doing the "heavy lifting". Values are picked one by one form `left`
         and `right` lists.
        Lists that have more than one element are already sorted, so the first element from
         each is "picked".
        """
        print('merging', left, 'and', right, end=' ')
        result = []
        left_i, right_i = 0, 0
        while left_i < len(left) and right_i < len(right):
            # Change the direction of this comparison to change the direction of the sort
            if left[left_i] <= right[right_i]:
                result.append(left[left_i])
                left_i += 1
            else:
                result.append(right[right_i])
                right_i += 1
        # Adds remaining elements
        if left:
            result.extend(left[left_i:])
        if right:
            result.extend(right[right_i:])
        print('into', result)
        return result

    print('splitting', list, 'in half')
    if len(list) <= 1:
        return list  # Base case
    mid_i = len(list) // 2
    left = list[:mid_i]
    right = list[mid_i:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
