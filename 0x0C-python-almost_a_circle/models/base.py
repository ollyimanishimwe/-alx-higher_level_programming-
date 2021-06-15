#!/usr/bin/python3
"""Module containing Base class"""


import json
import os.path
import turtle


class Base:
    """Base class for other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init method for Base class
        Args:
            id (int): ID of the created object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """Method to return a decoded JSON string"""

        if json_string is None or len(json_string) < 1:
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw shapes using turtle module"""

        turtle.setheading(0)
        turtle.penup()
        for obj in list_rectangles + list_squares:
            turtle.setposition(obj.x, obj.y)
            turtle.begin_fill()
            turtle.forward(obj.width)
            turtle.left(90)
            turtle.forward(obj.height)
            turtle.left(90)
            turtle.forward(obj.width)
            turtle.left(90)
            turtle.forward(obj.height)
            turtle.left(90)
            turtle.end_fill()

    @classmethod
    def create(cls, **dictionary):
        """Method to raeturn a new instance of a
        class from an attribute dictionary
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """method to load a list of instances from a JSON file"""

        if not os.path.exists(cls.__name__ + '.json'):
            return []
        with open(cls.__name__ + '.json', 'rt') as file:
            objects = cls.from_json_string(file.read())
        return [cls.create(**d) for d in objects]

    @classmethod
    def save_to_file(cls, list_objs):
        """Method to save a JSON sting to a file"""

        if list_objs is None:
            list_objs = []
        list_objs = [b.to_dictionary() for b in list_objs]
        list_objs = cls.to_json_string(list_objs)
        with open(cls.__name__ + ".json", "wt") as myFile:
            myFile.write(list_objs)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of 'list_dictionaries
        Args:
            list_dictionaries: A list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        else:
            return json.dumps(list_dictionaries)