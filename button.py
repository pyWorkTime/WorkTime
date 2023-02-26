import tkinter as tk
import math




class PrimaryButton():


    def __init__(self, data, canvas, x_origin, y_origin, radius, angle, distance_from_origin, colors, button_number) -> None:
        self.button_number  = button_number
        self.data           = data
        self.canvas         = canvas
        self.x_origin       = x_origin
        self.y_origin       = y_origin
        self.radius         = radius
        self.angle          = angle
        self.colors         = colors
        self.distance_from_origin = distance_from_origin

        self.x = self.x_origin + self.distance_from_origin * math.cos(math.radians(self.angle))
        self.y = self.y_origin + self.distance_from_origin * math.sin(math.radians(self.angle))

        self.draw_label()
        self.draw_button()

    def draw_label(self) -> None:
        ''' a label is a rectangle of a fixed length that extends from a button along the same angle from the origin.
            this rectangle is capped with an oval of the same color, then the angle is to 0, then another
            rectangle and oval is extended from this position.  The second rectangle will hold the description text.
            The length of the second rectangle depends on the length of the description text.
        '''

        #  Angle from origin, length to extend past parent button
        #x1, y1 = 50, 150  # <--  the origin
        length = 50
        angle_radians = math.radians(self.angle)
        x2 = self.x + length * math.cos(angle_radians)
        y2 = self.y + length * math.sin(angle_radians)
        
        #  second line segment that will carry a text label
        length = len(self.data['name']) * 10  #  assumes 10 pixels per character

        if self.x < self.x_origin:
            length = length * -1

        angle_radians = math.radians(0)  #  at angle 0
        x3 = x2 + length * math.cos(angle_radians)
        y3 = y2 + length * math.sin(angle_radians)
        
        #  multi-segmented line with join style of round and cap style of round
        self.label_line_id = self.canvas.create_line(self.x, self.y, x2, y2, x3, y3,
                                width=self.radius + 15,
                                state=tk.DISABLED,
                                fill=self.colors['label'],
                                joinstyle="round",
                                capstyle="round",
                                tags="primary_label")

        #  The label originates from the beginning of the second segment
        self.label_text_id = self.canvas.create_text((x2+x3)/2, y2,
                                fill=self.colors['dark_text'],
                                state=tk.DISABLED,
                                font="Times 16 bold",
                                text=self.data['name'],
                                tags="primary_label"
                                )


    def draw_button (self) -> None:
        ''' draws all menu ovals in primary ring with default colors '''


        self.oval_id = self.canvas.create_oval(
                                       self.x-self.radius,
                                       self.y-self.radius,
                                       self.x+self.radius,
                                       self.y+self.radius,
                                       outline=self.colors['bg'],
                                       width=5,
                                       fill=self.colors['button'],  
                                       #activefill=self.colors['focus'],
                                       #activeoutline="black",
                                       #activedash=(5, 1, 2, 1),
                                       tags=f'button{self.button_number}'
                                       )

        self.canvas.create_text(self.x,
                                self.y,
                                fill=self.colors['text'],
                                state=tk.DISABLED,
                                font="Times 16 bold",
                                text=self.data['name'][0:3]
                                )

        #####  might use this later
        ####self.canvas.tag_bind(f'button{j}', '<Enter>', lambda event, oval=self.oval: self.button_on_enter(event, oval))
        ####self.canvas.tag_bind(f'button{j}', '<Leave>', lambda event, oval=self.oval: self.button_on_leave(event, oval))
        ####self.canvas.tag_bind(f'button{j}', "<Button-1>", lambda event, oval=self.oval: self.handle_button_click(event, oval))
        ####self.canvas.create_text(x, y, fill=self.colors['text'], state=tk.DISABLED, font="Times 16 bold", text=self.data['projects'][j]['name'][0:3]) #

     #  these are handled on parent object - unable to get them to work correctly here
#    def button_on_enter(self, event, oval):
#        self.canvas.itemconfigure(oval, fill=self.colors['focus'])
#        self.canvas.itemconfigure('primary_label', state='hidden')
#        #self.canvas.create_oval(50, 50, 355, 355, outline="", fill="grey")
#
#    def button_on_leave(self, event, oval):
#        self.canvas.itemconfigure(oval, fill=self.colors['button'])
#        #self.canvas.itemconfigure('primary_label', state='normal')
#        self.canvas.itemconfigure('primary_label', state='disabled')
#        #self.canvas.itemconfigure('primary_label', tk.DISABLED)
#
#
#    def handle_button_click(self, oval_id, event):
#        print(f"button clicked: {self.oval_id} - {self.data['name']}")