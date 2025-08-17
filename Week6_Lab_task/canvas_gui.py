import tkinter as tk
from canvas import Canvas
import random

class CanvasGUI:
    def __init__(self, canvas: Canvas, width=600, height=600):
        self._canvas_model = canvas  # logical canvas (our own)
        self.root = tk.Tk()          # sirf yahin ek Tk()
        self.root.title("Turtle Final Drawing")
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack(fill="both", expand=True)

    def redraw(self):
        """Redraw all lines from the model on the Tkinter canvas."""
        self.canvas.delete("all")
        for line in self._canvas_model.lines:
            self.canvas.create_line(
            line.start.x, line.start.y,
            line.end.x, line.end.y,
            fill=(["red", "blue", "green", "black"][random.randint(0, 3)]), width=2
            )
        if self._canvas_model.lines:
            last=self._canvas_model.lines[-1].end
            self.canvas.create_oval(last.x-2, last.y-2, last.x+2, last.y+2, fill="red")

    def show(self):
        """Run the Tkinter main loop."""
        self.root.mainloop()
