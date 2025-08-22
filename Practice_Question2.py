def sum_of_elements(lst):
    """
    Function to find the sum of all elements in the list.
    :param lst: List[int] -> List of integers
    :return: int -> The sum of all elements in the list
    """
    sum=0
    for i in lst:
        sum=sum+i
    return f"The sum of all elements in the list is {sum}"
usr_input=input("Input the list of all Integer  ")
usr_int=list(map(int,usr_input.split()))
result=sum_of_elements(usr_int)
print(result)