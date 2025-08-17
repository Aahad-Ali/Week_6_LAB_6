from canvas import Canvas
from pen import Pen
from turtle_engine import Turtle
from parser import CommandParser



class Controller:
    """Controller class to manage the turtle graphics commands."""
    def __init__(self) -> None:
        self.canvas = Canvas(600,600)
        self.pen = Pen(self.canvas)
        self.turtle = Turtle(self.pen)
        self.parser = CommandParser(self.turtle)
        
        
    def execute_commands(self, program: str) -> None:
        """Parse and execute a string of commands."""
        commands = self.parser.parse(program)
        for c in commands:
            c.execute()
            
            
    def execute_commands_animated(self, program: str, gui, delay=500):
        """Step by step execution with animation in GUI"""
        commands = self.parser.parse(program)

        def step(i=0):
            if i < len(commands):
                commands[i].execute()   # ek command run karo
                gui.redraw()            # GUI update
                gui.root.after(delay, step, i+1)  # agla step delay ke sath

        step()