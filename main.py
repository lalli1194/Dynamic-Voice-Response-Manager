import tkinter as tk
from voice_controller import VoiceController

controller = VoiceController()


def play_text():
    text = text_box.get("1.0", tk.END)
    controller.play(text)


def pause_text():
    controller.pause()


def resume_text():
    controller.resume()


def stop_text():
    controller.stop()


def change_speed(value):
    controller.set_speed(int(value))


root = tk.Tk()
root.title("Dynamic Voice Response Manager")
root.geometry("700x500")

title = tk.Label(
    root,
    text="Dynamic Voice Response Manager",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

text_box = tk.Text(root, height=10, width=60)
text_box.pack(pady=10)

play_btn = tk.Button(
    root,
    text="Play",
    command=play_text,
    width=15
)
play_btn.pack(pady=5)

pause_btn = tk.Button(
    root,
    text="Pause",
    command=pause_text,
    width=15
)
pause_btn.pack(pady=5)

resume_btn = tk.Button(
    root,
    text="Resume",
    command=resume_text,
    width=15
)
resume_btn.pack(pady=5)

stop_btn = tk.Button(
    root,
    text="Stop",
    command=stop_text,
    width=15
)
stop_btn.pack(pady=5)

speed_label = tk.Label(root, text="Speech Speed")
speed_label.pack()

speed_slider = tk.Scale(
    root,
    from_=100,
    to=250,
    orient=tk.HORIZONTAL,
    command=change_speed
)
speed_slider.set(180)
speed_slider.pack()

root.mainloop()