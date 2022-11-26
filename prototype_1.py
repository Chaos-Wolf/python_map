import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import pm
import random
s = []
#just for my sanity so the arrays in the terminal dont look so crazy
def clean_print(x):
	for a in x:
		print(a)
#i mean it opens the file you want it too, it places the .csv file into the array
#it also prints the resulting array to the terminal as well as calling the 
#distances between each objects in the array
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(filetypes=[("System Files", "*.csv"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    global s
    s = pm.readall(filepath)
    clean_print(s)   
    pm.disall(s)
    window.title(f"Space Map Editor - {filepath}")
#takes whats in the editor and saves them to a .csv file
#should probaby add it to the array
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("System Files", "*.csv"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Space Map Editor - {filepath}")
#the guts to make the random star systems
def randsystem(size):
	#creates a random star system
	y = []
	for x in range(size):
		star = pm.ranstar()
		y.append([star.name,star.x,star.y,star.z,star.size,star.color,star.type])
	return(y)
#what the button to make a random starsystem talks to
def randouter():
	sys_amount = random.choice(range(10,20))
	x = randsystem(sys_amount)
	txt_edit.delete(1.0, tk.END)
	place = 0
	for a in x:
		for b in a:
			text = b
			txt_edit.insert(tk.END, text)
			txt_edit.insert(tk.END, ',')
		txt_edit.delete("end-2c",tk.END)
		txt_edit.insert(tk.END, '\n')
	txt_edit.delete("end-2c",tk.END)
	global s
	s = x
	clean_print(s)
	pm.disall(s)

#increases the value of the XYZ cordinates
def increase(buttonid):
    value = int(lbl_value[buttonid]["text"])
    lbl_value[buttonid]["text"] = f"{value + 1}"

#increases the size value by 10 because i can't get it to work with above
def increaseten():
    value = int(lbl_values["text"])
    lbl_values["text"] = f"{value + 10}"
	
# same as above above but down this time
def decrease(buttonid):
    value = int(lbl_value[buttonid]["text"])
    lbl_value[buttonid]["text"] = f"{value - 1}"

# same as above above but down this time and still stupid
def decreaseten():
    value = int(lbl_values["text"])
    lbl_values["text"] = f"{value - 10}"

#submit to the whims...this takes the values in each section of star creation and 
#places them at the end of array s and places it on the text editor
def submit():
	line = [en.get(), int(lbl_valuex.cget("text")), int(lbl_valuey.cget("text")), int(lbl_valuez.cget("text")), int(lbl_values.cget("text")), tkvar_color.get(), tkvar_type.get()]
	if txt_edit.compare("end-1c", "!=", "1.0"):
		txt_edit.insert(tk.END, '\n')
	for x in line:
		txt_edit.insert(tk.END, x)
		txt_edit.insert(tk.END, ', ')
	txt_edit.delete("end-3c",tk.END)
	s.append(line)
	clean_print(s)
#all of the code for the window using tkinter
window = tk.Tk()
window.title("Space Map Editor")
window.rowconfigure(1, minsize=50, weight=1)
window.columnconfigure(1, minsize=50, weight=1)
#setting up the text editor and buttons
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
fr_starinput = tk.Frame(window, relief=tk.RAISED, bd=2)
fr_example = tk.Frame(window, relief=tk.RAISED, bd=2)

btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_graph = tk.Button(fr_buttons, text="Show Map", command=lambda: pm.graph(s))
btn_rand = tk.Button(fr_buttons, text="Random Map", command=randouter)
tk.Label(fr_starinput, text="Star Name:").grid(row=1, column=0)
tk.Label(fr_example, text="name, x, y, z, size, color, type  Example: world,1,2,3,50,y,o").grid(row=1, column=0)
tk.Label(fr_example, text="Types: o = star, ^ = space station, s = black hole, p = nebula").grid(row=2, column=0)
tk.Label(fr_example, text="Colors: type the color name Example: yellow, blue, black").grid(row=3, column=0)
en = tk.Entry(fr_starinput)

btn_increasex = tk.Button(fr_starinput, text="+", command=lambda: increase(0))
lbl_valuex = tk.Label(fr_starinput, text="0")
btn_decreasex = tk.Button(fr_starinput, text="-", command=lambda: decrease(0))

btn_increasey = tk.Button(fr_starinput, text="+", command=lambda: increase(1))
lbl_valuey = tk.Label(fr_starinput, text="0")
btn_decreasey = tk.Button(fr_starinput, text="-", command=lambda: decrease(1))

btn_increasez = tk.Button(fr_starinput, text="+", command=lambda: increase(2))
lbl_valuez = tk.Label(fr_starinput, text="0")
btn_decreasez = tk.Button(fr_starinput, text="-", command=lambda: decrease(2))

btn_increases = tk.Button(fr_starinput, text="+", command=lambda: increaseten())
lbl_values = tk.Label(fr_starinput, text="0")
btn_decreases = tk.Button(fr_starinput, text="-", command=lambda: decreaseten())

btn_submit = tk.Button(fr_starinput, text="submit", command=submit)
#drop down menus
tkvar_type = tk.StringVar()
tkvar_color = tk.StringVar()
color = {'b','r','y','w','k'}
obs = {'o','^','s','p'}
tkvar_type.set('o')
tkvar_color.set('y')

obtype_color = tk.OptionMenu(fr_starinput,tkvar_color,*color)
obtype_type = tk.OptionMenu(fr_starinput,tkvar_type,*obs)
#button locations on the windows
btn_open.grid(row=0, column=0, sticky="ew", padx=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_graph.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_rand.grid(row=3, column=0, sticky="ew", padx=5)
en.grid(row=1, column=1)

btn_increasex.grid(row=0, column=2)
lbl_valuex.grid(row=1, column=2)
btn_decreasex.grid(row=2, column=2)

btn_increasey.grid(row=0, column=3)
lbl_valuey.grid(row=1, column=3)
btn_decreasey.grid(row=2, column=3)

btn_increasez.grid(row=0, column=4)
lbl_valuez.grid(row=1, column=4)
btn_decreasez.grid(row=2, column=4)

btn_increases.grid(row=0, column=5)
lbl_values.grid(row=1, column=5)
btn_decreases.grid(row=2, column=5)

obtype_color.grid(row=1,column=6)
obtype_type.grid(row=1,column=7)

btn_submit.grid(row=1,column=8)

lbl_value = [lbl_valuex,lbl_valuey,lbl_valuez]
#overarching structure of the window
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
fr_starinput.grid(row=1, column=1, sticky="ew")
fr_example.grid(row=2, column=1, sticky="ew")
window.mainloop()
