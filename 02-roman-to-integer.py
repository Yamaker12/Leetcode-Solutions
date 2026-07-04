
#Date: 04/07/2026
#Difficulty: Eazy
#Problem link:https://leetcode.com/problems/roman-to-integer/
#Duration: 3 hours 😭
class Solution(object):
    def romanToInt(self, s):
        lista_romana = {

        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000

        }
        resultado = 0
        
        for x in range(len(s)):
                valor = lista_romana[s[x]]
                if x + 1 < len(s): # Se a x + 1 for menor que a len() então continua
                    proximo_valor = lista_romana[s[x+1]]
                    if proximo_valor > valor: # se o valor for menor que o proximo valor então vai subtrair com o resultado
                            resultado -= valor 
                    else: # Se não for menor então vai somar com o resultado
                            resultado += valor
                else: # se for igual a len() ou maior (impossivel) soma com o resultado
                    resultado += valor

        return result

                        
sol = Solution()
print(sol.romanToInt("IXI")) #Bote qualquer numero romano que no terminal vai resultar em numeros inteiros
