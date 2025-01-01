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

    add_lou = State(name='Louisiana')
    session.add(add_lou)
    session.commit()
    print(session.query(State).filter(State.name == 'Louisiana').first().id)
    session.close()
