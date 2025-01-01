#Secret code language

inp = input("Enter the input : ")
reversed_string = inp[::-1]
if len(inp)<3:
    print(reversed_string)
    print("Do you want ot decode it : ", reversed_string)
    reply = input("Enter your reply :")
    if reply == "yes":
       print(inp)
       

else:
    new_string =inp[1:]
    random_characters = "aki"
    random2_characters = "tha"
    print(random_characters + new_string + inp[:1] + random2_characters)

#Decoding   
    print("Do you want ot decode it : ", random_characters + new_string + inp[:1] + random2_characters)
    reply = input("Enter your reply :")
    if reply == "yes":
       print(inp)



    
    
    
    #first_letter = inp[:1]
    #print(first_letter)
    
    #first_letter = inp[0]
    #new_string = inp
    #print(new_string)
    
    #print(inp + first_letter)
    
#length = len(inp)
#if length<3:
    
   
