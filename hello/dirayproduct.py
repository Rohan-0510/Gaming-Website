# diray product

class dirayproduct:
    def __init__(self, no, b, t, p, g):
        self.diaryId = no
        self.diraybrand = b
        self.producttype = t
        self.price = p
        self.grade = g


class productgrade:
    def __init__(self, dl, wd):
        self.diraylist = dl
        self.weightagedict = wd

    def pricebasedonBrandtype(self, diray_brand, ptype):
        ans = []
        for i in self.diraylist:
            if i.diraybrand == diray_brand and i.producttype == ptype:
                i.price += i.price * self.weightagedict[i.grade] / 100
                ans.append((diray_brand, i.price))

        return ans


if __name__ == '__main__':
    n = int(input("enter the no.of product: "))
    diray_product = []

    for i in range(n):
        dirayid = int(input("Enter the id: "))
        diraybrand = input("Enter the brand: ")
        producttype = input("Enter the type: ")
        price = int(input("Enter the price: "))
        grade = input("Enter the grade: ")
        dirayobj = dirayproduct(dirayid, diraybrand, producttype, price, grade)
        diray_product.append(dirayobj)

    n2 = int(input("enter the no of grade: "))
    weightage_dict = {}

    for i in range(n2):
        grade = input("enter the grade: ")
        weight = int(input("Enter the weightage: "))

        weightage_dict[grade] = weight

    prodobj = productgrade(diray_product, weightage_dict)

    brand_name = input("Enter the brand_name: ")
    product_type = input("Enter the product_type: ")

    result = []
    result = prodobj.pricebasedonBrandtype(brand_name, product_type)

    if len(result) == 0:
        print("Diary Not Found:")
    else:
        for i in result:
            print("Diray_brand: ", i[0])
            print("Updated_price: ", i[1])
