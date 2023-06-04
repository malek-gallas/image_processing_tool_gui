from tkinter import *

def create_presets_frame(process_frame):
    # create and configure presets_frame
    presets_frame = LabelFrame(process_frame, text="Presets")

    # Create a scrollbar for the presets list
    scrollbar = Scrollbar(presets_frame)
    scrollbar.pack(side='right', fill='y')

    # Add presets list
    presets_list = Listbox(presets_frame, height=4, exportselection=False, yscrollcommand=scrollbar.set)
    presets_list.pack(side='top', padx=5, pady=5)
    presets_list.insert(1, 'Preset 1')
    presets_list.insert(2, 'Preset 2')
    presets_list.insert(3, 'Preset 3')
    presets_list.insert(4, 'Preset 4')

    scrollbar.config(command=presets_list.yview)

    #Return presets_frame object + presets_list
    return presets_frame, presets_list
