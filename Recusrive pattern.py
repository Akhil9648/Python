def pattern(n):
    if n==0:
        return 
    print("*"*n)
    pattern(n-1)
pattern(int(input("Enter a number")))

"""
Output:
Enter a number3
***
**
*
"""
=== Code Execution Successful ===
