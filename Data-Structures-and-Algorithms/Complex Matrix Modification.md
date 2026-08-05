##### **Complex Matrix Modification (Space Focus)**



Analyse the precise asymptotic Time and Auxiliary Space Complexity of the following algorithmic operation: 



**text Matrix-Transform(Array A\[n]\[n]):**

&#x20;   Create a new 2D array Matrix B of size n x n

&#x20;   for i = 1 to n:

&#x20;       for j = 1 to n:

&#x20;           Matrix B\[i]\[j] = A\[i]\[j] \* 2

&#x20;   

**Recursive-Reduce(MatrixB, n)**

&#x20;text Recursive-Reduce(Array B\[]\[], int size):

&#x20;  		 if size <= 1:

&#x20;      			return

&#x20;   

// Performs an in-place array step modification taking O(1) time

&#x20;   		Recursive-Reduce(B, size / 2)



**1. Break Down Component Time Complexities** 

**Allocation and Nested Loop Initialization:** 

Memory initialization and copying requires visiting every cell of the n × n matrix. 

This step costs Θ(n²) time.

**Recursive Call Reduction:** 

The function Recursive-Reduce reduces the problem size by half on each execution loop ((size right arrow frac{size}{2})). 

The recurrence is (T\_{rec}(n) = T\_{rec}(frac{n}{2}) + Theta(1)). 

By Master Theorem, this evaluates to (Theta(log n)).



**2. Combine Time Components** 

Add the execution times together. 

The polynomial term heavily dominates the logarithmic term: 

&#x09;		(T\_{total}(n)=Theta (n^{2})+Theta (log n)=Theta (n^{2}))



**3. Evaluate Spatial Requirements**

Input Space: Explicit memory allocation for the initial matrix A takes up n × n = Θ(n²) space.



Auxiliary Space (Explicit): 

A separate duplicate matrix structure Matrix B of dimensions n × n is declared inside the scope:

&#x09;		(text{Memory}\_{text{Matrix B}}=Theta (n^{2}))



Auxiliary Space (Implicit Stack): 

The recursion depth of Recursive-Reduce drops logarithmically: 

&#x09;		(text{Memory}\_{text{Stack}}=Theta (log n))

