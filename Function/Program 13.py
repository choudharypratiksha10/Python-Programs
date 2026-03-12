# Program 13: Pascal’s Triangle

def pascal_triangle(n):
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(prev[j-1] + prev[j])
        print(row)
        prev = row

rows = int(input("Enter number of rows: "))
pascal_triangle(rows)