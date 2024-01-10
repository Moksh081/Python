class Solution:
    def duplicates(self, arr, n): 
        max_val = max(arr)
        l = [0] * (max_val + 1)

        result = []
        for i in range(n):
            l[arr[i]] += 1

        duplicate_found = False
        for i in range(max_val + 1):
            if l[i] > 1:
                result.append(i)
                duplicate_found = True

        if not duplicate_found:
            result.append(-1)

        return result
