def summer_69(nums):
    # if 6 in nums:
    #     index_of_6 = nums.index(6)
    #     print(index_of_6)
    #     index_of_9 = nums.index(9)
    #     print(index_of_9)
    #     nums=nums[0:index_of_6] + nums[index_of_9+1:]
    #     print(nums)
    # return sum(nums)

    add = True
    total = 0

    for num in nums:
        while add:
            if num != 6:
                total = total + num
                break
            else:
                add = False
        while not add:
            if num!= 9 :
                break
            else:
                add = True
                break
    return total


arr = [1,3,5] #9
print(summer_69(arr))


arr = [4,5,6,7,8,9] #9
print(summer_69(arr))

arr = [2,1,6,9,11] #14
print(summer_69(arr))