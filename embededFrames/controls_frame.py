from tkinter import *

def create_controls_frame(process_frame, presets_list, adjustments_parameters):

    # create controls_frame
    controls_frame = Frame(process_frame, width=400)

    # Unpack adjustments_parameters
    (input1, input2, input3, input4, rb1, rb2, scale) = adjustments_parameters 


    # presets_data
    presets_data = {
        'Preset 1': {
            'Level': 10,
            'Exposure': 20,
            'Vibrance': 30,
            'Saturation': 40,
            'Mode': 1,
            'Balance': 3
        },
        'Preset 2': {
            'Level': 20,
            'Exposure': 30,
            'Vibrance': 40,
            'Saturation': 50,
            'Mode': 2,
            'Balance': 5
        },
        'Preset 3': {
            'Level': 30,
            'Exposure': 40,
            'Vibrance': 50,
            'Saturation': 60,
            'Mode': 1,
            'Balance': 7
        },
        'Preset 4': {
            'Level': 40,
            'Exposure': 50,
            'Vibrance': 60,
            'Saturation': 70,
            'Mode': 2,
            'Balance': 9
        }
    }

    # Load function
    def load_preset(event):
        # Get the name of the selected preset
        selection = presets_list.curselection()
        if selection:
            name = presets_list.get(selection[0])
            # Get the data for the selected preset from the presets_data dictionary
            data = presets_data.get(name, {})
            # Set the values of the corresponding widgets in the adjustments_frame
            input1.delete(0, END)
            input1.insert(0, data.get('Level', ''))
            input2.delete(0, END)
            input2.insert(0, data.get('Exposure', ''))
            input3.delete(0, END)
            input3.insert(0, data.get('Vibrance', ''))
            input4.delete(0, END)
            input4.insert(0, data.get('Saturation', ''))
            balance = data.get('Balance', 5)
            scale.set(balance)
            mode = data.get('Mode', 1)
            if mode == 1:
                rb1.select()
            elif mode == 2:
                rb2.select()

    # Bind the load_preset function to the <<ListboxSelect>> event of the presets_list listbox
    presets_list.bind('<<ListboxSelect>>', load_preset)

    # Save function
    var = IntVar()
    def save_preset():
        preset_name = f"Preset {len(presets_list.get(0, END)) + 1}"
        if not preset_name:
            messagebox.showerror("Error", "Please enter a preset name")
            return

        preset_values = [input1.get(), input2.get(), input3.get(), input4.get(), scale.get(), var.get()]
        presets_list.insert(END, preset_name)
        presets_data[preset_name] = {
            'Level': preset_values[0],
            'Exposure': preset_values[1],
            'Vibrance': preset_values[2],
            'Saturation': preset_values[3],
            'Balance': preset_values[4],
            'Mode': preset_values[5]
        }

    # Reset function
    def reset_adjustments():
        selected_preset_name = presets_list.get(presets_list.curselection())
        if selected_preset_name in presets_data:
            preset = presets_data[selected_preset_name]
            input1.delete(0, END)
            input1.insert(0, preset['Level'])
            input2.delete(0, END)
            input2.insert(0, preset['Exposure'])
            input3.delete(0, END)
            input3.insert(0, preset['Vibrance'])
            input4.delete(0, END)
            input4.insert(0, preset['Saturation'])
            var.set(preset['Mode'])
            if preset['Mode'] == 1:
                rb1.select()
            else:
                rb2.select()
            scale.set(preset['Balance'])

    # create and add "Save" button
    save_button = Button(controls_frame, relief= GROOVE, text="Save", width=10, height=2, command= save_preset)  
    save_button.grid(row=0, column=0, padx=10, pady=5)

    # create and add "Reset" button
    reset_button = Button(controls_frame, relief= GROOVE, text="Reset", width=10, height=2, command= reset_adjustments) 
    reset_button.grid(row=0, column=1, padx=10, pady=5)

    # create and add "Apply" button
    apply_button = Button(controls_frame, relief= GROOVE, text="Apply", width=25, height=2) 
    apply_button.grid(row=1, columnspan=2, padx=10, pady=5)

    # Return controls_frame
    return controls_frame
