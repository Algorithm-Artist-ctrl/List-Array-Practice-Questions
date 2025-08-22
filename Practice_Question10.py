def intersection(nums1, nums2):
    """
    Function to find the intersection of two integer arrays.
    :param nums1: List[int] -> First array of integers
    :param nums2: List[int] -> Second array of integers
    :return: List[int] -> An array of unique integers present in both arrays
    """
    set1=set(nums1)
    set2=set(nums2)
    unique=list(set1.intersection(set2))
    return f"An array of unique integers present in both arrays {unique}"
usr_input1=input("Enter the list1 of integer:  ")
usr_input2=input("Enter the list2 of integers:  ")
usr_list1=list(map(int,usr_input1.split()))
usr_list2=list(map(int,usr_input2.split()))
result=intersection(usr_list1,usr_list2)
print(result)