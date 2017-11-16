def multi_table(n):
    for i in range(n+1):
        for j in range(n+1):
            print(i * j, end =' ')
            if j == n:
                print('\t')
        
           
            

def main():
    multi_table(3)
    
if __name__ == "__main__":
    main()

# to suppress the endline terminator supplied by the print function, we add the optional argument end = ''. 
# And to make the layout look nicer, we add an empty string to our print call.