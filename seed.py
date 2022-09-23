"""Seed file for sample data for 'adopt' project/database"""

from readline import append_history_file
from models import Pet, db
from app import app

db.drop_all()
db.create_all()

'''
p1 = Pet(name="",
    species="",
    photo_url="",
    age=,
    notes="")
'''

p1 = Pet(name="Frost",
    species="Dog",
    photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUgAl9v10uxW9vtvsXiBHs4BbpcN6YoV-_8w&usqp=CAU",
    age=3,
    notes="Super fluffy!  Loves cuddles!")

p2 = Pet(name="Sherlock",
    species="Cat",
    photo_url="https://ih1.redbubble.net/image.2029468953.0653/flat,128x,075,f-pad,128x128,f8f8f8.jpg",
    age=1,
    notes="Looks always confused, but is actually very smart")

p3 = Pet(name="Bella",
    species="Dog",
    photo_url="https://pbs.twimg.com/profile_images/589457287036538881/jgw-Ofws_400x400.jpg",
    age=4,
    notes="Great with kids")

db.session.add_all([p1, p2, p3])
db.session.commit()