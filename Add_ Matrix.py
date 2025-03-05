# A basic code for matrix input from user

R = int(input(&quot;Enter the number of rows:&quot;))
C = int(input(&quot;Enter the number of columns:&quot;))

# Initialize matrix
matrix = []
print(&quot;Enter the entries rowwise:&quot;)

# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = &quot; &quot;)
    print()
