class Solution(object):
    def isPalindrome(self, x): 
       s = str(x) # Transformando x numa String para poder identificar as indices
       if set(s[0]) == set(s[-1]) : # Aqui fala se o primeiro indice de x e o ultimo for igual e também se o numero de algarimos for impar então é um palindromo (ex: 1212121)
        if len(s) % 2 == 1 :
           return True
       else: 
          return False
       
#ainda possui muitos furos pois se forem números como 1331 ou 11 ou 13331 e assim por diante, ele provavelmente vai dar error ou null
    
sol = Solution()
print(sol.isPalindrome(121))
