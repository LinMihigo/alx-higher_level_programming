#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    Rectangle.save_to_file([Rectangle(1, 2)])

    with open("Rectangle.json", "r") as file:
        print(file.read())
