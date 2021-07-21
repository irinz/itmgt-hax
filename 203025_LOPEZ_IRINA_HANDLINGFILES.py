#dictionary

products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

# problem 1

def get_product(code):
    return products[code]

# problem 2

def get_property(code,property):
    return products[code][property]

# problem 3

def main():
    americano = 0
    brewedcoffee = 0
    cappuccino = 0
    dalgona = 0
    espresso = 0
    frappuccino = 0

    current_order = ""

    while current_order != "/":
        current_order = input("Please input your order (product,quantity): ")

        if current_order != "/":
            new_order = current_order.split(",")
            product_code = new_order[0]
            product_quantity = new_order[1]

            if product_code.lower() == "americano":
                americano += int(product_quantity)
            elif product_code.lower() == "brewedcoffee":
                brewedcoffee += int(product_quantity)
            elif product_code.lower() == "cappuccino":
                cappuccino += int(product_quantity)
            elif product_code.lower() == "dalgona":
                dalgona += int(product_quantity)
            elif product_code.lower() == "espresso":
                espresso += int(product_quantity)
            elif product_code.lower() == "frappuccino":
                frappuccino += int(product_quantity)

        else:
            break

    with open("receipt.txt","w") as f:
        f.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n''')

    with open("receipt.txt","a+") as f:
        total = 0

        if americano > 0:
            f.write('americano\t\t'+get_property("americano","name")+'\t\t'+str(americano)+'\t\t\t\t'+str(americano*get_property("americano","price"))+'\t\n')
            total += americano*get_property("americano","price")
        if brewedcoffee > 0:
            f.write('brewedcoffee\t\t'+get_property("brewedcoffee","name")+'\t\t'+str(brewedcoffee)+'\t\t\t\t'+str(brewedcoffee*get_property("brewedcoffee","price"))+'\t\n')
            total += brewedcoffee*get_property("brewedcoffee","price")
        if cappuccino > 0:
            f.write('cappuccino\t\t'+get_property("cappuccino","name")+'\t\t'+str(cappuccino)+'\t\t\t\t'+str(cappuccino*get_property("cappuccino","price"))+'\t\n')
            total += cappuccino*get_property("cappuccino","price")
        if dalgona > 0:
            f.write('dalgona\t\t\t'+get_property("dalgona","name")+'\t\t\t'+str(dalgona)+'\t\t\t\t'+str(dalgona*get_property("dalgona","price"))+'\t\n')
            total += dalgona*get_property("dalgona","price")
        if espresso > 0:
            f.write('espresso\t\t'+get_property("espresso","name")+'\t\t'+str(espresso)+'\t\t\t\t'+str(espresso*get_property("espresso","price"))+'\t\n')
            total += espresso*get_property("espresso","price")
        if frappuccino > 0:
            f.write('frappuccino\t\t'+get_property("frappuccino","name")+'\t\t'+str(frappuccino)+'\t\t\t\t'+str(frappuccino*get_property("frappuccino","price"))+'\t\n')
            total += frappuccino*get_property("frappuccino","price")

        f.write(f'''\t\t\t\t\t\t\t\t\t\t\n''')
        f.write(f'''Total:\t\t\t\t\t\t\t\t\t\t{total}\n''')
        f.write(f'''==''')

    with open("receipt.txt","r") as f:
        final = f.read()
        print(final)

main()
