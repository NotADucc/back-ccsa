def zeef(num) :
    arr = [i for i in range(2, num + 1)]
    ans = []
    index, mod = 0, 2
    while len(arr) > 0 :
        if index >= len(arr) :
            index = 0
            mod += 1
        num = arr[index]
        if num % mod == 0 :
            if num == mod :
                ans.append(num)
            arr.remove(num)
        else :
            index += 1
    return ans
