from Tkinter import *

class Mouse_event(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.pack(expand=YES , fill =BOTH)
        self.master.title("MOUSE EVENT 1")
        self.master.geometry("500x400")

        self.mouse_pst=StringVar()
        self.mouse_pst.set("MOUSE OUTSIDE WINDOW")

        self.label=Label(self, textvariable=self.mouse_pst)
        self.label.pack(side=BOTTOM)
        
        self.bind("<Enter>",self.enter_win)
        self.bind("<Leave>",self.leave_win)
        self.bind("<Button-1>",self.mouse_press)
        self.bind("<ButtonRelease-1>",self.mouse_release)
        self.bind("<B1-Motion>",self.mouse_drag)

    def enter_win(self,event):

        self.mouse_pst.set("MOUSE IS IN WINDOW")

    def leave_win(self,event):

        self.mouse_pst.set("MOUSE IS OUTSIDE WINDOW")

    def mouse_press(self,event):

        self.mouse_pst.set("MOUSE PRESSED  AT [ " + str(event.x) + "," + str(event.y) +"]")

    def mouse_release(self,event):

        self.mouse_pst.set("MOUSE RELEASED AT [ " + str(event.x) + "," + str(event.y) +"]")

    def mouse_drag(self,event):

        self.mouse_pst.set("MOUSE DRAGGED AT [ " + str(event.x) + "," + str(event.y)+"]")

Mouse_event().mainloop()
 
