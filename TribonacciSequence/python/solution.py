def tribonacci(signature, n):
    lst = signature[:n]
    for i in range(3, n):
        lst.append(lst[i - 1] + lst[i - 2] + lst[i - 3])
    return lst[:n]
