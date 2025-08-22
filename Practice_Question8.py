import numpy as np
def is_sorted(arr):
    """
    Function to check if the given array is sorted in non-decreasing order.
    :param arr: List[int] -> A list of integers
    :return: bool -> True if the array is sorted, False otherwise
    """
    size=len(arr)
    for i in range(size):
        for j in range(size-i-1):
            if arr[j]>arr[j+1]:
                t=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=t
    return arr
usr_input=input("Input numbers separeted by spaces: ")
usr_list=list(map(int,usr_input.split()))
usr_arr=np.array(usr_list)
print(type(usr_arr))
result=is_sorted(usr_arr)
print(result)
    