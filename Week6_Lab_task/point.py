from dataclasses import dataclass

@dataclass(frozen=True)

class Point:
    
    x:int
    y:int
    def add(self,dx: int=0, dy: int=0) -> 'Point':
        """Return a new Point with the given deltas added to the current coordinates."""
        return Point(self.x + dx, self.y + dy)