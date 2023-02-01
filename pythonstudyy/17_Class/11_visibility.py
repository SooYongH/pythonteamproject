#가시성(visibility)

class Product:
    id=0
    def __init__(self,name='product'):
        Product.id += 1
        self.name= name + str(Product.id)

    def printProduct(self):
        print(f'제품이름은 {self.name}')

class Inventory:
    def __init__(self):
        self.__items = [] #비공개 메서드

    def addNewItem(self,product):
        if type(product) == Product :
            self.__items.append(product)
            print('new item added')
        else:
            print('error')

    def getNumberOfItems(self):
        return len(self.__items)

    def printItems(self):
        for getItems in self.__items:
            getItems.printProduct()

    @property #비공개 변수 외부에서 직접 반환할 수 있게함
    def items(self):
        return self.__items

myInvent =Inventory()
product1=Product()
print(type(product1))
myInvent.addNewItem(Product())
myInvent.addNewItem(Product())
myInvent.addNewItem(Product())

print('추가된 아이템의 수는 =', myInvent.getNumberOfItems())
print()
myInvent.printItems()
print(myInvent.items) #myInvet.__items 오류나지만 @proverty덕분에 오류없음