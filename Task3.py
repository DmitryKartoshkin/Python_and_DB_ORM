import sqlalchemy
from sqlalchemy.orm import sessionmaker

import json

from Models1 import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:dima1983@localhost:5432/homework'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open("tests_data.json", encoding="utf-8") as f:
    json_data = json.load(f)

for i in json_data:
    # print(i['model'])
    if i['model'] == 'publisher':
        publisher = Publisher(id = i['pk'], title=i['fields']['name'])
        session.add(publisher)
        session.commit()

    elif i['model'] == 'book':
        book = Book(id = i['pk'], name = i['fields']['title'],
        id_publisher = i['fields']['id_publisher'])
        session.add(book)
        session.commit()

    elif i['model'] == 'shop':
        shop = Shop(id = i['pk'], name = i['fields']['name'])
        session.add(shop)
        session.commit()

    elif i['model'] == 'stock':
        stock = Stock(id=i['pk'], count = i['fields']['count'],
        id_book = i['fields']['id_book'], id_shop = i['fields']['id_shop'])
        session.add(stock)
        session.commit()

    elif i['model'] == 'sale':
        sale = Sale(id=i['pk'], price = i['fields']['price'],
        count = i['fields']['count'],
        date_sale = i['fields']['date_sale'],
        id_stock = i['fields']['id_stock'])
        session.add(sale)
        session.commit()

session.close
