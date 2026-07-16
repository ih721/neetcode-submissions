class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n= len(arr)
        i = n-1
        r_max= -1
        while i >= 0:
            arr[i], r_max = r_max, max(arr[i], r_max)
            i -= 1
        return arr

            
               

        