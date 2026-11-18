class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      L,output=0,0
               
      for R,n in enumerate(nums):
        if n==0 :
            L=R+1

        output=max(output, R-L+1)

      return output

solution=Solution()
print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))