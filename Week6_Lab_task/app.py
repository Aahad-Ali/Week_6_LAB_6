from controller import Controller
from canvas_gui import CanvasGUI
import tkinter as tk



class App:
    """Main application class to run the turtle graphics."""
    
    def run(self)->None:
        ctl = Controller()
        gui = CanvasGUI(ctl.canvas)
        ctl.execute_commands_animated("F+F+F+F", gui, delay=300)
        
        #input box for user commands
        entry=tk.Entry(gui.root)
        entry.pack()
            
        def run_user_input():
            text = entry.get()
            ctl.execute_commands_animated(text,gui,delay=500)  # Execute user input commands
        
        
        button = tk.Button(gui.root, text="Run", command=run_user_input)
        button.pack()
        
        gui.show()
        
        
        
        btn_square = tk.Button(gui.root, text="Square", command=lambda: ctl.execute_commands_animated("F-F-F-F", gui))
        btn_square.pack()

        btn_triangle = tk.Button(gui.root, text="Triangle", command=lambda: ctl.execute_commands_animated("F-F-F", gui))
        btn_triangle.pack()
        #example
        
        # ctl.execute_commands("-F-F-F-F+")  Another example
        # ctl.execute_commands("F-F-F-F")   # Move forward 4 times
        # ctl.execute_commands("F-F-F")   # Move forward 3 times
        # ctl.execute_commands("F+F-F+F") #zig-zag pattern

        # ctl.debug_dump()
        
        


# # =============================================  Animation Version  =============================================

# from controller import Controller
# from canvas_gui import CanvasGUI
# import tkinter as tk

# class App:
#     """Main application class with animation."""
    
#     def run(self) -> None:
#         self.ctl = Controller()
#         self.gui = CanvasGUI(self.ctl.canvas)
        
#         # Program (Square Example)
#         self.program = "F-F-F-F"
#         self.commands = self.ctl.parser.parse(self.program)
        
#         # Create main window
#         self.root = tk.Tk()
#         self.root.title("Turtle Animation Drawing")
        
#         # Put canvas in window
#         self.gui.root_canvas.pack(fill="both", expand=True)
        
#         # Start animation
#         self.current_index = 0
#         self.animate()
        
#         self.root.mainloop()

#     def animate(self):
#         """Execute one command at a time with delay."""
#         if self.current_index < len(self.commands):
#             cmd = self.commands[self.current_index]
#             cmd.execute()
#             self.gui.redraw()   # refresh screen
#             self.current_index += 1
#             self.root.after(500, self.animate)  # 500ms delay between steps
