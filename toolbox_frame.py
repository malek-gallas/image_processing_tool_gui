from tkinter import *

def create_toolbox_frame(root):
    # create and configure toolbox_frame
    toolbox_frame = Frame(root)
    
    # add an empty label with fixed width to center the buttons vertically
    Label(toolbox_frame, width=6).pack()

    # create the 8 buttons with icons
    cursor_icon = PhotoImage(file='icons/Cursor.png').subsample(25)
    cursor_button = Button(toolbox_frame, bd=0, image=cursor_icon)
    cursor_button.image = cursor_icon  # Store PhotoImage as attribute
    cursor_button.pack(pady=5)

    move_icon = PhotoImage(file='icons/Move.png').subsample(25)
    move_button = Button(toolbox_frame, image=move_icon, bd=0)
    move_button.image = move_icon  # Store PhotoImage as attribute
    move_button.pack(pady=5)

    brush_icon = PhotoImage(file='icons/Brush.png').subsample(25)
    brush_button = Button(toolbox_frame, image=brush_icon, bd=0)
    brush_button.image = brush_icon  # Store PhotoImage as attribute
    brush_button.pack(pady=5)

    eraser_icon = PhotoImage(file='icons/Rubber.png').subsample(25)
    eraser_button = Button(toolbox_frame, image=eraser_icon, bd=0)
    eraser_button.image = eraser_icon  # Store PhotoImage as attribute
    eraser_button.pack(pady=5)

    pipette_icon = PhotoImage(file='icons/Pipette.png').subsample(25)
    pipette_button = Button(toolbox_frame, image=pipette_icon, bd=0)
    pipette_button.image = pipette_icon  # Store PhotoImage as attribute
    pipette_button.pack(pady=5)

    blur_icon = PhotoImage(file='icons/Blur.png').subsample(25)
    blur_button = Button(toolbox_frame, image=blur_icon, bd=0)
    blur_button.image = blur_icon  # Store PhotoImage as attribute
    blur_button.pack(pady=5)

    stamp_icon = PhotoImage(file='icons\Stamp.png').subsample(25)
    stamp_button = Button(toolbox_frame, image=stamp_icon, bd=0)
    stamp_button.image = stamp_icon  # Store PhotoImage as attribute
    stamp_button.pack(pady=5)

    zoom_in_icon = PhotoImage(file='icons/magnifier.png').subsample(25)
    zoom_in_button = Button(toolbox_frame, image=zoom_in_icon, bd=0)
    zoom_in_button.image = zoom_in_icon  # Store PhotoImage as attribute
    zoom_in_button.pack(pady=5)

    # add a separator line between the first 8 buttons and the last 2
    separator = Frame(toolbox_frame, height=2, bg='gray')
    separator.pack(fill='x', pady=5)

    # add the last 2 buttons with icons
    pen_icon = PhotoImage(file='icons/Vector.png').subsample(25)
    pen_button = Button(toolbox_frame, image=pen_icon, bd=0)
    pen_button.image = pen_icon  # Store PhotoImage as attribute
    pen_button.pack(pady=5)

    text_icon = PhotoImage(file='icons/Text.png').subsample(25)
    text_button = Button(toolbox_frame, image=text_icon, bd=0)
    text_button.image = text_icon  # Store PhotoImage as attribute
    text_button.pack(pady=5)

    # center the buttons horizontally
    for widget in toolbox_frame.winfo_children():
        widget.pack_configure(anchor='center')

    #return toolbox_frame_object
    return toolbox_frame
