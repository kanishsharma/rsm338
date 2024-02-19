def reverse_groups(numbers, k):
    # Convert the string of numbers into a list of integers
    num_list = list(map(int, numbers.split(',')))
    # Initialize the index for the list
    index = 0
    # Process chunks of k elements
    while index + k <= len(num_list):
        # Reverse the chunk of k elements using slicing
        num_list[index:index+k] = num_list[index:index+k][::-1]
        # Move to the next chunk
        index += k
    # Convert the list of integers back to a string with comma separation and include k
    return ','.join(map(str, num_list))


print(reverse_groups([1,2,3,4,5], 5))