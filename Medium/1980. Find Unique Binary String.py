class Solution:
    def findActualNumber(self, num):
        j = 0 
        result = 0
        for i in range(len(num)-1,-1,-1):
            result += pow(2,j)*int(num[i])
            j+=1

        return result 
    
    def convertToBinary(self, string, len) :
        binary = bin(int(string))[2:]
        return binary.zfill(len)
        

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # num_size = len(nums[0])
        # limit = pow(2,num_size)-1
        # nums_converted = set([self.findActualNumber(x) for x in nums])
        # for i in range(limit+1):
        #     if i not in nums_converted:
        #         return self.convertToBinary(i,len(nums[0]))

        for num in nums :
            num
