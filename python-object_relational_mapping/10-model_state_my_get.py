#!/usr/bin/python3
"""
lists all State objects that contain 
the letter a from the
database hbtn_0e_6_usa
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
    state_table = Session().query(State)\
        .filter(State.name == sys.argv[4]).count()
    if stable_table == 0:
        print("Not found")
    else:
        for state in Session().query(State).filter_by(name=sys.argv[4]):
            print("{}".format(state.id))
    Session().close()
