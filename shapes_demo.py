import tkinter as tk
import math
import yaml
from yaml.loader import SafeLoader
#import os

#import time
#def draw_radial_menu(canvas):
#    canvas.delete("all")
#    
#    canvas.create_arc(100, 100, 300, 300, start=0, extent=90, style="arc")
#    canvas.create_arc(100, 100, 300, 300, start=90, extent=90, style="arc")
#
#    canvas.create_arc(10, 10, 200, 200, start=0, extent=90, fill="red", tag="arc1")
#    #canvas.create_arc(10, 10, 200, 200, start=90, extent=90, fill="blue", tag="arc2")
#    #canvas.create_arc(10, 10, 200, 200, start=180, extent=90, fill="green", tag="arc3")
#    #canvas.create_arc(10, 10, 200, 200, start=270, extent=90, fill="yellow", tag="arc4")
#
#    #  this should be create_oval
#    #canvas.create_arc(160, 160, 50,50, start=0, extent=359, fill="gray", tag="arc5")  
#
#    #canvas.create_arc(10, 10, 90, 90, start=0, extent=359, fill="red", tag="arc1")
#
#
#def key_press(event):
#
#
#    canvas1 = tk.Canvas(root, width=200, height=200, bd=0, relief='ridge', highlightthickness=0, bg="gray")
#    
#    canvas1.pack()
#    draw_radial_menu(canvas1)
#
#    canvas1.tag_bind("arc1", "<Button-1>", lambda event: handle_arc_click(event, "arc1"))
#    canvas1.tag_bind("arc2", "<Button-1>", lambda event: handle_arc_click(event, "arc2"))
#    canvas1.tag_bind("arc3", "<Button-1>", lambda event: handle_arc_click(event, "arc3"))
#    canvas1.tag_bind("arc4", "<Button-1>", lambda event: handle_arc_click(event, "arc4"))
#    canvas1.tag_bind("arc5", "<Button-1>", lambda event: handle_arc_click(event, "arc5"))
#
#
#
#    x = root.winfo_pointerx()
#    y = root.winfo_pointery()
#    root.geometry("+%d+%d" % (x, y))
#    key = event.char
#    print(key, 'is pressed')
#    root.deiconify()
#
#
#root = tk.Tk()
#root.withdraw()  # Hide the UI initially
#root.geometry("200x200")
#root.config(bg='gray')
#root.overrideredirect(True)
##root.attributes('-alpha',0.5)
#
#
#def handle_arc_click(event, tag):
#    print(f"Arc clicked: {tag}")
#
#    quit()
#
#
##canvas2 = tk.Canvas(root, width=300, height=300, bg="gray")
##canvas2.pack(side="right")
##draw_radial_menu(canvas2)
#
#
#root.bind("a", key_press)
#root.bind("<ButtonRelease-1>", quit)
#
#
#root.mainloop()


class menu():


    def __init__(self, data):
        self.data = data
        self.root = tk.Tk()



        self.x_origin       = 400
        self.y_origin       = 400
        #self.x_origin = self.root.winfo_pointerx()
        #self.y_origin = self.root.winfo_pointery()
        self.root.geometry("+%d+%d" % (self.x_origin, self.y_origin))

        #self.root.attributes('-alpha',0.5)




        #x = root.winfo_pointerx()
        #y = root.winfo_pointery()
        #root.geometry("+%d+%d" % (x, y))
        #key = event.char
        #print(key, 'is pressed')


        #  base colors
        #self.bg_color     = "grey"
        #self.border_color = "black"
        #self.focus_color  = "orange"
        #self.text_color   = "white"

        #  light colors
        #self.bg_color     = "#E7F2F8"
        #self.focus_color  = "#FFA384"
        #self.border_color = "#74BDCB"
        #self.text_color   = "#EFE7BC"

        #  better colors
        self.bg_color     = "#9AB1B1"
        self.focus_color  = "#B1A24F"
        self.border_color = "#3A5B66"
        self.text_color   = "#AE4D5C"
        



        self.primary_radius = 100
        self.oval_count     = len(self.data['projects'])
        #self.oval_count     = 12

        if self.oval_count < 8:
            self.primary_radius = 100
            self.oval_scale_factor = 2.5
        elif self.oval_count < 10:
            self.primary_radius = 150
            self.oval_scale_factor = 3.5
        elif self.oval_count < 12:
            self.primary_radius = 200
            self.oval_scale_factor = 4
        else:
            quit('unsupported number of items on primary ring')

        #  setup canvas
        self.canvas = tk.Canvas(self.root, width=900, height=900)
        self.canvas.pack()

        self.root.bind("q", quit)
        #self.root.bind("a", self.draw_default_view())
        #self.root.bind("<ButtonRelease-1>", quit)
        self.root.withdraw()  # Hide the UI initially

        #self.root.config(bg='gray')
        self.root.overrideredirect(True)
        self.root.deiconify()
        #self.draw_inner_oval()
        #self.draw_default_view()  #  radius and small oval size
        #self.root.config(bg = '#add123')
        self.root.wm_attributes('-transparentcolor', self.root['bg'])


        #self.root.attributes('-alpha',0.5)

        #self.draw_border()

        #def callback(event):
        #    
        #    #print ("clicked at", event.x, event.y)
        #    print ("clicked at")


        #def on_close(self):
        #    pass
        #    #self.root.destroy()
        #self.root.bind("<ButtonPress-1>", callback(self))
        #self.root.bind("<ButtonRelease-2>", on_close(self))

        #self.draw_fill()

        self.draw_default_view()
        self.root.mainloop()   # <---  must happen last in draw sequence




    def draw_inner_oval(self):
        ''' draws just the inner oval, lays on top of the border oval '''
        self.canvas.create_oval(self.x_origin - self.primary_radius, self.y_origin - self.primary_radius, self.x_origin + self.primary_radius, self.y_origin + self.primary_radius, outline="", fill=self.bg_color)



    def draw_border(self, radius, small_oval_size):
        ''' draws the initial black border around the menu '''

        self.canvas.create_oval(245, 245, 560, 560, outline="", fill=self.bg_color)

        # Calculate the origin and size of each smaller oval
        center_x = self.x_origin
        center_y = self.y_origin

        step = 360 / self.oval_count

        for i in range(self.oval_count):
            angle = i * step
            x = center_x + radius * math.cos(math.radians(angle))
            y = center_y + radius * math.sin(math.radians(angle))
            self.canvas.create_oval(x-small_oval_size, y-small_oval_size, x+small_oval_size, y+small_oval_size, outline="", fill=self.bg_color)

            secondary_center_x = x
            secondary_center_y = y
            secondary_oval_count = 5
            secondary_radius = 50           # how far from origin
            secondary_small_oval_size = 10  # diameter of oval
            secondary_step = 150 / secondary_oval_count

            #  1 = 0
            #  2 = 30
            #  3 = 50
            #  4 = 55
            #  5 = 60
            #  6 = 62
            #  7 = 65
            #  8 = 67

            for j in range(secondary_oval_count):
                #secondary_angle = (i * secondary_step + angle)
                secondary_angle = (angle - 67) + (j * secondary_step)
                x = secondary_center_x + secondary_radius * math.cos(math.radians(secondary_angle))
                y = secondary_center_y + secondary_radius * math.sin(math.radians(secondary_angle))
                self.canvas.create_oval(x-secondary_small_oval_size, y-secondary_small_oval_size, x+secondary_small_oval_size, y+secondary_small_oval_size, outline="", fill=self.bg_color)


    def draw_default_view(self):
        ''' draws the initial menu as it would look on initial open '''
        #self.draw_border(160, 50)
        self.draw_inner_oval()
        self.draw_primary_ovals(45)

    def draw_primary_ovals (self, small_oval_size ):
        ''' draws all menu ovals in primary ring with default colors '''

        # Calculate the origin and size of each smaller oval
        center_x = self.x_origin
        center_y = self.y_origin
        small_oval_size = self.primary_radius / self.oval_scale_factor
        step = 360 / self.oval_count
        for j in range(self.oval_count):
            angle = j * step
            x = center_x + self.primary_radius * math.cos(math.radians(angle))
            y = center_y + self.primary_radius * math.sin(math.radians(angle))
            oval = self.canvas.create_oval(x-small_oval_size, y-small_oval_size, x+small_oval_size, y+small_oval_size,
                                            outline="",
                                            fill=self.border_color,
                                            activefill=self.focus_color,
                                            #activeoutline="black",
                                            #activedash=(5, 1, 2, 1),
                                            tags=f'primary_oval{j}'
                                            )

            #  might use the later
            #self.canvas.tag_bind(f'primary_oval{i}', '<Enter>', lambda event, oval=oval: self.change_color_on_enter(event, oval))
            #self.canvas.tag_bind(f'primary_oval{i}', '<Leave>', lambda event, oval=oval: self.change_color_back_on_leave(event, oval))

            self.canvas.tag_bind(f'primary_oval{j}', "<Button-1>", lambda event, oval=oval: self.handle_primmary_oval_click(event, oval))
            self.canvas.create_text(x, y, fill=self.text_color, state=tk.DISABLED, font="Times 16 bold", text=self.data['projects'][j]['name'][0:3]) #
    
    #def change_color_on_enter(self, event, oval):
    #    self.canvas.itemconfigure(oval, fill=self.focus_color)
    #    #self.canvas.create_oval(50, 50, 355, 355, outline="", fill="grey")

    #def change_color_back_on_leave(self, event, oval):
    #    self.canvas.itemconfigure(oval, fill=self.bg_color)

    def handle_primmary_oval_click(self, event, tag):
        print(f"oval clicked: {tag}")

    #def draw_fill(self):
    #    self.draw_opening_box ( 50, 355, 155, "grey",  40) 


    
    
    


def main():

    from pathlib import Path
    p = Path(__file__).with_name('projects.yml')
    with p.open('r') as f:
        #print(f.read())
        data = yaml.load(f, Loader=SafeLoader)
    #with open(os.path.join(__location__, 'projects.yml') as f:
    #    data = yaml.load(f, Loader=SafeLoader)


    ui = menu(data)


    root = tk.Tk()
    #root.geometry("+%d+%d" % (x_origin, y_origin))
    root.bind("q", quit)
    root.withdraw()  # Hide the UI initially
    root.overrideredirect(True)
    root.deiconify()
    root.wm_attributes('-transparentcolor', root['bg'])


    def hotkey_pressed(event):


        x = root.winfo_pointerx()
        y = root.winfo_pointery()
        abs_coord_x = root.winfo_pointerx() - root.winfo_vrootx()
        abs_coord_y = root.winfo_pointery() - root.winfo_vrooty()

        x, y = event.x, event.y
        print('{}, {}'.format(x, y))
        ui = menu(data, x, y)

    def hotkey_released(event):
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))

    root.bind("<ButtonPress-1>",   hotkey_pressed(event))
    root.bind("<ButtonRelease-2>", hotkey_released(event))
    root.mainloop()   # <---  must happen last in draw sequence

    

    quit()
    


if __name__ == "__main__":
    

    main()
