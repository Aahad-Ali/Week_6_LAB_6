from typing import List
from line import Line
from point import Point


class Canvas:
    def __init__(self, width: int=500, height: int=500) -> None:
        self.width = width
        self.height = height
        self._lines: List[Line] = []   #private attribute
        
        
    def add_line(self, start: Point, end: Point):
        """Add a line defined by start and end points to the canvas."""
        line = Line(start=start, end=end)
        self.lines.append(line)
        
    @property
    def lines(self) -> List[Line]:
        """Return the list of lines on the canvas."""
        return self._lines
    
    def debug_print(self):
        """Print the lines in the canvas for debugging purposes."""
        for i, ln in enumerate(self._lines,1):
            print(f"{i:02d}. {ln.start} -> {ln.end}")
    
    def clear(self):
        self._lines.clear()
        