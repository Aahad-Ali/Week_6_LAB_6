from typing import List
from turtle_engine import Turtle
from commands import Command, ForwardCmd, TurnLeftCmd, TurnRightCmd

class CommandParser:
    def __init__(self, turtle: Turtle) -> None:
        self.turtle = turtle

    def parse(self, text: str) -> List[Command]:
        cmds: List[Command] = []
        for ch in text.replace(" ", ""):
            if ch == "F":
                cmds.append(ForwardCmd(self.turtle))
            elif ch == "+":   # plus means turn right
                cmds.append(TurnRightCmd(self.turtle))
            elif ch == "-":   # minus means turn left
                cmds.append(TurnLeftCmd(self.turtle))
            else:
                pass  # ignore unsupported characters
        return cmds
