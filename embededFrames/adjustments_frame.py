from tkinter import *

def create_adjustments_frame(process_frame):
    # create adjustements_frame
    adjustments_frame = LabelFrame(process_frame, text="Adjustments")

    # Add 4 labels, 4 inputs, 2 radio buttons, and 1 scale
    Label(adjustments_frame, text='Level').pack(side='top', pady=2)
    input1 = Entry(adjustments_frame, width=30)
    input1.pack(side='top', padx=5, pady=2)

    Label(adjustments_frame, text='Exposure').pack(side='top', pady=2)
    input2 = Entry(adjustments_frame, width=30)
    input2.pack(side='top', padx=5, pady=2)

    Label(adjustments_frame, text='Vibrance').pack(side='top', pady=2)
    input3 = Entry(adjustments_frame, width=30)
    input3.pack(side='top', padx=5, pady=2)

    Label(adjustments_frame, text='Saturation').pack(side='top', pady=2)
    input4 = Entry(adjustments_frame, width=30)
    input4.pack(side='top', padx=5, pady=2)

    Label(adjustments_frame, text='Mode :').pack(side='top', pady=5)
    radio_frame = Frame(adjustments_frame)
    radio_frame.pack(side='top', padx=5, pady=2)

    rb1 = Radiobutton(radio_frame, text='Soft', value=1)
    rb1.pack(side='left', padx=5)
    rb1.select()
    rb2 = Radiobutton(radio_frame, text='Hard', value=2)
    rb2.pack(side='left', padx=5)

    scale_frame = Frame(adjustments_frame)
    scale_frame.pack(side='top', padx=5, pady=2)

    scale_label = Label(scale_frame, text='Balance :')
    scale_label.pack(side='left', anchor='se')
    scale = Scale(scale_frame, from_=1, to=10, orient='horizontal')
    scale.pack(side='left', padx=5, anchor='w')

    adjustments_parameters = (input1, input2, input3, input4, rb1, rb2, scale) 

    #Return adjustments_frame object
    return adjustments_frame, adjustments_parameters
