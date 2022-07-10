height = int(input("Enter height of board "))
width = int(input("Enter width of board "))
i =  int(input("Enter i "))
j = int(input("Enter j "))
print("Neighbouring cells are:")
for p in range(i-1, i+2):
    for q in range(j-1, j+2):
        if (p, q)==(i, j):
            continue
        #If cell is in bound
        if 0 <= p < height and 0 <= q < width:
           #Prints neighbouring cells
           print((p, q)) 