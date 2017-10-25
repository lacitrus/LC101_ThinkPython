#Fibonacci sequence code by Garry, classmate in LC101 Tampa


def fib_sequence(num):
    a = 1
    b = 0
    def get_sequence(a,b):
        for i in range(num):
            c = b
            b = a+b
            a = c
        return (b)
    return get_sequence(a,b)
print(fib_sequence(4))


#Here are two set of code from stack overflow on this function
#number 1

def fib(n):
    a = 0
    b = 1
    for i in range(0,n-1):
        b = a+b
        a = b-a
    return b

n = int(input("a number"))
print(fib(n))

#number 2
def fib(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fib(n-1) + fib(n-2)  
