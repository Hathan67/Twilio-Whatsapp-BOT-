from models import Product, Odetails
from database import SessionLocal, session, engine
from sqlalchemy.sql import select
from sqlalchemy import func


# hii= session.query(Odetails).filter(Product.orders.any(order_id="AB123")).all()
# orders = session.query(Odetails).join(Odetails.products).filter(Odetails.product_id==Product.product_id).filter(Odetails.order_id=="AB123").all()
# orders = session.query(Odetails).select_from(Product).join(Odetails.products).filter(Odetails.order_id=="AB123").all()
#
# for order in orders:
#     print(order)

# han = session.query(Odetails, Product).filter(Odetails.product_id==Product.product_id).filter(Odetails.order_id=="AB123").all()
# for o, p in han :
    # print(p.product_name)
    # print(o.order_id)
    # print(f"{o.order_id} {p.product_name}")

# han = session.query(Odetails).join(Odetails.products).options(joinedload(Odetails.products)).filter(Odetails.order_id=="AB123").all()
# for ha in han:
#     print(ha)

# orders = session.query(Odetails).join(Odetails.products).filter(Odetails.order_id=='AB123').limit(3)
# products = session.query(Product).join(Product.orders).filter(Odetails.order_id=='AB123').limit(3)
# for order in orders:
#     for product in products:
# for (order,product) in zip(orders, products):
#         print(f"OrderId: {order.order_id} \nProductName: {product.product_name} ")


# orders = session.query(Odetails).join(Odetails.products).filter(Odetails.order_id == "AB123").limit(3)
# products = session.query(Product).join(Product.orders).filter(Odetails.order_id == "AB123").limit(3)
# for (order, product) in zip(orders, products):
#                hi = (f"OrderId: {order.order_id} \nProductName: {product.product_name} \nRate: {product.rate} \nQuantity: {order.quantity} \nAmount: {order.amount}\n")
#                print(hi)
#
# orders = session.query(Odetails).join(Odetails.products).filter(Odetails.order_id=="AB123").with_entities(Odetails.order_id).all()
# print(orders)
# if "AB123" in orders[0]:
#     print("else")

# qry = session.query(func.sum(Odetails.amount)).filter(Odetails.order_id=="AB123").first()

# sum = session.query(Odetails).with_entities(func.sum(Odetails.amount)).filter(Odetails.order_id=="AB123").scalar()
# print(sum)
# print([x.amount for x in hel])
# if "AB123" in [x.order_id for x in hel]:# if orde.order_id == "AB12":
#     print("ok")
# else:
#     print("not")


# hel = session.query(Odetails, Product).filter(Odetails.product_id == Product.product_id).filter(
#     Odetails.order_id == "AB123").limit(3)
# print([x.order_id for x, y in hel][0])




# product1 = Product(product_id=101, product_name='Red', rate=10)
# product2 = Product(product_id=102, product_name='Violet', rate=20)
# product3 = Product(product_id=103, product_name='Indigo', rate=30)
# product4 = Product(product_id=104, product_name='Blue', rate=40)
# product5 = Product(product_id=105, product_name='Green', rate=50)
# product6 = Product(product_id=106, product_name='Yellow', rate=60)
# product7 = Product(product_id=107, product_name='Orange', rate=70)
# product8 = Product(product_id=108, product_name='White', rate=80)
# product9 = Product(product_id=109, product_name='Navy', rate=90)
# product10 = Product(product_id=201, product_name='Steel', rate=100)
#
# order1 = Odetails(order_id='AB122', quantity=3, amount=90 ,orderStatus='Ordered')
# order = Odetails(order_id='AB122', quantity=3, amount=30 ,orderStatus='Ordered')
# order2 = Odetails(order_id='AB123', quantity=2, amount=60, orderStatus='Delivered')
# order3 = Odetails(order_id='AB124', quantity=4, amount=120, orderStatus='en route')
#
# product3.orders.append(order1)
# product3.orders.append(order2)
# product3.orders.append(order3)
# product1.orders.append(order)
#
# session.add_all([product1, product2, product3, product4, product5, product6, product7, product8, product9, product10])
# session.add_all([order,order3,order2,order1])
#
# session.commit()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# product1 = Product(product_id=101, product_name='Red', rate=10)
# product2 = Product(product_id=102, product_name='Violet', rate=20)
# product3 = Product(product_id=103, product_name='Indigo', rate=30)
# product4 = Product(product_id=104, product_name='Blue', rate=40)
# product5 = Product(product_id=105, product_name='Green', rate=50)
# product6 = Product(product_id=106, product_name='Yellow', rate=60)
# product7 = Product(product_id=107, product_name='Orange', rate=70)
# product8 = Product(product_id=108, product_name='White', rate=80)
# product9 = Product(product_id=109, product_name='Navy', rate=90)
# product10 = Product(product_id=201, product_name='Steel', rate=100)
#
# order1 = Odetails(order_id='AB122', quantity=3, orderStatus='Ordered')
# order2 = Odetails(order_id='AB123', quantity=2, orderStatus='Delivered')
# order3 = Odetails(order_id='AB124', quantity=4, orderStatus='en route')

# product1.orders = [order1, order2, order3]
# product3.orders = [order1, order2, order3]
# product5.orders = [order1, order2, order3]
# product7.orders = [order1, order2, order3]
# product9.orders = [order1, order2, order3]

# product2.orders = [order1, order2, order3]
# product4.orders = [order1, order2, order3]
# product6.orders = [order1, order2, order3]
# product8.orders = [order1, order2, order3]
# product10.orders = [order1, order2, order3]
#
# session.add_all([product1,product3,product5,product7,product9])
# session.add_all([product1, product2, product3, product4, product5, product6, product7, product8, product9, product10])
# session.commit()

# session.add(product1)
# session.commit()



# order1 = Odetails(order_id=122, products=,quantity=3,orderStatus='Ordered')
# order2 = Odetails(order_id=122, products=product2,quantity=4,orderStatus='Ordered')
# order3 = Odetails(order_id=122, products=product3,quantity=5,orderStatus='Ordered')
# order4 = Odetails(order_id=122, products=product4,quantity=6,orderStatus='Ordered')
# order5 = Odetails(order_id=122, products=product5,quantity=7,orderStatus='Ordered')
# order6 = Odetails(order_id=122, products=product6,quantity=8,orderStatus='Ordered')
# order7 = Odetails(order_id=122, products=product7,quantity=3,orderStatus='Ordered')


# order2 = [Odetails(order_id=123,products=101,quantity=1,orderStatus='Delivered'),
#   Odetails(order_id=123,products=102,quantity=2,orderStatus='Delivered'),
#   Odetails(order_id=123,products=103,quantity=2,orderStatus='Delivered'),
#   Odetails(order_id=123,products=104,quantity=1,orderStatus='Delivered')]

# order3 = [Odetails(order_id=124,products=101,quantity=3,orderStatus='enroute'),
#   Odetails(order_id=124,products=102,quantity=5,orderStatus='enroute'),
#   Odetails(order_id=124,products=103,quantity=3,orderStatus='enroute'),
#   Odetails(order_id=124,products=104,quantity=3,orderStatus='enroute'),
#   Odetails(order_id=124,products=105,quantity=3,orderStatus='enroute'),
#   Odetails(order_id=124,products=106,quantity=2,orderStatus='enroute'),
#   Odetails(order_id=124,products=107,quantity=3,orderStatus='enroute')]


# order = Odetails(order_id=122,product_id=101,quantity=3,rate=10,orderStatus='Ordered')
# session.add(order)
# session.commit()
# print(order.amount)
