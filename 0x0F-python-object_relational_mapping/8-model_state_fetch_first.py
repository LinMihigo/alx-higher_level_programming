#!/usr/bin/python3
""" Lists all State objects from the database """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    if session.query(State).first() is not None:
        state = session.query(State).first()
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
