#massiv and function
def gg(perem):
    return  perem[1:] ==[i+1 for i in  perem[:-1]]

def main():
    print(gg([-1, 0, 1, 2, 3]))
    print(gg([-1, 0, 1, 3, 4]))
    print(gg([0, 1]))
    print(gg([1, 0] ))

if __name__=="__main__":
    main()