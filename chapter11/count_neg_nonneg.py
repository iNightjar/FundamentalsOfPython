#Initialize counters
def count_neg_nonneg(nums):
    neg_count, nonneg_count = 0, 0
    for num in nums:
        if num < 0 :
            neg_count += 1
        else: 
            nonneg_count += 1

    return neg_count, nonneg_count


print(count_neg_nonneg([12,3,4,-13,4,-23]))
print(type(count_neg_nonneg([12, 3, 4, -13, 4, -23])))
