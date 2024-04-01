product = {'name': 'Fancy pen', 'price': 14.99,
           'imported': True, 'stock': 793}

for key in product:
    print(key)
    
for price in product.values():
    print(price)

for key, price in product.items():
    print(key, '=', price)

print(key, price)