import sys
import os
import json
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

class BrainPyFuck:
	def __init__(self):
	    	self.pointers = []
		self.pointer_index = 0

		self.root = Tk()
		self.file_name = ""
		self.saved = False

		self.current_ascii_list_element_count = 0

		with open("ascii.json", "r") as fh:
			self.ascii_table = json.load(fh)

		self.ascii_list_text = ""

	def print(self, text):
		self.listbox_for_console.insert(END, text)

	def print_error(self, error):
		self.listbox_for_console.insert(END, "\n" + error + "\n")

	def clear_console(self):
		self.listbox_for_console.delete(0, END)

	def gui(self):
		self.root.geometry("800x640")
		self.root.resizable(False, False)
		self.root.bind("<Key>", self.key)
		self.root.title("BrainPyFuck | untilted.bpf")

		self.scrollbar = Scrollbar(self.root)
		self.listbox = Listbox(self.root, yscrollcommand=self.scrollbar.set)

		self.console_info_label = Label(self.root, text="Console for Output")

		self.console = Scrollbar(self.root, bg="black")
		self.listbox_for_console = Listbox(self.root, fg="white", bg="black", yscrollcommand=self.console.set)

		self.clear_console_btn = Button(self.root, text="Clear console")
		self.clear_console_btn.config(command=self.clear_console)

		self.paste_cur_ascii_into_code = Button(self.root, text="Paste into code")

		# 95 Characters
		for number in self.ascii_table:
			char = self.ascii_table[number]
			self.ascii_list_text = f"{number} - {char}"
			self.listbox.insert(END, self.ascii_list_text)

		self.scrollbar.place(x=670, y=30, height=370)
		self.listbox.place(x=670, y=30, height=370)
		self.scrollbar.config(command=self.listbox.yview)

		self.console.place(x=10, y=430, width=670, height=200)
		self.clear_console_btn.place(x=680, y=430, width=80, height=30)
		self.listbox_for_console.place(x=10, y=430, width=670, height=200)
		self.console_info_label.place(x=10, y=410)

		self.listbox.bind('<<ListboxSelect>>', self.select_ascii)

		self.paste_cur_ascii_into_code.config(command=self.paste_ascii_into_code)
		self.paste_cur_ascii_into_code.place(x=670, y=5, width=100, height=25)
		
		self.code_input = ScrolledText(self.root)
		self.code_input.place(x=10, y=10)

		self.mainbar = Menu(self.root)

		self.file_bar = Menu(self.mainbar)
		self.run_bar = Menu(self.mainbar)
		self.help_bar = Menu(self.mainbar)

		self.file_bar.add_command(label="Save as", command=self.save_code_as)
		self.file_bar.add_command(label="Save", command=self.save_code)
		self.file_bar.add_command(label="Load", command=self.load_code)

		self.run_bar.add_command(label="Run", command=self.run_code)
		self.run_bar.add_command(label="Reset", command=self.reset_code)

		self.help_bar.add_command(label="Syntax (Will delete your current code)", command=self.open_syntax)
		self.help_bar.add_command(label="About (Will delete your current code)", command=self.about)

		self.mainbar.add_cascade(label="File", menu=self.file_bar)
		self.mainbar.add_cascade(label="Run", menu=self.run_bar)
		self.mainbar.add_cascade(label="Help", menu=self.help_bar)

		self.root.config(menu=self.mainbar)

		self.root.mainloop()

	def reset_code(self):
		self.clear_console()
		self.clear_code()

	def clear_code(self):
		self.code_input.delete("1.0", END)

	def paste_ascii_into_code(self):
		to_insert = "p" * self.current_ascii_list_element_count
		self.code_input.insert(INSERT, "\n" + to_insert)

	def select_ascii(self, e):
		try:
			w = e.widget
			index = int(w.curselection()[0])
			value = w.get(index)

			self.current_ascii_list_element_count = int(value.split(" - ")[0])
		except IndexError:
			pass

	def about(self):
		self.clear_code()
		self.saved = False
		self.file_name = ""
		self.code_input.insert(INSERT,
			"*\n\nBrainPyFuck\n\nCreated by Ari24\n\nIt's a fun language\nDefault extension: .bpf\n*"
			)

	def open_syntax(self):
		self.clear_code()
		self.saved = False
		self.file_name = ""
		self.code_input.insert(INSERT, 
			"* Commentary Start/End Brackets\n\nAll commands:\n\n+ Adds a pointer\n- Removes the last pointer. If pointers are 0, it will raise an Error\n> goes one pointer right. If its on the end, it will go to the first pointer\n< goes one pointer left. If its on the start, it will go to the last pointer\np increase the pointer value by 1\nm decrease the pointer value by 1\ni multiplies the pointer with itself\n; prints the pointer value\n: prints the pointer value in ascii\na prints all pointers (like a list)\ns prints all pointers in ascii value in a row\nn prints all pointers in ascii value\nc prints the current pointer position\nl prints the length of the pointer\n\n*"
			)

	def key(self, e):
		c = e.keysym
		s = e.state

		ctrl  = (s & 0x4) != 0

		if ctrl:
			if c == "s":
				if self.file_name == "":
					self.save_code_as()
				else:
					self.save_code()	
	
	def save_code_as(self):
		self.code = self.code_input.get("1.0", END)
		f = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".bpf")
		if f == None:
			return

		f.write(self.code)
		self.saved = True
		self.file_name = f.name

		self.root.title("BrainPyFuck | " + self.file_name)
		f.close()

	def save_code(self):
		if not self.file_name == "":
			with open(self.file_name, "w") as fh:
				fh.write(self.code_input.get("1.0", END))

			self.saved = True

	def load_code(self, filename=""):
		if filename == "":
			f = tkinter.filedialog.askopenfile()
		else:
			f = open(filename)

		if f == None:
			return

		self.clear_code()
		self.file_name = f.name

		self.code_input.insert(INSERT, f.read())

		self.print("")
		self.print("Loaded " + self.file_name)
		self.print("")

		self.root.title("BrainPyFuck | " + self.file_name)
		f.close()

	def run_code(self):
		if self.saved:
			self.parse()
		else:
			if not self.file_name == "":
				self.save_code()
			else:
				self.save_code_as()

	def parse(self):
		self.pointers = []
		self.pointer_index = 0

		file = open(self.file_name)
		text = file.read()
		file.close()


		'''
		+ Adds a pointer
		- Removes the last pointer. If self.pointers are 0, and its remove another, raise Error
		> goes one pointer right. If its on the end, go to the first pointer
		< goes one pointer left. If its on the start, go to the last pointer
		p increase the pointer value by 1
		m decrease the pointer value by 1
		i multiplies the pointer with itself
		; prints the pointer value
		: prints the pointer ascii value. If its not in the ascii list, it will print nothing
		a prints all self.pointers
		s prints all self.pointers in a row in ascii value. If its not in the ascii list, it will print nothing
		n prints all self.pointers in ascii value. 
		c prints the current pointer position
		l prints the length of the self.pointers
		* Commentary Start Brackets
		* Commentary End Brackets
		'''

		self.syntaxes = [
			"+",
			"-",
			">",
			"<",
			"p",
			"m",
			"i",
			";",
			":",
			"a",
			"s",
			"n",
			"c",
			"l",
			"*"
		]

		isCommentary = False

		i = 0
		for char in text:
			i += 1

			if char == "*":
				if not isCommentary:
					isCommentary = True
					continue
				elif isCommentary:
					isCommentary = False
					continue

			if not char in self.syntaxes:
				if not isCommentary:
					if not char == "\n":
						self.print_error("Can't find this syntax in my syntax list Code, char " + str(i))
						continue

			elif char == "+" and not isCommentary:
				self.pointers.append(0)
				continue

			elif char == "-" and not isCommentary:
				if not len(self.pointers) == 0:
					self.pointers.pop()
				else:
					self.print_error("Cannot remove a pointer from 0 pointers. Code, Char " + str(i))
					return
				continue

			elif char == ">" and not isCommentary:
				if not self.pointer_index == len(self.pointers) - 1:
					self.pointer_index += 1
				else:
					self.pointer_index = 0
				continue

			elif char == "<" and not isCommentary:
				if not self.pointer_index == 0:
					self.pointer_index -= 1
				else:
					self.pointer_index = len(self.pointers) - 1
				continue

			elif char == "p" and not isCommentary:
				try:
					self.pointers[self.pointer_index] += 1
				except IndexError:
					self.print_error("To few Pointers Code, char " + str(i))
				continue

			elif char == "m" and not isCommentary:
				self.pointers[self.pointer_index] -= 1
				continue

			elif char == "i" and not isCommentary:
				self.pointers[self.pointer_index] *= self.pointers[self.pointer_index]
				continue

			elif char == ";" and not isCommentary:
				self.print(str(self.pointers[self.pointer_index]))
				continue

			elif char == ":" and not isCommentary:
				self.print(str(chr(self.pointers[self.pointer_index])))
				continue

			elif char == "s" and not isCommentary:
				to_print = ""
				for pointer in self.pointers:
					to_print += str(chr(pointer))

				self.print(to_print)
				continue

			elif char == "n" and not isCommentary:
				for pointer in self.pointers:
					self.print(str(chr(pointer)))
				continue

			elif char == "a" and not isCommentary:
				self.print(self.pointers)
				continue

			elif char == "c" and not isCommentary:
				self.print(str(self.pointer_index))
				continue

			elif char == "l" and not isCommentary:
				self.print(str(len(self.pointers)))
				continue

	def replace_white_space(self, string):
		return string[:len(string)-1]

	def extension(self, name, extension):
		return self.replace_white_space(name[len(name) - len(extension) - 1:]) == extension


def get_file_name(args):
	# If its opened in a console
	name = ""
	for i in range(len(args)):
		if args[i] == "-f":
			for i in range(i+1, len(args)):
				name += args[i] + " "
			break 

	return name if not name == "" else None

if __name__ == "__main__":
	bpf = BrainPyFuck()
	bpf.gui()
