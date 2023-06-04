from tkinter import *

from embededFrames.presets_frame import create_presets_frame
from embededFrames.adjustments_frame import create_adjustments_frame
from embededFrames.controls_frame import create_controls_frame

def create_process_frame(root):
    # create process_frame
    process_frame = Frame(root)

    ######################################   PRESETS_FRAME   ##########################################

    # create and configure presets_frame
    (presets_frame, presets_list) = create_presets_frame(process_frame)
    presets_frame.pack(side='top', padx=10, pady=10, anchor='center')

    ######################################   ADJUSTMENTS_FRAME  ##########################################

    # create and configure adjustements_frame
    (adjustments_frame, (input1, input2, input3, input4, rb1, rb2, scale)) = create_adjustments_frame(process_frame)
    adjustments_frame.pack(side='top', padx=10, pady=10, anchor='center')
    adjustments_parameters = (input1, input2, input3, input4, rb1, rb2, scale)

    ######################################   CONTROLS_FRAME   ##########################################

    # create and configure controls_frame
    controls_frame = create_controls_frame(process_frame, presets_list, adjustments_parameters)  
    controls_frame.pack(side='top', padx=10, pady=10, anchor='center')

    #Return process_frame object
    return (process_frame, presets_frame, adjustments_frame, controls_frame)
