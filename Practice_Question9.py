def move_zeroes(nums):
    """
    Function to move all 0's to the end of the array while maintaining the order of non-zero elements.
    :param nums: List[int] -> A list of integers
    :return: None -> The list is modified in place
    """
    count=0
    for i in nums:
        if i==0:
            nums.remove(i)
            count=count+1
    for i in range(count):
        nums.append(0)
    return f"The list is modified in place {nums}"
usr_input=input("Enter the List of integers ")
usr_list=list(map(int,usr_input.split()))
result=move_zeroes(usr_list)
print(result)