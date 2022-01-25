from tkinter import *
import time

WIDTH = 500 
HEIGHT = 500
xVelocity = 3
yVelocity = 5



master = Tk()

canvas = Canvas(master , width = WIDTH , height = HEIGHT)
canvas.pack()

background = PhotoImage(file = "E:/python_projects/python_animation/africa.png")
background_canvas_img = canvas.create_image(0 , 0 , image = background , anchor = NW)  # NW = North-west

img = PhotoImage(file = "E:/python_projects/python_animation/Python_logo_PNG14.png")
canvas_img = canvas.create_image(0 , 0 , image = img , anchor = NW)  # NW = North-west

img_width = img.width()
img_height = img.height()

while True:
	coordinates = canvas.coords(canvas_img)
	print(coordinates)

	if(coordinates[0] >= (WIDTH - img_width) or coordinates[0] < 0 ):
		xVelocity = -xVelocity

	if(coordinates[1] >= (HEIGHT - img_height) or coordinates[1] < 0 ):
		yVelocity = -yVelocity

	canvas.move(canvas_img , xVelocity , yVelocity)
	master.update()
	time.sleep(0.01)

	






master.mainloop()