class Solution(object):
    def isPalindrome(self, x):
        number = str(x) # Transformando o número int em uma string pra poder conseguir usar os colchetes
        if number == number[::-1]: # Se o número for igual ao número de traz para frente então é um palíndromo
            return True
        else:
            return False

sol = Solution()
print(sol.isPalindrome(1221))
# Essa foi a resposta
# A resolução era muito mais simples que parecia😭😭
