from tkinter import *

def create_settings_frame(root):
    # create settings_frame
    settings_frame = Frame(root)

    # add an empty label to center the widgets
    empty_label = Label(settings_frame)
    empty_label.grid(row=0, column=0, padx=30, pady=10, sticky='w')

    # add checkboxes
    chk1 = Checkbutton(settings_frame, text="Override")
    chk2 = Checkbutton(settings_frame, text="Block")
    chk1.grid(row=0, column=1, padx=10, pady=10, sticky='w')
    chk2.grid(row=0, column=2, padx=10, pady=10, sticky='w')

    # add spinboxes
    spinbox1_label = Label(settings_frame, text="Flow :")
    spinbox1_label.grid(row=0, column=3, padx=10, pady=10, sticky='e')
    spinbox1 = Spinbox(settings_frame, from_=0, to=100)
    spinbox1.grid(row=0, column=4, padx=10, pady=10, sticky='w')

    spinbox2_label = Label(settings_frame, text="Opacity :")
    spinbox2_label.grid(row=0, column=5, padx=10, pady=10, sticky='e')
    spinbox2 = Spinbox(settings_frame, from_=0, to=100)
    spinbox2.grid(row=0, column=6, padx=10, pady=10, sticky='w')

    # add scale
    scale_label = Label(settings_frame, text="Size :")
    scale_label.grid(row=0, column=7, padx=10, pady=10, sticky='e')
    scale = Scale(settings_frame, from_=0, to=100, orient=HORIZONTAL, length=200, showvalue=0)
    scale.grid(row=0, column=8, padx=10, pady=10, sticky='w')
    scale_value_label = Label(settings_frame, borderwidth=1, text=scale.get())
    scale_value_label.grid(row=0, column=9, padx=10, pady=10, sticky='w')

    # update scale value label
    def update_scale_value_label(value):
        scale_value_label.config(text=value)

    scale.config(command=update_scale_value_label)

    #Return settings_frame object
    return settings_frame
