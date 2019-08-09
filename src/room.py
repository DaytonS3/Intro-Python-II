# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    def __init__(self, roomname, desc, items):
        self.roomname = roomname
        self.desc = desc
        self.items = items

    def __str__(self):
        return (f"Room: {self.roomname}, Items: {self.items}")
