import math
from point import Point
from pen import Pen
from strategy import TurnStrategy, StepStrategy, RightAngleStrategy, FixedStepStrategy


class Turtle:
    def __init__(self,pen:Pen,direction_deg:float =0.0, turn_strategy:TurnStrategy |None =None, step_strategy:StepStrategy |None =None):
        self._pen = pen
        self._dir = direction_deg
        self._turn = turn_strategy or RightAngleStrategy(90)
        self._step = step_strategy or FixedStepStrategy(50)
        
    @property
    def direction(self) -> float:
        """Return the current position of the turtle."""
        return self._dir
    
    def move_forward(self):
        dist = self._step.step()
        rad =math.radians(self._dir)
        dx =round(dist * math.cos(rad))
        dy =round(dist * math.sin(rad))
        new_p = self._pen.position.add(dx, dy)
        self._pen.line_to(new_p)
        
    def move_back(self):
        dist = self._step.step()
        rad =math.radians(self._dir)
        dx =round(-dist * math.cos(rad))
        dy =round(-dist * math.sin(rad))
        new_p = self._pen.position.add(dx, dy)
        self._pen.line_to(new_p)
        
        
    def move_left(self):
        self._dir = (self._dir + self._turn.left_angle()) % 360
        
    def move_right(self):
        self._dir = (self._dir - self._turn.right_angle()) % 360