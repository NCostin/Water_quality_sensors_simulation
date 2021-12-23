from tkinter import *
from tk_tools import *
from PIL import ImageTk, Image
import random

class Application(Frame):

	# class constructor

	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()
		
	# function for generating led widgets

	def __create_leds(self):

		 #create leds for normal values
		
		self.led_1 = Led(self, size = 15)
		self.led_1.grid(row = 1, column = 3, pady=(20,0))
		
		self.led_2 = Led(self, size = 15)
		self.led_2.grid(row = 2, column = 3, pady=(20,0))
		
		self.led_3 = Led(self, size = 15)
		self.led_3.grid(row = 3, column = 3, pady=(20,0))
		
		self.led_4 = Led(self, size = 15)
		self.led_4.grid(row = 4, column = 3, pady=(20,0))
		
		self.led_5 = Led(self, size = 15)
		self.led_5.grid(row = 5, column = 3, pady=(20,0))
		
		self.led_6 = Led(self, size = 15)
		self.led_6.grid(row = 6, column = 3, pady=(20,0))
		
		#create leds for anormal values
		
		self.aled_1 = Led(self, size = 15)
		self.aled_1.grid(row = 1, column = 4, pady=(20,0))
		
		self.aled_2 = Led(self, size = 15)
		self.aled_2.grid(row = 2, column = 4, pady=(20,0))
		
		self.aled_3 = Led(self, size = 15)
		self.aled_3.grid(row = 3, column = 4, pady=(20,0))
		
		self.aled_4 = Led(self, size = 15)
		self.aled_4.grid(row = 4, column = 4, pady=(20,0))
		
		self.aled_5 = Led(self, size = 15)
		self.aled_5.grid(row = 5, column = 4, pady=(20,0))
		
		self.aled_6 = Led(self, size = 15)
		self.aled_6.grid(row = 6, column = 4, pady=(20,0))

	# function for generating description labels

	def __create_description_labels(self):


		Label(self, text = "Water Parameters"
			 ).grid(row = 0, column = 0, padx = 30, pady = 5)
		
		Label(self, text = "Values"
			 ).grid(row = 0, column = 1, padx = 30)
		
		Label(self, text = "Unit of\n""measurement"
			 ).grid(row = 0, column = 2, padx = 30, pady = 5 )
		
		Label(self, text = "Normal"
			 ).grid(row = 0, column = 3, padx = 30, pady = 5)
		
		Label(self, text = "Anormal"
			 ).grid(row = 0, column = 4, pady = 5)

		Label(self, text = "Readings interval (sec)"
			).grid(row = 7, column = 0, columnspan = 2)

	# function for generating parameters labels

	def __create_description_terms(self):

		Label(self, text = "Temperature"
			 ).grid(row = 1, column = 0,  pady=(20,0))
		
		Label(self, text = "pH"
			 ).grid(row = 2, column = 0,  pady=(20,0))
		
		Label(self, text = "Electroconductivity"
			 ).grid(row = 3, column = 0,  pady=(20,0))
		
		Label(self, text = "Turbidity"
			 ).grid(row = 4, column = 0,  pady=(20,0))
		
		Label(self, text = "Dissolved oxygen"
			 ).grid(row = 5, column = 0,  pady=(20,0))
		
		Label(self, text = "Residual Chlorhine"
			 ).grid(row = 6, column = 0, pady=(20,0))

	# function for generating text boxes 

	def __create_values_text_boxes(self):

		self.temp_box = Text(self, width = 5, height = 1)
		self.temp_box.grid(row = 1, column = 1, pady=(20,0))
		
		self.ph_box = Text(self, width = 5, height = 1)
		self.ph_box.grid(row = 2, column = 1, pady=(20,0))
		
		self.ec_box = Text(self, width = 5, height = 1)
		self.ec_box.grid(row = 3, column = 1, pady=(20,0))
		
		self.tur_box = Text(self, width = 5, height = 1)
		self.tur_box.grid(row = 4, column = 1, pady=(20,0))
		
		self.oxi_box = Text(self, width = 5, height = 1)
		self.oxi_box.grid(row = 5, column = 1, pady=(20,0))
		
		self.chlor_box = Text(self, width = 5, height = 1)
		self.chlor_box.grid(row = 6, column = 1, pady=(20,0))


	# function for generating units labels

	def __create_units_labels(self):

		units = ["°C", "-", "uS", "NTU", "mg/L", "mg/L"]

		row = 1

		for unit in units:

			Label(self, text = unit
				 ).grid(row = row, column = 2, pady=(20,0))

			row += 1

	# function for generating buttons

	def __create_buttons(self, start_command = None, stop_command = None):

		self.button_start = Button(self,
		text = "Start simulation",
		command = start_command,
		width = 30,
		height = 2)
		
		self.button_start.grid(row = 7, column = 5, pady = (20,0))

		self.button_stop = Button(self,
		text = "Stop simulation",
		command = stop_command,
		state = 'disabled',
		width = 30,
		height = 2)

		self.button_stop.grid(row = 8, column = 5, pady = (20,0))


		self.scale = Scale(self, from_ = 1, to = 5, orient = HORIZONTAL, length = 300, tickinterval =1, showvalue = 0)
		self.scale.grid(row = 7, column = 0, columnspan = 3, padx = 20, pady = 50, rowspan = 5)

	# function for generating image

	def __create_canvas(self):
		self.img = ImageTk.PhotoImage(Image.open("water_sensor_image.jpg"))
		self.canvas = Canvas(self, width = 300, height = 350)
		self.canvas.grid(row = 1, column = 5,rowspan = 6)
		self.canvas.create_image(150, 200, image = self.img)

	# function for creating widgets

	def create_widgets(self):
	   
		self.__create_description_labels()
		
		self.__create_description_terms()

		self.__create_values_text_boxes()
		
		self.__create_units_labels()
		
		self.__create_leds()

		self.__create_buttons(start_command = self.generate_values, stop_command = self.stop )

		self.__create_canvas()


	# function for sensors values generation

	def generate_values(self):

		self.temp = round(random.uniform(19,20),1)

		self.ph = round(random.uniform(4.0,10.0),2)

		self.ec = random.randrange(0,2700)

		self.tur = round(random.uniform(0.1,2),1)

		self.oxi = round(random.uniform(4,8),1)

		self.chlor = round(random.uniform(0,7),1)


		self.temp_box.delete(0.0, END)
		self.ph_box.delete(0.0, END)
		self.ec_box.delete(0.0, END)
		self.tur_box.delete(0.0, END)
		self.oxi_box.delete(0.0, END)
		self.chlor_box.delete(0.0, END)


		self.temp_box.insert(0.0, self.temp)
		self.ph_box.insert(0.0, self.ph)
		self.ec_box.insert(0.0, self.ec)
		self.tur_box.insert(0.0, self.tur)
		self.oxi_box.insert(0.0, self.oxi)
		self.chlor_box.insert(0.0, self.chlor)

		self.button_start['state'] = ['disabled']
		self.button_stop['state'] = ['active']

		self.check()

		#delay the value generation for x seconds

		self.after(1000 * self.scale.get(), self.generate_values)

		
	# function for quitting the program

	def stop(self):
		self.quit()


	# function for led management

	def check(self):

		if 13 <= self.temp <= 20:

			self.led_1.to_green() 
			self.aled_1.to_grey()

		else:

			self.aled_1.to_red()
			self.led_1.to_grey()


		if 6.5 <= self.ph <= 8.5:

			self.led_2.to_green() 
			self.aled_2.to_grey()

		else:

			self.aled_2.to_red()
			self.led_2.to_grey()


		if 0 <= self.ec <= 2500:

			self.led_3.to_green() 
			self.aled_3.to_grey()

		else:

			self.aled_3.to_red()
			self.led_3.to_grey()


		if 0.1 <= self.tur <= 1.0:

			self.led_4.to_green() 
			self.aled_4.to_grey()

		else:

			self.aled_4.to_red()
			self.led_4.to_grey()


		if 6.5 <= self.oxi <= 8:

			self.led_5.to_green() 
			self.aled_5.to_grey()

		else:

			self.aled_5.to_red()
			self.led_5.to_grey()




		if 1.0 <= self.chlor <= 4.0:

			self.led_6.to_green() 
			self.aled_6.to_grey()

		else:

			self.aled_6.to_red()
			self.led_6.to_grey()




#main
root = Tk()
root.title("Water quality sensors simulation")
root.geometry("900x520")
app = Application(root)
root.mainloop()