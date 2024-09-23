def zoekBinair(arr, target):
    left = 0
    right = len(arr) - 1
    while left != right :
        print(str(left) + ", " + str(right))
        mid = (left + right) // 2
        if arr[mid] < target :
            left = mid + 1
        else :
            right = mid
 
    return left if arr[left] == target else -1
    