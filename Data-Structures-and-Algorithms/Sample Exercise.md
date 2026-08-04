#### **SAMPLE PRACTICE PROBLEMS** 



**Problem 1: Find the complexity of the below recurrence:**  

&#x20;             { 3T(n-1), if  n>0,

T(n) =   { 1, otherwise





**Problem 2: Find the complexity of the recurrence:**  

&#x20;            { 2T(n-1) - 1, if n>0,

T(n) =   { 1, otherwise





**Problem 3: Find the complexity of the below program:** 



def funct(n):

&#x20;   if (n==1):

&#x20;      return

&#x20;   for i in range(1, n+1):

&#x20;       for j in range(1, n + 1):

&#x20;           print("\*", end = "")

&#x20;           break

&#x20;         print()



**Problem 4: Find the complexity of the below program:** 



def function(n):

&#x20;   # Initialize count to 0

&#x20;   count = 0

​

&#x20;   # Outer loop starts from n/2 and goes up to n

&#x20;   for i in range(n//2, n+1):

&#x20;       # Middle loop starts from 1 and goes up to n/2

&#x20;       for j in range(1, n + 1 - n//2):  # j + n//2 <= n

&#x20;           # Inner loop starts from 1 and doubles at each step

&#x20;           for k in range(1, n+1, k\*2):

&#x20;               # Increment count at each iteration

&#x20;               count += 1





**Problem 5: What is the time complexity of the following code:** 



a = 0;

for i in range(N):

&#x20; for j in reversed(range(i,N)):

&#x20;   a = a + i + j;

Options: 



A) 	O(N)

B)	O(N\*log(N))

C)	O(N \* Sqrt(N))

D)	O(N\*N)







**Problem 6: What is the time, and space complexity of the following code:** 



a = 0

b = 0

for i in range(N):

&#x20; a = a + random()



for i in range(M):

&#x20; b= b + random()



A) 	O(N \* M) time, O(1) space

B)	O(N + M) time, O(N + M) space

C)	O(N + M) time, O(1) space

D)	O(N \* M) time, O(N + M) space

