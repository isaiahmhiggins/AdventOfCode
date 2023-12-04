from dataclasses import dataclass

@dataclass
class Coordinate2D:
    x: int
    y: int
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Coordinate2D):
            raise RuntimeError(f"Cannot compare {__value} to a 'Coordinate2D'")
        return __value.x == self.x and __value.y == self.y
    
    def is_adjacent(self, obj: 'Coordinate2D'):
        return abs(self.x - obj.x) <= 1 and abs(self.y - obj.y) <= 1


@dataclass
class Coordinate3D:
    x: int
    y: int
    z: int
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Coordinate3D):
            raise RuntimeError(f"Cannot compare {__value} to a 'Coordinate3D'")
        return __value.x == self.x and __value.y == self.y and __value.z == self.z
    
    def is_adjacent(self, obj: 'Coordinate3D'):
        return abs(self.x - obj.x) <= 1 and abs(self.y - obj.y) <= 1 and abs(self.z - obj.z) <= 1