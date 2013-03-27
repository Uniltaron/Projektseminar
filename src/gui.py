from Tkinter import *
#let's make it this way, gui gets the thesaurus Methods...
from new_thesaurus import *
#OOP is just what we need!
class Gui(object):
	def __init__(self, master):
		#setup mainframe, contains all gui-elements
		frame = Frame(master)
		frame.grid() #grid > pack
		#"New Thesaurus"-Button
		self.new_thb = Button (frame, text="New Thesaurus", command=self.new_the)
		self.new_thb.grid(row = 0, column = 0)

		#"Import Thesaurus"-Button
		self.import_thb = Button (frame, text="Import Thesaurus", command = self.import_the)
		self.import_thb.grid(row = 0, column = 1)

		#"Quit"-Button
		self.endb = Button (frame, text="Quit", command = frame.quit)
		self.endb.grid(row=1)

		#Define Options for File-Dialogue:
		self.file_opt = options = {}
		options['defaultextension'] = '.txt'
		options['filetypes'] = [('xml files', '.xml'), ('json files', '.json'), ('csv files', '.csv')]
		options['initialdir'] = 'C:\\'
		options['initialfile'] = 'subject.xml'
		options['parent'] = root
		options['title'] = 'Importiere Thesuarus aus...'

	def new_the(self):
		pass
		#wie soll das ausschaun...?

	def import_the(self):
		the_datei = tself.askopenfilename(**self.file_opt)
		


root = Tk()
app = Gui(root)

root.mainloop()