from sys import path
path.append("../")

from type import Vector2

class Transform:
    def __init__(self):
        self.position: Vector2 = Vector2()
        self.rotation: Vector2 = Vector2()
        self.scale: Vector2 = Vector2()