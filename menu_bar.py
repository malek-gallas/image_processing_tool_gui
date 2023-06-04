from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import platform

def create_menu_bar(root, functions):

    # Unpack functions tuple
    (import_image, hide_lines, show_horizental_line, show_vertical_line, show_both_lines, normal_theme, developper_theme, alert) = functions

    # Create menu_bar
    menu_bar = Menu(root)

    # file_menu
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New")
    file_menu.add_command(label="Open")
    file_menu.add_separator()
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Save As")
    file_menu.add_separator()
    file_menu.add_command(label="Import", command=import_image)
    file_menu.add_command(label="Export")
    file_menu.add_separator()
    file_menu.add_command(label="Print")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.destroy)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # edit_menu
    edit_menu = Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Undo")
    edit_menu.add_command(label="Redo")
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut")
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Pase")
    edit_menu.add_separator()
    edit_menu.add_command(label="Preferences")
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    # view_menu
    view_menu = Menu(menu_bar, tearoff=0)
    view_menu.add_command(label="Single", command=hide_lines)
    view_menu.add_command(label="Double Horizental", command=show_horizental_line)
    view_menu.add_command(label="Double Vertical", command=show_vertical_line)
    view_menu.add_command(label="Grid", command=show_both_lines)
    menu_bar.add_cascade(label="View", menu=view_menu)

    # process_menu
    process_menu = Menu(menu_bar, tearoff=0)
    process_menu.add_command(label="Noise")
    process_menu.add_command(label="Filter")
    process_menu.add_command(label="Distortion")
    process_menu.add_command(label="Segmentation")
    menu_bar.add_cascade(label="Process", menu=process_menu)

    # help_menu
    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="Normal Mode", command=normal_theme)
    help_menu.add_command(label="Developer Mode", command=developper_theme)
    help_menu.add_command(label="Credits", command=alert)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    # Return menu_object
    return menu_bar
