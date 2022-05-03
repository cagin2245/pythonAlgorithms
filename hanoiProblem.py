def hanoi(n,x,y,z):
    if(n==1):
        print("Diski {} çubuğundan {} çubuğuna koy. ".format(x,z))
        return
    else:
        hanoi(n-1, x, z, y)
        hanoi(1, x, y, z)
        hanoi(n-1, y, x, z)
if __name__ == '__main__':
    n = int(input("Disk sayısı N: "))
    hanoi(n, 'A', 'B', 'C')
