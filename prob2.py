find_top_seller=(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10,   "Banan": 5,    "Uzum": 8}
)

qyt=find_top_seller[1]
products=find_top_seller[0]
shop=tuple((name,product*price)
             for i,(name,product) in enumerate(products.items())
             for n,price in enumerate(qyt.values())
             if i==n)
max_product=max(shop,key=lambda x : x[-1])
print(f"Eng daromadli mahsulot\n{max_product[0]} : {max_product[-1]}")
