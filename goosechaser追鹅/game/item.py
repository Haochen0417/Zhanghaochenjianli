"""
TODO: Define the Item class, as described on page 12 of the assignment
description. You are allowed to change the scaffold somewhat to better suit
the needs of your program (change function parameters, etc.)

You are allowed to create as many methods as you feel are necessary.
"""

class Item:
    def __init__(self, short_name, item_name, full_desc, terror_rating,location):
        self.short_name=short_name
        self.item_name=item_name
        self.full_desc=full_desc
        self.terror_rating=terror_rating
        self.location=location
        
        """
        TODO: Constructor; instantiates an Item class. You may modify
        this constructor so that it can receive additional arguments (or
        fewer arguments).
        """

    # You can define more methods here!
