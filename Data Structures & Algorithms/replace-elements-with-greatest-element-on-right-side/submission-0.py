class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        for i in range(len(arr)):
            mx = -1
            for j in range(i+1,len(arr)):
                mx = max(mx,arr[j])
            arr[i] = mx
        return arr