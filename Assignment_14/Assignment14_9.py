class Product:
   def __init__(self, name, id):
      self.name = name
      self.id = id

   def __eq__(self, other):
      if isinstance(other, Product):
         return self.name == other.name and self.id == other.id
      return False


def main():
    p1 = Product("Marvellous", 153)
    p2 = Product("Marvellous", 153)

    if p1 == p2:
        print("p1 and p2 are equal")

if __name__ == "__main__":
    main()