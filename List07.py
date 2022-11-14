def main(list01):
    """
    A list of zeros and ones is given. Find how many zeros are involved and return.
    Args:
        list01(list): parameter
    Returns:
        int: return answer
    """
    k=0
    for i in list01:
        if i==0:
            k=list01.count(0)
    return k

print(main([1,0,1,0,0]))