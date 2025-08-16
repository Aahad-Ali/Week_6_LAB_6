from abc import ABC, abstractmethod


class TurnStrategy(ABC):
    @abstractmethod
    def left_angle(self) -> float: ...
    
    @abstractmethod
    def right_angle(self) -> float: ...
    
    
class RightAngleStrategy(TurnStrategy):
    def __init__(self,angle:float = 90.0):
        self.a = angle
        
    def left_angle(self) -> float:
        return self._a
    
    def right_angle(self) -> float:
        return self._a

class StepStrategy(ABC):
    def step(self) -> int: ...