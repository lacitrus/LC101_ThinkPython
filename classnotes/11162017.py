#put * infront of tuple can break it into elements and be used
#function(*my_tuple)
#my_tuple = ('1', '2','3','4')
def function(par1, par2, par3, par4):
    print(par2)


mytuple=("fun",)
print(mytuple)
#without ',' mytuple becomes string, try to see the difference of the assignment statements

#mytuple("fun","aaa")
#print(sorted(mytuple))#is going to return ["fun","aaa"]
#print(mytuple)# is going to print ("fun","aaa")
#all of these is because tuple is immutable, you can make operations on it but cannot change it

