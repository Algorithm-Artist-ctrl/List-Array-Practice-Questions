def find_missing_number(nums):
    """
    Function to find the missing number in the array.
    :param nums: List[int] -> A list of distinct integers in the range [0, n]
    :return: int -> The missing number in the range
    """
    max=0
    for m in nums:
        if max<=m:
            max=m
    numbers=list(range(m+1))
    print(numbers)
    miss_num=[]
    for i in numbers:
        if i not in nums:
            miss_num.append(i)
    return f"The missing numbers in the range are {miss_num}"
usr_input=input("Input the list separeted by space: ")
usr_list=list(map(int,usr_input.split()))
result=find_missing_number(usr_list)
print(result)