#Duration: 20 min
#Difficulty: Eazy
#Date:04/07/2026
#Problem: https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
          marked = target - nums[i] #Daqui pra baixo tecnicamente vê se a subtração entre o numero escolhido e primeiro numero da lista existe na lista se existir então retorne o indice da subtraçao e  o i
          if marked in nums:
            if nums.index(marked) != i:#aqui checa se o numero da subtração ta no indice diferente do que o i
                  
                return i , nums.index(marked)
