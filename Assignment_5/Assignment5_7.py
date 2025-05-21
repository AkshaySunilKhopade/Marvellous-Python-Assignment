
Area = lambda L,B : 2 * L * B

Perimeter = lambda L,B : 2*(L+B)


def main():
    
    print("Enter the length of rectangle :")
    Length = float(input())
    print("Enter the length of rectangle :")
    Breadth = float(input())
    
    fArea = Area(Length,Breadth)
    fPerimeter = Perimeter(Length,Breadth)

    print("Area is :",fArea)
    print("Perimeter is :",fPerimeter)

if __name__ == "__main__":
    main()