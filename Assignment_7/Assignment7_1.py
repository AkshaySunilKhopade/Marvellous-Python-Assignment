
square = lambda ino : ino**2
cube = lambda ino : ino**3


def main():
    print("Enter the number :")
    ino = int(input())

    s = square(ino)
    c = cube(ino)
    
    print("Sqaure is :",s)
    print("Cube is :",c)
    
if __name__ == "__main__":
    main()