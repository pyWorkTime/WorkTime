import tkinter as tk
import math


class PrimaryArc:
    def __init__(
        self,
        data,
        canvas,
        x_origin,
        y_origin,
        radius,
        angle,
        distance_from_origin,
        colors,
        arc_number,
    ) -> None:
        self.arc_number = arc_number
        self.data = data
        self.canvas = canvas
        self.x_origin = x_origin
        self.y_origin = y_origin
        self.radius = radius
        self.angle = angle
        self.colors = colors
        self.distance_from_origin = distance_from_origin

        self.x = self.x_origin + self.distance_from_origin * math.cos(
            math.radians(self.angle)
        )
        self.y = self.y_origin + self.distance_from_origin * math.sin(
            math.radians(self.angle)
        )

        x, y = self.x_origin, self.y_origin  # The center point of the arc
        radius = (
            50  # The radius of the arc - how far will the arc extend from the origin
        )
        start_angle = 45  # The start angle of the arc
        extent = 90  # The extent of the arc


#        self.canvas.create_arc( x-radius,
#                                y-radius,
#                                x+radius,
#                                y+radius,
#                                start=start_angle,
#                                extent=extent,
#                                tags="secondary_arc",
#                                fill=self.colors['text'],
#                                state=tk.HIDDEN,
#                                fill='grey'
#                            )
#        self.canvas.create_arc(x-radius, y-radius, x+radius, y+radius,
#                          start=start_angle+90, extent=extent, fill='red')
