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
    species="dog",
    photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUgAl9v10uxW9vtvsXiBHs4BbpcN6YoV-_8w&usqp=CAU",
    age=3,
    notes="Super fluffy!  Loves cuddles!")

p2 = Pet(name="Sherlock",
    species="cat",
    photo_url="https://ih1.redbubble.net/image.2029468953.0653/flat,128x,075,f-pad,128x128,f8f8f8.jpg",
    age=1,
    notes="Looks always confused, but is actually very smart")

p3 = Pet(name="Bella",
    species="dog",
    photo_url="https://pbs.twimg.com/profile_images/589457287036538881/jgw-Ofws_400x400.jpg",
    age=4,
    notes="Great with kids")

p4 = Pet(name="Dane",
    species="dog",
    photo_url="https://styles.redditmedia.com/t5_2ks0l6/styles/communityIcon_55iharf09us41.png",
    age=3,
    notes="Gentle as can be!")

p5 = Pet(name="Mena",
    species="dog",
    photo_url="https://cdn130.picsart.com/340659206033201.jpg?type=webp&to=crop&r=256",
    age=2,
    notes="Look at that smile!")

db.session.add_all([p1, p2, p3])
db.session.commit()