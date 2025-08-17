from abc import ABC, abstractmethod
from turtle_engine import Turtle


class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    
class ForwardCmd(Command):
    def __init__(self,turtle: Turtle) -> None:
        self.turtle = turtle
    def execute(self) -> None:
        self.turtle.move_forward()
        
        
class TurnLeftCmd(Command):
    def __init__(self,turtle: Turtle) -> None:
        self.turtle = turtle
    def execute(self) -> None:
        self.turtle.move_left()
        
        
        
class TurnRightCmd(Command):
    def __init__(self,turtle: Turtle) -> None:
        self.turtle = turtle
    def execute(self) -> None:
        self.turtle.move_right()