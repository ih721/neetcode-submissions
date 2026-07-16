class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n= len(arr)
        i = n-1
        r_max= -1
        curr = 0
        while i >=0:
            curr = arr[i]
            arr[i] = r_max
            r_max = max(r_max, curr)
            i-=1
        return arr

            
               

        