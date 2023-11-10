# arr=[1,2,3,4,5,6,7,8,10]

def binarySearch(arr, l, r, x):
    while l<=r:
        mid = l + (r-l)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x :
            l = mid + 1
        else:
            r = mid - 1
    return - 1

# arr = [1,2,3,4,5,6,7,8,9,10,15]
# l , r, x = 0, len(arr)-1, 15
# ans = binarySearch(arr, l, r, x)
# print(ans)

list = []
n = int(input())
for i in range(0, n):
    list.append(int(input()))
l, x = 0, int(input())

ans = binarySearch(list, l, n-1, x)
if ans != -1:
    print(x, "Found at", ans)
else:
    print(x, "Not Found\n")
