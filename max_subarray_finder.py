def max_subarray(array):
    """
    Solves max subarray problem using Kadane's algorithm
    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    There are enhancements to given algorithm to also calculate the start and end 
    indices of max subarray. Returns a tuple containing max_subarray sum and subarray itself
    """
    maxAtCurrentIndex = array[0]
    maxSumSoFar = array[0]
    maxSubarrayStartIndex = 0
    maxSubarrayEndIndex = 0
    
    # slice array to start looping from its first element onwards
    for index, number in enumerate(array[1:]):
        maxAtCurrentIndex = max(number, maxAtCurrentIndex + number)
        maxSumSoFar = max(maxSumSoFar, maxAtCurrentIndex)
        
        # if max sum so far is same as max at current index, the maxSubArray ends at current index
        if (maxSumSoFar == maxAtCurrentIndex):
            maxSubarrayEndIndex = index + 1     # adding 1 because we are starting looping from first element of array

            # if max at curr index is ALSO eq to the number itself, it means maxSubArr starts at curr index
            if (maxAtCurrentIndex == number):
                maxSubarrayStartIndex = index + 1            
        
    maxSubArray = [array[maxSubarrayStartIndex]] if maxSubarrayStartIndex == maxSubarrayEndIndex else array[maxSubarrayStartIndex:maxSubarrayEndIndex+1]
    
    return (maxSumSoFar, maxSubArray)
    
def max_subarray_sum(array):
    """
    Solves max subarray problem using Kadane's algorithm
    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    Code is modified to support returning max element value in case all 
    elements in array are -ve.
    """
    maxAtCurrentIndex = 0
    maxSumSoFar = 0
    maxElement = array[0]

    for number in array:
        maxAtCurrentIndex = max(0, maxAtCurrentIndex + number)
        maxSumSoFar = max(maxSumSoFar, maxAtCurrentIndex)
        maxElement = max(maxElement, number)
    
    return maxSumSoFar if maxSumSoFar > 0 else maxElement


# Examples:
# print max subarray sum only
print(max_subarray_sum([-10,2,3,-2,0,5,-20, 9]))
print(max_subarray_sum([2,3,-2,-1,10]))

# print max subarray sum and subarray both
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray([-8,-89, -76, -70]))
print(max_subarray([-6,-2, 0, -70, -1]))
print(max_subarray([-6,-2, 0, 2, -70, -1]))
print(max_subarray([-6,-2, 0, 2, 1, -70, -1]))