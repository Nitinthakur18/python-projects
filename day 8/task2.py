def calculate_love_score(name1,name2):
    Total1 = 0
    name = (name1+name2).upper()
    for i in name:
        if i == 'T':
            Total1 += 1
        elif i == 'R':
            Total1 += 1
        elif i == 'U':
            Total1 += 1
        elif i == 'E':
            Total1 += 1
    Total2 = 0        
    for i in name:
        if i == 'L':
            Total2 += 1 
        elif i == 'O':
            Total2 += 1
        elif i == 'V':
            Total2 += 1
        elif i == 'E':
            Total2 +=1
    
    love_score = int(str(Total1) + str(Total2))        
    print(love_score)    
    
calculate_love_score("Angela Yu","Jack Bauer")   