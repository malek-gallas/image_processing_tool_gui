#####################################   DEPENDANCIES   ##########################################

#Libraries
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import platform

#Modules
from menu_bar import create_menu_bar
from settings_frame import create_settings_frame
from toolbox_frame import create_toolbox_frame
from process_frame import create_process_frame

#####################################   INITIALIZATION   ##########################################

root = Tk()
root.title('Image Processing Tool')
root['bg'] = 'white'
root.state('zoomed')
default_bg_color = "SystemButtonFace"

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Configure frames to expand vertically
root.rowconfigure(1, weight=1)
# Configure frames to expand horizentally
root.columnconfigure(1, weight=1)

########################################   FUNCTIONS   ############################################

def alert():
    showinfo("Credits", "Python Tkinter Project.\nMalek Gallas.\n10/05/2023.")

def show_horizental_line():
    global lines_visible
    canvas.itemconfig(horizental_line, state="normal")
    canvas.itemconfig(vertical_line, state="hidden")
    lines_visible = True

def show_vertical_line():
    global lines_visible
    canvas.itemconfig(horizental_line, state="hidden")
    canvas.itemconfig(vertical_line, state="normal")
    lines_visible = True

def show_both_lines():
    global lines_visible
    canvas.itemconfig(horizental_line, state="normal")
    canvas.itemconfig(vertical_line, state="normal")
    lines_visible = True

def hide_lines():
    global lines_visible
    canvas.itemconfig(horizental_line, state="hidden")
    canvas.itemconfig(vertical_line, state="hidden")
    lines_visible = False

def normal_theme():
    settings_frame.config(bg=default_bg_color)
    toolbox_frame.config(bg=default_bg_color)
    process_frame.config(bg=default_bg_color)
    canvas.config(bg='grey')
    presets_frame.config(bg=default_bg_color)
    adjustments_frame.config(bg=default_bg_color)
    controls_frame.config(bg=default_bg_color)

def developper_theme():
    settings_frame.config(bg='red')
    toolbox_frame.config(bg='green')
    process_frame.config(bg='blue')
    canvas.config(bg='yellow')
    presets_frame.config(bg='cyan')
    adjustments_frame.config(bg='magenta')
    controls_frame.config(bg='indigo')

def import_image():
    global photo
    filepath = askopenfilename(title="Import Image", filetypes=[('png files','.png'),('all files','.*')])
    photo = PhotoImage(file=filepath)

    # Get the dimensions of the canvas and the image
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    image_width = photo.width()
    image_height = photo.height()

    # Calculate the coordinates to center the image
    x = (canvas_width - image_width) // 2
    y = (canvas_height - image_height) // 2

    # Create the image on the canvas at the center coordinates and assign a tag
    image_tag = canvas.create_image(x, y, anchor=NW, image=photo)

    # Configure the image item using its tag
    canvas.itemconfig(image_tag, image=photo)

# Pack all functions in a tuple
functions = (import_image, hide_lines, show_horizental_line, show_vertical_line, show_both_lines, normal_theme, developper_theme, alert) 

########################################   MENU_BAR   ############################################

menu_bar = create_menu_bar(root, functions)
root.config(menu=menu_bar)

######################################   SETTINGS_FRAME   ##########################################

settings_frame = create_settings_frame(root)
settings_frame.grid(row=0, column=0, columnspan=3, sticky='new')

######################################   TOOLBOX_FRAME   ##########################################

toolbox_frame = create_toolbox_frame(root)
toolbox_frame.grid(row=1, column=0, sticky='nse')

######################################   PROCESS_FRAME   ##########################################

(process_frame, presets_frame, adjustments_frame, controls_frame) = create_process_frame(root)
process_frame.grid(row=1, column=2, sticky='nsw')

##########################################   CANVAS   #############################################
canvas = Canvas(root, bg='grey')

lines_visible = False

root.update()

toolbox_width = toolbox_frame.winfo_width()
process_width = process_frame.winfo_width()
canvas_width = screen_width - (toolbox_width + process_width + 6) # +6 because we added an empty label with width=6 to toolbox_frame

settings_height = settings_frame.winfo_height()
# Get the height of an empty label
temp_label_height = Label(root).winfo_reqheight()
# Get the height of the men_bar
menu_bar_height = menu_bar.winfo_reqheight()
canvas_height = screen_height - (settings_height + temp_label_height + (menu_bar_height/2) + 8) # +8 because of the title_bar

horizental_line = canvas.create_line(0, canvas_height/2, canvas_width, canvas_height/2, state="hidden")
vertical_line = canvas.create_line(canvas_width/2, 0, canvas_width/2, canvas_height, state="hidden")

canvas.grid(row=1, column=1, sticky='nsew')

if not lines_visible:
    hide_lines()
    
############################################   MAIN   ###############################################

root.mainloop()

################################################### MALEK GALLAS - EPI DIGITAL SCHOOL - 3TC - GROUPE M ####################################################
