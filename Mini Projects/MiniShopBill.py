products = {"iphone18": 200000, "laptop": 90000,
    "table": 12000, "bottle": 500, "tshirt": 600}
print(products)

name = input('Enter the Product Name You Want : ')
qty = 0

pro = products.get(name)
print(pro)

if pro:

    qty = int(input('Enter the Quentiy of You Want : '))
    bill = pro * qty
    print('---------- BILL ----------')
    print(f'Product : {name}')
    print(f'Price : {pro}')
    print(f'Quentity : {qty}')
    print(f'Total : {bill}')

else : 

    print(f'{name} not found..')
   


# for i,j in products.items() : 

#     if i == name : 
#         qty = int(input('Enter the Quentiy of You Want : '))
#         bill = j * qty
#         print('---------- BILL ----------')
#         print(f'Product : {i}')
#         print(f'Price : {j}')
#         print(f'Quentity : {qty}')
#         print(f'Total : {bill}')
#         break
#     else : 
#         print('Product Not Found...')

