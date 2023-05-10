from . import db

class BaseModel : 
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self 
    
    @staticmethod
    def roolback():
        db.session.rollback()

    @staticmethod
    def commit(): 
        db.session.commit()
        