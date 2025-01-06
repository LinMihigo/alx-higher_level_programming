#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(argv[0]))
        exit(1)

    username, password, db_name = argv[1], argv[2], argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id, City.id).all()

    for state in states:
        for city in state.cities:
            print(f"{state.id}: {state.name} -> {city.id}: {city.name}")

    session.close()
