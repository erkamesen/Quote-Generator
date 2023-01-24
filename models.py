from flask_sqlalchemy import SQLAlchemy
import random


db = SQLAlchemy()



class Quotes(db.Model):
    __tablename__ = "quotes"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    author = db.Column(db.String)

    @classmethod
    def get_all_quotes(cls):
        to_json = []
        for row in db.session.query(cls).all():
            to_json.append({'text':row.text,
                            "author":row.author})
        return to_json
    
    @classmethod
    def random_quote(cls):
        quotes_list = cls.get_all_quotes()
        quote = quotes_list[random.randint(0,len(quotes_list)-1)]
        return quote