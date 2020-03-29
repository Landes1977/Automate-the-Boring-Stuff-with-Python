# Programmer: Matthew Landes
# Date:		  March 22, 2020

def printTable(table):
    colWidth = []
    for i in range(len(table)):
        width = 0
        for j in range(len(table[i])):
            if len(table[i][j]) > width:
                width = len(data[i][j])
        colWidth.append(width)
     
    for j in range(len(table[0])):
        text = ''
        for i in range(len(table)):
            text = text + ' ' + table[i][j].rjust(colWidth[i])
        print(text)
        
    return




data = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]
  
print(printTable(data))