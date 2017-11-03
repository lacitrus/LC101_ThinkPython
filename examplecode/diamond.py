def diamond(n):
    for i in range(n):
        print((n-i-1)*' ' + (1 + i *2)*'#')
    for i in range(n-1,0, -1):
        print((n-i)*' ' + (i*2-1)*'#')
              
def main():
    diamond(5)     
    
if __name__ == "__main__":
    main()