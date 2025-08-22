def is_palindrome(lst):
    """
    Function to check if a list is a palindrome.
    :param lst: List[int] -> List of integers
    :return: bool -> True if the list is a palindrome, False otherwise
    """
    temp=lst[::-1]
    if temp==lst:
        return True
    else:
        return False
usr_input=input("The Input  ").split()
usr_list=list(map(int,usr_input))
result=is_palindrome(usr_list)
print(result)

