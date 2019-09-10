for x in range (1, 10) :              # Starts for loop in range 1 - 10. This serves as the rows.
    for y in range (1, (x + 1)):     # Starts nested loop in range 1 - x+1 (for loop + 1). This serves as the columns. 
        print ((x * y), end= "\t")   # Multiply's for loop variable with nested loop variable. Inserts "tab" at the end of the text. 
    print ("")                         
    
