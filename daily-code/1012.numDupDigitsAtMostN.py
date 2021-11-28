class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        notDupCount = 0
        for i in range(1,n+1):
            i_text = [x for x in str(i)]
            if len(set(i_text)) == len(i_text):
                notDupCount= notDupCount+1
        return n - notDupCount

solution = Solution()
input_num = 6358960
result = solution.numDupDigitsAtMostN(input_num)
print(f"input_num:{input_num},result:{result}")