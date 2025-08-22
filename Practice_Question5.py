def rotate_left(ARR, D):
    """
    Function to rotate the list to the left by D positions.
    :param ARR: List[int] -> The list of integers
    :param D: int -> The number of positions to rotate
    :return: List[int] -> The list after rotation
    """
    arr=(ARR[D:])
    for i in arr:
        if i in arr:
            ARR.remove(i)
    rotate=[]
    for j in arr:
        rotate.append(j)
    for k in ARR:
        rotate.append(k)
    return f"The list after rotation {rotate}"
usr_input=input("The list of integers separeted by spaces   ")
pos=int(input("The number of positions to rotate  "))
usr_list=list(map(int,usr_input.split()))
result=rotate_left(usr_list,pos)
print(result)

