def turnStoASC():

   
       strng = input ('Give me a strng')
       
       l = '%d'*len(strng) % tuple(map(ord, strng))
       l = int(l)
       print(l)
       
       if l > 1: 
   
               for i in range(2, l//2): #Tha mporouse na balw mexri l-1 alla etsi meiwnw simantika tin ypologistiki dynami
       
                       if (l % i) == 0: 
                               print(l, "den einai prwtos") 
                               break
               else: 
                     print(l, "einai prwtos") 
  
       else: 
              print(l, "den einai prwtos") 
       
     
turnStoASC()
  
      
