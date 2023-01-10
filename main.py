import os
import pandas as pd
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from fastapi import FastAPI, Depends, Form, Response
from models import Product,Odetails, engine
from database import session
from sqlalchemy.orm import Session
from sqlalchemy import exc, func


account_sid = 'ACe6db9c8721eb76dcd5e677f362653d98'
auth_token = 'd500e731a614d788d5c321168b6e1717'
client = Client(account_sid, auth_token)

ho=client.messages.create(from_="whatsapp:+14155238886", body='- give *OrderID* to show orders.\n\t- type *orderstatus* to show status\n\t- type *ALL* to show all orders\n\t- type *Invoice* to get PDF', to="whatsapp:+919941571104")

app = FastAPI()
def get_db():
    try:
        yield session
    finally:
        session.close()


@app.post("/bot")
async def chat(Body: str = Form(...)): #The (...) also called Ellipsis specifies that From and Body don’t have a default parameter.
    global order, product, sum
    user = Body.lower()
    response = MessagingResponse()
    msg = response.message()

    # orde = session.query(Odetails).join(Odetails.products).with_entities(Odetails.order_id).all()
    # print(len(orde[0][0]))
    # print(len(user))
    # orderID = orde[0][0]
    # if len(user) == len(orde[0][0]):
    # print(orde.order_id)

    # print([x.order_id for x in hel])
    # try:
    hel = session.query(Odetails).all()
    if user in [x.order_id.lower() for x in hel] or ('orderstatus' in user or 'order status' in user) or 'all' in user or 'invoice' in user:

            # try:
        if session.query(Odetails).filter(Odetails.order_id==user).first():
            han =session.query(Odetails, Product).filter(Odetails.product_id==Product.product_id).filter(Odetails.order_id==user).limit(3)
            hey =[f"ORDER_ID \t{user.upper()}\n\n-------ORDERS-------"]
            for order, product in han:
                # newline =  '\n'
                he = (f"orderID: {order.order_id} \nProductName: {product.product_name} \nRate: {product.rate} \nQuantity: {order.quantity} \nAmount: {order.amount}")
                hey.append(he)
            msg.body('\n\n'.join(hey))

        elif ('orderstatus' in user or 'order status' in user) :
            try:
                han = session.query(Odetails, Product).filter(Odetails.product_id==Product.product_id).filter(Odetails.order_id==order.order_id).limit(3)
                hi =[f"ORDER_ID \t{order.order_id}\n\n-------ORDERS-------"]
                for order, product in han :
                    he = (f"ProductName: {product.product_name} \nOrderStatus: {order.orderStatus}")
                    hi.append(he)
                msg.body('\n\n'.join(hi))
            except:
                msg.body('Mention "orderID" to get details')

        elif "all" in user:
            try:
                han = session.query(Odetails, Product).filter(Odetails.product_id==Product.product_id).filter(Odetails.order_id==order.order_id).all()
                sum = session.query(Odetails).with_entities(func.sum(Odetails.amount)).filter(Odetails.order_id ==order.order_id).scalar()
                hi =[f"ORDER_ID \t{order.order_id}\n\n-------ORDERS-------\nTotal Amount = ₹{sum}"]
                for order, product in han :
                   he = (f"ProductName: {product.product_name} \nRate: {product.rate} \nQuantity: {order.quantity} \nAmount: {order.amount}")
                   hi.append(he)
                msg.body('\n\n'.join(hi))
            except:
                msg.body('Mention "orderID" to get details')

        elif "invoice" in user:
            try:
                if order.order_id:
                    msg.media("https://ideassion.com/wp-content/uploads/2022/10/faq.xlsx")
            except:
                msg.body('Mention "orderID" to get details')

    else:
        msg.body('Mention "orderID" to get details')

    return Response(content=str(response), media_type="application/xml")


# \nproductName: {product.product_name} \nQuantity: {product.orders}


























