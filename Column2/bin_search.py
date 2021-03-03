def find_one_duplicate_element(arr, lo, hi):
    if lo + 1 >= hi:
        return arr[lo] + 1
    mid = lo + ((hi - lo) // 2)
    # if the range of nums in left half, is less than number of el in left, search left
    if arr[mid] - arr[lo] != mid - lo:
        return find_one_duplicate_element(arr, lo, mid)
    if arr[hi] - arr[mid] != hi - mid:
        return find_one_duplicate_element(arr, mid, hi)
    print("No duplicates")
    return -1

def find_one_missing_element(arr, lo, hi):
    if lo + 1 >= hi:
        return arr[lo] + 1 
    mid = lo+ (hi - lo) //2
    if arr[mid] - arr[lo] != mid - lo:
        return find_one_missing_element(arr, lo, mid)
    if arr[hi] - arr[mid] != hi - mid:
        return find_one_missing_element(arr, mid, hi)
    print("No Missin Numbers")
    return -1


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    nums2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print(find_one_duplicate_element(nums, 0, len(nums) - 1))
    print(find_one_missing_element(nums2, 0, len(nums2) - 1))
