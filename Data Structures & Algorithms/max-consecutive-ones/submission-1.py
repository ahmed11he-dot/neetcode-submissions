class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
     count,output=0,0
               
     for n in nums:
        if n==1 :
            count +=1
            output=max(output,count)
        else:
            count = 0

     return output  
        

solution=Solution()
print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))