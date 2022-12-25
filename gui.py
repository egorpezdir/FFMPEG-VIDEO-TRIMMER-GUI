import subprocess
import tkinter as tk
from tkinter import filedialog
import os

def trim_video():
    start_time = start_hours_entry.get() + ":" + start_minutes_entry.get() + ":" + start_seconds_entry.get()
    end_time = end_hours_entry.get() + ":" + end_minutes_entry.get() + ":" + end_seconds_entry.get()
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()

    # Use ffmpeg to trim the video
    command = ['ffmpeg', '-i', input_file, '-ss', start_time, '-to', end_time, output_file]
    subprocess.call(command)

def select_input_file():
    # Open the file explorer to select a video file
    input_file = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv;*.webm")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, input_file)



def select_output_file():
    # Open the file explorer to select a file for the output
    output_file = filedialog.asksaveasfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv;*.webm")])

    # Split the file name and extension
    file_name, file_ext = os.path.splitext(output_file)

    # If the extension is empty, append .mp4 to the file name
    if file_ext == "":
        output_file = file_name + ".mp4"

    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, output_file)


# Create the main window
window = tk.Tk()
window.title("Video Trimmer")

# Create the input file entry and label
input_file_label = tk.Label(text="Input file:")
input_file_label.pack()
input_file_entry = tk.Entry()
input_file_entry.pack()

# Create the button to select the input file
select_input_file_button = tk.Button(text="Choose video", command=select_input_file)
select_input_file_button.pack()

# Create the start time entries and labels
start_time_label = tk.Label(text="Start time:")
start_time_label.pack()

start_time_frame = tk.Frame()
start_time_frame.pack()

start_hours_label = tk.Label(start_time_frame, text="Hours:")
start_hours_label.pack(side="left")
start_hours_entry = tk.Entry(start_time_frame, width=5)
start_hours_entry.pack(side="left")

start_minutes_label = tk.Label(start_time_frame, text="Minutes:")
start_minutes_label.pack(side="left")
start_minutes_entry = tk.Entry(start_time_frame, width=5)
start_minutes_entry.pack(side="left")

start_seconds_label = tk.Label(start_time_frame, text="Seconds:")
start_seconds_label.pack(side="left")
start_seconds_entry = tk.Entry(start_time_frame, width=5)
start_seconds_entry.pack(side="left")

# Create the end time entries and labels
end_time_label = tk.Label(text="End time:")
end_time_label.pack()

end_time_frame = tk.Frame()
end_time_frame.pack()

end_hours_label = tk.Label(end_time_frame, text="Hours:")
end_hours_label.pack(side="left")
end_hours_entry = tk.Entry(end_time_frame, width=5)
end_hours_entry.pack(side="left")

end_minutes_label = tk.Label(end_time_frame, text="Minutes:")
end_minutes_label.pack(side="left")
end_minutes_entry = tk.Entry(end_time_frame, width=5)
end_minutes_entry.pack(side="left")

end_seconds_label = tk.Label(end_time_frame, text="Seconds:")
end_seconds_label.pack(side="left")
end_seconds_entry = tk.Entry(end_time_frame, width=5)
end_seconds_entry.pack(side="left")

# Create the output file entry and label
output_file_label = tk.Label(text="Output file:")
output_file_label.pack()
output_file_entry = tk.Entry()
output_file_entry.pack()

# Create the button to select the output file
select_input_file_button = tk.Button(text="Choose output", command=select_output_file)
select_input_file_button.pack()

# Create the trim button
trim_button = tk.Button(text="Trim", command=trim_video)
trim_button.pack()

# Run the main loop
window.mainloop()
