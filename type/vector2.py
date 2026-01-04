class Vector2:
    def __init__(self, x: int | float = 0, y: int | float = 0):
        self.x: int | float = x
        self.y: int | float = y

    def SetTo(self, newX: int | float, newY: int | float):
        return Vector2(newX, newY)
    
    def MoveTo(self, origin, newPosition, speed: int | float):
        return Vector2(
            origin.x + speed * (1 if newPosition.x > origin.x else -1),
            origin.y + speed * (1 if newPosition.y > origin.y else -1)
        )
    
    def Lerp(self, origin, newPosition, speed: int | float):
        return Vector2(
            origin.x + speed * (newPosition.x - origin.x),
            origin.y + speed * (newPosition.y - origin.y),
        )