def find_max_consecutive_ones(nums):
    """
    Function to find the maximum number of consecutive 1's in a binary array.
    :param nums: List[int] -> A binary array where each element is either 0 or 1
    :return: int -> The maximum number of consecutive 1's
    """
    count = 0         # Current count of consecutive 1's
    max_count = 0     # Max count found so far

    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return f"The maximum number of consecutive 1's is {max_count}"

# Input from user
usr_input = input("A binary array (space-separated 0s and 1s): ")
usr_list = list(map(int, usr_input.split()))
result = find_max_consecutive_ones(usr_list)
print(result)
