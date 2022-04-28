# a linear search algorithm

def search_unsorted(thelist, value):
    n = len(thelist)
    for i in range(n):
        if thelist[i] == value:
            return True
    return False  # item not in list

def search_sorted(thelist, value):
    n = len(thelist)
    for i in range(n):
        if thelist[i] == value:
            return True
        elif thelist[i] > value:
            return False
    return False

def smallest_element(thelist):
    n = len(thelist)
    smallest = thelist[0]  # assumes the first element is the smallest element
    for i in range(1, n):
        if thelist[i] < smallest:
            smallest = thelist[i]
    return smallest


# binary search algorithm with a time complexity of O(log n)

def binary_search(thelist, value):
    n = len(thelist)
    low = 0
    high = n-1

    while low <= high:
        mid = (low+high) // 2
        if thelist[mid] == value:
            return True
        elif thelist[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return False



def bubble_sort(the_list):
    n = len(the_list)
    for i in range(n-1):
        for j in range(i, n-2):
            if the_list[j] > the_list[j+1]:
                the_list[j], the_list[j+1] = the_list[j+1], the_list[j]
    return the_list


def insertion_sort(the_list):
    # loop from the second value of the array
    for i in range(1, len(the_list)):
        item = the_list[i] # item to be repositioned

        j = i - 1 # will be used to reposition  the key item to the left
        while j >= 0 and the_list[j] > item:
            the_list[j+1] = the_list[j]
            j -= 1

        the_list[j+1] = item
    return the_list

def merge(left, right):
    """ takes in two array split from an original array """

    # returns the other array if either of them is empty
    if not left:
        return right
    if not right:
        return left

    merged_list = []
    index_right = index_left = 0

    #keeps looping until the array contains all the right and left array elements
    while len(merged_list) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            merged_list.append(left[index_left])
            index_left += 1
        else:
            merged_list.append(right[index_right])
            index_right += 1

        # if we reach the end of either arrays
        if index_right == len(right):
            merged_list.append(left[index_left:])
            break
        if index_left == len(left):
            merged_list.append(right[index_right:])
            break

    return merged_list

# the function to split the list

def split_merge(_array):
    if len(_array) < 2:
        return _array
    mid = len(_array) // 2

    # sorts the function by recursively splitting the array into half and merging it
    return merge(split_merge(_array[:mid]), split_merge(_array[mid:]))