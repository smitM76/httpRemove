from sqlalchemy.orm import sessionmaker
from connection import engine, User
import logging

# [ Ignore byDefault ] DEBUG: Detailed information, typically of interest only when diagnosing problems.

# [ Ignore byDefault ] INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(level=logging.DEBUG, filename='test.log',
                    format='%(asctime)s:%(levelname)s:%(message)s')

Session = sessionmaker(bind=engine)


def display_data():
    session = Session()
    users = session.query(User).all()
    for user in users:
        print("user : {} || id : {}".format(user.username, user.id))
    session.close()


def insert_data():
    session = Session()
    uname = input("Enter Username : ")
    user = User()
    user.username = uname
    session.add(user)
    session.commit()
    session.close()


def update_data():
    session = Session()
    uid = input("Enter the id : ")
    u_id = '{}'.format(uid)
    u_name = input("Enter username : ")
    x = session.query(User).filter(User.id == u_id).first()
    x.username = u_name
    logging.debug(x)
    session.commit()
    session.close()


def delete_data():
    session = Session()

    uid = input("Enter Id to delete : ")
    u_id = '{}'.format(uid)
    x = session.query(User).filter(User.id == u_id). \
        delete(synchronize_session=False)
    session.commit()
    session.close()


display_data()
# update_data()
# logging.debug(update_data())
