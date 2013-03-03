from Tkinter import *
#from import_the import *

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
    
    #button1 command
    def new_the(self):
        print "Erstellt irgendwann einen neuen Thesaurus!"
    
    #button2 command
    def import_the(self):
        print "Importiert irgendwann mal einen bestehenden Thesaurus!"
        
root = Tk()
app = Gui(root)

root.mainloop()
