def max_subarray(array):
    """
    Solves max subarray problem using Kadane's algorithm
    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    There are enhancements to given algorithm to also calculate the start and end 
    indices of max subarray. Returns a tuple containing max_subarray sum and subarray itself
    """
    maxAtCurrentIndex = 0
    maxSumSoFar = 0
    maxSubarrayStartIndex = None
    maxSubarrayEndIndex = None
    
    for index, number in enumerate(array):
        maxAtCurrentIndex = max(0, maxAtCurrentIndex + number)
        maxSumSoFar = max(maxSumSoFar, maxAtCurrentIndex)
        
        if (maxAtCurrentIndex == 0):
            maxSubarrayStartIndex = None
        
        if(maxSumSoFar == maxAtCurrentIndex):
            maxSubarrayEndIndex = index
            if(maxSubarrayStartIndex is None):
                maxSubarrayStartIndex = index
        
    maxSubArray = [array[maxSubarrayStartIndex]] if maxSubarrayStartIndex == maxSubarrayEndIndex else array[maxSubarrayStartIndex:maxSubarrayEndIndex+1]
    
    return (maxSumSoFar, maxSubArray)
    
def max_subarray_sum(array):
    """
    Solves max subarray problem using Kadane's algorithm
    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    """
    maxAtCurrentIndex = 0
    maxSumSoFar = 0
    
    for number in array:
        maxAtCurrentIndex = max(0, maxAtCurrentIndex + number)
        maxSumSoFar = max(maxSumSoFar, maxAtCurrentIndex)
    
    return maxSumSoFar

# print max subarray sum only
print(max_subarray_sum([-10,2,3,-2,0,5,-20, 9]))
print(max_subarray_sum([2,3,-2,-1,10]))

# print max subarray sum and subarray both
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))