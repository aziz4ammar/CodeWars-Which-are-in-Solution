def in_array(array1, array2):
    result = []
    for word1 in array1:
        for word2 in array2:
            if word1 in word2 and word1 not in result:
                result.append(word1)
    result.sort()
    return result