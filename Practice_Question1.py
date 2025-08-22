def find_max_element(lst):
    """
    Function to find the maximum element in a list.
    :param lst: List[int] -> List of integers
    :return: int -> The maximum element in the list
    """
    max=0
    for i in lst:
        if max<=i:
            max=i
        else:
            pass
    return f"The maximum element in the list {max}"
usr_input=input("Input the Number separeted by Spaces:\n")
usr_list=list(map(float,usr_input.split()))
result=find_max_element(usr_list)
print(result)


