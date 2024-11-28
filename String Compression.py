class Solution(object):
 def compress(self,chars):
    w = 0  
    r = 0   

    while r < len(chars):
        char = chars[r] 
        count = 0
        
      
        while r < len(chars) and chars[r] == char:
            r += 1
            count += 1
        

        chars[w] = char
        w += 1
        
       
        if count > 1:
            for digit in str(count):
                chars[w] = digit
                w += 1
    
    return w
