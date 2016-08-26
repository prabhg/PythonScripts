def maxSubarray(A):
    """
    This solves max-subarray problem using Kadane's algorithm
    """
    maxEndingHere = maxSumSoFar = A[0]
    maxSubarrStartIdx = maxSubarrEndIdx = 0
    for idx,x in enumerate(A[1:]):
        # calc max sum
        maxEndingHere = max(x, maxEndingHere + x)
        maxSumSoFar = max(maxSumSoFar, maxEndingHere)
        
        # update maxsubarray start and end indices
        # if maxEndingHere and maxSumSoFar are exactly same, then this is the end
        # index. In addition, if maxEndingHere and maxSumSoFar both happen to equal
        # current element, then this is also the start index
        if (maxEndingHere == maxSumSoFar):
            maxSubarrEndIdx = idx+1
            if (maxEndingHere == x):
                maxSubarrStartIdx = idx+1

    # return max sum and a tuple containing max subarray's start and end indices
    return maxSumSoFar, (maxSubarrStartIdx, maxSubarrEndIdx)
    
def sumIt(array, startIndex=0, endIndex=None):
    """
    Sums the array of numbers. Default startIndex is 0, and default endIndex is upto end of list
    """
    total = 0 
    # end index is 'inclusive', so need to +1
    for number in range(startIndex, (endIndex or len(array)-1) +1):
        total += array[number]
    return total

def fixedWidthMaxSubarray(A, width):
    """
    Calculate max subarray but of a fixed width.
    """
    if (width < 1): raise ValueError('target width is less than 1')
    # start index
    startIdx = subArrStartIdx = 0
    # end index
    endIdx = subArrEndIdx = subArrStartIdx + (width-1)
    # max sum
    maxSumSoFar = subarrSum = sumIt(A, startIdx, endIdx)
    
    while (True):
        # increment start index and end index
        startIdx += 1
        endIdx += 1
        
        if (endIdx >= len(A)):
            break
        # get new subarray sum
        subarrSum = sumIt(A, startIdx, endIdx)
        # if it is greater than older max sum, update maxsum and start/end values
        if (subarrSum > maxSumSoFar):
            subArrStartIdx = startIdx
            subArrEndIdx = endIdx
            maxSumSoFar = subarrSum
    
    return maxSumSoFar, (subArrStartIdx, subArrEndIdx)
