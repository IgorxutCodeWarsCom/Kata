def triangle_type(a, b, c):

    if (a + b) > c and (a + c) > b and (b + c) > a:

        list1 = [a, b, c]
        list1.sort()

        if list1[2] * list1[2] < (list1[0] * list1[0] + list1[1] * list1[1]):
            return 1  # 1 : acute triangle

        if list1[2] * list1[2] == (list1[0] * list1[0] + list1[1] * list1[1]):
            return 2  # 2 : right triangle

        if list1[2] * list1[2] > (list1[0] * list1[0] + list1[1] * list1[1]):
            return 3  # 3 : obtuse triangle

    else:

        return 0  # 0 : if triangle cannot be made with given sides
