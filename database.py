from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///game.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_account(name):
    account = Account(name=name)
    session.add(account)
    session.commit()

def get_all_accounts():
    account = session.query(Account).all()
    return account

#def correct_answer(question,answer):
	# if answer == :	
	# 	return "CORRECT!"
	# else:
	# 	return "WRONG!"

