from point import Point
from canvas import Canvas

class Pen:
    def __init__(self, canvas: Canvas, start: Point | None = None) -> None:
        self.canvas = canvas
        self.current_position =start or Point(250, 250)

    @property
    def position(self) -> Point:
        """Return the current position of the pen."""
        return self.current_position
    
    def move_to(self, p: Point):
        """Move the pen to a new position without drawing."""
        self.current_position = p
    
    def line_to(self, p: Point):
        """Draw a line from the current position to a new position."""
        self.canvas.add_line(self.current_position, p)
        self.current_position =p