#!/usr/bin/python3
"""
script that deletes all
a State object with a name
containing the letter 'a'
from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker)

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    delete_data = session.query(State).filter(State.name.like('%a%'))
#    print(type(delete_data))
#    print(type(delete_data.all()))
#    print("=====================")
    for elem in delete_data.all():
        session.delete(elem)

    session.commit()
    session.close()
