
import tkinter as tk
import math
import re    # for working with hex color codes
import time
from button import PrimaryButton
from arc    import PrimaryArc


class menu():


    def __init__(self,  data) -> None:
        

        self.data = data
        self.root = tk.Tk()
        self.set_root_properties()
        self.x_origin, self.y_origin = self.root.winfo_pointerxy()

        #  default colors
        self.colors = {
        'bg'       : "#656565",
        'focus'    : "#D55A00",
        'button'   : "#000000",
        'text'     : "#989898",
        'label'    : "#BABABA",
        'dark_text': "#323232",
        }


        #self.oval_count     = 12
            #inner circle is medium gray background, black buttons, dark grey text, light label streaks with black text on the streak
            #
            #on primary highlight the primary labels and text disappear, the selected circle is highlighted, primary circle text lights up as white, a sub-coral appears
            #
            #sub coral is surrounded by a medium-light gray, has black buttons with dark grey text, light label streaks with black text on the streak
            ##000000   <-- darkest
            ##323232
            ##656565
            ##989898
            ##BABABA
            ##DEDEDE    <-- lightest


        #  setup canvas
        self.canvas = tk.Canvas(self.root, width=900, height=900)
        self.canvas.pack(fill=tk.BOTH, expand=True)


        
        ###########  establish primary buttons and labels



        #  calculate the angle of each button around the circumference
        self.oval_count = len(self.data['projects'])
        self.step = 360 / self.oval_count


        if self.oval_count < 8:
            self.primary_radius = 60
            self.oval_scale_factor = 2.5
        elif self.oval_count < 10:
            self.primary_radius = 70
            self.oval_scale_factor = 3
        elif self.oval_count < 12:
            self.primary_radius = 150
            self.oval_scale_factor = 4
        else:
            quit('unsupported number of items on primary ring')

        #  this is the base background and primary circle buttons
        self.draw_default_view()

        #  to be populated with primary button objects
        self.buttons        = []

        for button_number, project in enumerate(self.data['projects']):
            
            #  basic math for this button
            angle = (button_number * self.step) + (self.step // 2)   #  prevents buttons from forming directly at 0, 90, 120, and 180 markers
 
            #  x,y here represent the center of this button
            x = self.x_origin + self.primary_radius * math.cos(math.radians(angle))
            y = self.y_origin + self.primary_radius * math.sin(math.radians(angle))

            radian_start = angle - (self.step // 2)  #  for future use
            radian_end   = angle + (self.step // 2)  #  for future use

            radius = self.primary_radius / self.oval_scale_factor
            self.buttons.append(PrimaryButton(project,
                                              self.canvas,
                                              self.x_origin,
                                              self.y_origin,
                                              radius,
                                              angle,
                                              self.primary_radius,
                                              self.colors,
                                              button_number
                                              )
                                )

            #  functions are handled in the parent class
            self.canvas.tag_bind(f'button{button_number}', '<Enter>',   
                                   lambda event, project=self.buttons[button_number].data, oval=self.buttons[button_number].oval_id:
                                   self.button_on_enter(event, project, oval)        
                                )

            self.canvas.tag_bind(f'button{button_number}', '<Leave>',   
                                   lambda event, project=self.buttons[button_number].data, oval=self.buttons[button_number].oval_id:
                                   self.button_on_leave(event, project, oval)        
                                )

            self.canvas.tag_bind(f'button{button_number}', '<Button-1>',
                                   lambda event, project=self.buttons[button_number].data, oval=self.buttons[button_number].oval_id:
                                   self.handle_button_click(event, project, oval)    
                                )



            




            '''
            num_circles = 3
            circle_radius = radius
            
            
            #  This formula establishes the relation between radius of big circle R,
            #    radius of small circle r and number of (touching) small circles N.
            #    We will need to find R to calculate how much space we need on our arc
            #    in order to fit all the buttons
            #  R = r / Sin(Pi/N)
            radius_container = (circle_radius) / math.sin(math.pi / num_circles)
            
            #  Now turn the radius into the circumfrence
            circumfrence_container = ((math.pi * radius_container) * 2) * 0.9
            
            #  Now that we have the circumfrence, we need to project that onto an arc
            #    To do this we need to find the angle of that arc which will produce
            #    an equal size to the circumference we found above which will fit
            #    all the child circles (buttons)
            ###################
            #  The formula:
            #  L = r * θ
            ###################
            #  Hence, the arc length is equal to radius multiplied by the central angle, θ (in radians).
            #  Arc Length = r x θ
            #  Arc Length / r = θ
            #  θ = Arc Length / r
            
            #  Calculate the angles for the start and end points of the arc
            radian_start = angle - (65)
            radian_end   = (angle + 65) % 360

            start_angle = radian_start
            end_angle = radian_end
            arc_radius = 100  #  start small, increase until we can fit all buttons

            #  If the angle required to produce the arc of necessary size is bigger than 120
            #    then we can slowly begin to increase the size of the radius
            #    This will guarantee that we will never have an arc greater than 120 degrees
            arc_angle = math.degrees(circumfrence_container / arc_radius)

            while arc_angle > 120:
                
                print("loop", arc_angle)
                time.sleep(1)
                arc_radius = arc_radius + 5
                #  the answer here is in radians, it needs to be in degrees
                arc_angle = start_angle + math.degrees(circumfrence_container / arc_radius) #  θ = Arc Length / r

            total_degrees = end_angle - start_angle
            center_x = x
            center_y = y

            #  Draw the arc using the create_arc method
            self.canvas.create_arc(center_x-arc_radius, center_y-arc_radius, center_x+arc_radius, center_y+arc_radius, start=start_angle, extent=end_angle-start_angle)
            
            #  Draw the buttons using the create_oval method
            step = total_degrees / (num_circles - 1)
            for i in range(num_circles):
                #angle = (i * total_degrees / num_circles) + start_angle
                angle = start_angle + (i * step)
                x = center_x + arc_radius * math.cos(math.radians(angle))
                y = center_y - arc_radius * math.sin(math.radians(angle))
                self.canvas.create_oval(x-circle_radius, y-circle_radius, x+circle_radius, y+circle_radius, fill='red')
            '''

            #                                tags="secondary_arc",
#                                fill=self.colors['text'],
#                                state=tk.HIDDEN,
#                                fill='grey'
#            radius = self.primary_radius / self.oval_scale_factor
#            self.buttons.append(PrimaryButton(project,
#                                              self.canvas,
#                                              self.x_origin,
#                                              self.y_origin,
#                                              radius,
#                                              angle,
#                                              self.primary_radius,
#                                              self.colors,
#                                              button_number
#                                              )
#                                )
#
#            #  functions are handled in the parent class
#            self.canvas.tag_bind(f'button{button_number}', '<Enter>',    lambda event, project=self.buttons[button_number].data, oval=self.buttons[button_number].oval_id: self.button_on_enter(event, project, oval)        )
#            self.canvas.tag_bind(f'button{button_number}', '<Leave>',    lambda event, project=self.buttons[button_number].data, oval=self.buttons[button_number].oval_id: self.button_on_leave(event, project, oval)        )
#            self.canvas.tag_bind(f'button{button_number}', '<Button-1>', lambda event, project=self.buttons[button_number].data, oval=self.buttons[button_number].oval_id: self.handle_button_click(event, project, oval)    )





        #self.draw_default_buttons()

        self.open_ui()



    def draw_default_view(self) -> None:
        ''' draws the initial menu as it would look on initial open '''

        #self.draw_border()
        self.draw_inner_oval()



#    def draw_default_buttons(self):
#        ''' draws X number of primary buttons based on contents of the input .yml file '''
#        self.draw_button()




    #def draw_label(self, x1, y1):
    #    ''' a label is a rectangle of a fixed length that extends from a button along the same angle from the origin.
    #        this rectangle is capped with an oval of the same color, then the angle is to 0, then another
    #        rectangle and oval is extended from this position.  The second rectangle will hold the description text.
    #        The length of the second rectangle depends on the length of the description text.
    #    '''

    #    #  Angle from origin, length to extend past parent button
    #    x1, y1 = 50, 150  # <--  the origin
    #    length = 60
    #    angle = 75
    #    angle_radians = math.radians(angle)
    #    x2 = x1 + length * math.cos(angle_radians)
    #    y2 = y1 + length * math.sin(angle_radians)
    #    
    #    #  second line segment that will carry a text label
    #    length = 200
    #    angle = 0
    #    angle_radians = math.radians(angle)
    #    x3 = x2 + length * math.cos(angle_radians)
    #    y3 = y2 + length * math.sin(angle_radians)
    #    
    #    # multi-segmented line with join style of round and cap style of round
    #    self.canvas.create_line(x1, y1, x2, y2, x3, y3,
    #                            width=self.primary_radius,
    #                            state=tk.DISABLED,
    #                            fill='#BABABA',
    #                            joinstyle="round",
    #                            capstyle="round")

    #    #  The label originates from the beginning of the second segment
    #    self.canvas.create_text((x2+x3)/2, y2,
    #                            fill="white",
    #                            state=tk.DISABLED,
    #                            font="Times 16 bold",
    #                            text=self.data['projects'][j]['name'])



    def open_ui(self) -> None:
        '''  draw main ui component '''
        self.root.mainloop()   # <---  must happen last in draw sequence



    def draw_inner_oval(self) -> None:
        ''' draws just the inner oval, everything else lays on top of this '''


        self.main_oval_id = self.canvas.create_oval(self.x_origin - self.primary_radius,  #  top left x position
                                self.y_origin - self.primary_radius,  #  top left y position
                                self.x_origin + self.primary_radius,  #  bottom right x position
                                self.y_origin + self.primary_radius,  #  bottom right y position
                                outline=self.colors['bg'],
                                width=15,
                                #outline="",
                                fill=self.colors['bg'])


#    def draw_border(self) -> None:
#        ''' draws the initial border around the menu '''
#
#
#        for i in range(self.oval_count):
#            angle = i * self.step
#            x = self.x_origin + self.primary_radius * math.cos(math.radians(angle))
#            y = self.y_origin + self.primary_radius * math.sin(math.radians(angle))
#            self.canvas.create_oval(x-self.small_oval_size,
#                                    y-self.small_oval_size,
#                                    x+self.small_oval_size,
#                                    y+self.small_oval_size,
#                                    outline="",
#                                    fill=self.colors['bg'])
#            
#
#            #  this is junk code that might be used later to add extra circles for hints about sub menus, for now this is not needed
#            #####secondary_center_x = x
#            #####secondary_center_y = y
#            #####secondary_oval_count = 5
#            #####secondary_radius = self.primary_radius       # how far from origin
#            #####secondary_small_oval_size = 5  # diameter of oval
#            #####secondary_step = 150 / secondary_oval_count
#            ######  1 = 0
#            ######  2 = 30
#            ######  3 = 50
#            ######  4 = 55
#            ######  5 = 60
#            ######  6 = 62
#            ######  7 = 65
#            ######  8 = 67
#            #####for j in range(secondary_oval_count):
#            #####    #secondary_angle = (i * secondary_step + angle)
#            #####    secondary_angle = (angle - 67) + (j * secondary_step)
#            #####    x = secondary_center_x + secondary_radius * math.cos(math.radians(secondary_angle))
#            #####    y = secondary_center_y + secondary_radius * math.sin(math.radians(secondary_angle))
#            #####    self.canvas.create_oval(x-secondary_small_oval_size, y-secondary_small_oval_size, x+secondary_small_oval_size, y+secondary_small_oval_size, outline="", fill=self.colors['bg'])




#    def draw_button (self) -> None:
#        ''' draws all menu ovals in primary ring with default colors '''
#
#        for j in range(self.oval_count):
#            angle = j * self.step
#            x = self.x_origin + self.primary_radius * math.cos(math.radians(angle))
#            y = self.y_origin + self.primary_radius * math.sin(math.radians(angle))
#            oval = self.canvas.create_oval(x-self.small_oval_size,
#                                           y-self.small_oval_size,
#                                           x+self.small_oval_size,
#                                           y+self.small_oval_size,
#                                           outline=self.colors['bg'],
#                                           width=10,
#                                           fill=self.colors['button'],
#                                           activefill=self.colors['focus'],
#                                           #activeoutline="black",
#                                           #activedash=(5, 1, 2, 1),
#                                           tags=f'button{j}'
#                                           )
#
#            #  might use this later
#            self.canvas.tag_bind(f'button{j}', '<Enter>', lambda event, oval=oval: self.button_on_enter(event, oval))
#            self.canvas.tag_bind(f'button{j}', '<Leave>', lambda event, oval=oval: self.button_on_leave(event, oval))
#            self.canvas.tag_bind(f'button{j}', "<Button-1>", lambda event, oval=oval: self.handle_button_click(event, oval))
#            self.canvas.create_text(x, y, fill=self.colors['text'], state=tk.DISABLED, font="Times 16 bold", text=self.data['projects'][j]['name'][0:3]) #
    



    def button_on_enter(self, event, project, oval_id) -> None:
        print(f"ENTERED OBJECT ID {oval_id}")
        self.canvas.itemconfigure(oval_id, fill=self.colors['focus'])

        #  all primary labels hide
        self.canvas.itemconfigure('primary_label', state='hidden')


    def button_on_leave(self, event, project, oval_id) -> None:
        print(f"LEFT OBJECT ID {oval_id}")
        self.canvas.itemconfigure(oval_id, fill=self.colors['button'])
        #self.canvas.itemconfigure('primary_label', state='normal')

        #  all primary labels return to view
        self.canvas.itemconfigure('primary_label', state='disabled')
        time.sleep(0.02)

        
    #   now handled on child button object
    def handle_button_click(self, event, project, oval_id) -> None:
        print(f"oval clicked: {oval_id}, {project['name']}")
        print(f"")



    def set_root_properties(self) -> None:
        ''' setup root object attributes. The root object has no concept of x,y coordinates - just make it full screen and transparent '''
        
        # Hide the UI initially
        ############self.root.withdraw()
        self.root.overrideredirect(True)

        #  make root transparent when showing the 'bg' color
        self.root.wm_attributes('-transparentcolor', self.root['bg'])

        #  root is full screen, but unnoticeable because it is transparent
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")

        #  escape key quits the UI
        self.root.bind('<Escape>', lambda e: self.root.quit())

        #  Removes title bar, icon from system tray
        self.root.deiconify()

        #  update all root properties
        self.root.update_idletasks()



    def change_color_brightness(self, hex_color_code:str, brightness_change:int) -> str:
        ''' takes a current hex color code and an integer used to adjust brightness.
            a negative brightness change makes the color darker
            a positive brightness change makes the color lighter'''

        #  Extract only hexadecimal characters from the input string
        hex_color_code = re.sub('[^0-9a-fA-F]', '', hex_color_code)
    
        #  Convert the hex color code to RGB values
        red = int(hex_color_code[0:2], 16)
        green = int(hex_color_code[2:4], 16)
        blue = int(hex_color_code[4:6], 16)
    
        #  Calculate the new RGB values based on the brightness change - max of 255 and min of 0
        new_red = max(min(red + brightness_change, 255), 0)
        new_green = max(min(green + brightness_change, 255), 0)
        new_blue = max(min(blue + brightness_change, 255), 0)
    
        #  Convert the new RGB values back to a hex color code and return it
        return '#{:02x}{:02x}{:02x}'.format(new_red, new_green, new_blue)
