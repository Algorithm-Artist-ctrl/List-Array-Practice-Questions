def reverse_list(lst):
    """
    Function to reverse the order of elements in a list.
    :param lst: List[int] -> List of integers
    :return: List[int] -> The list with elements in reversed order
    """
    rev=lst[::-1]
    return f"The list with elements in reversed order is {rev}"
usr_input=input("List of integers:\n")
usr_list=list(map(int,usr_input.split()))
result=reverse_list(usr_list)
print(result)