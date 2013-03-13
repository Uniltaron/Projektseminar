from Tkinter import *
#from import_the import *

#OOP is just what we need!
class Gui(object):
    def __init__(self, master, bla, fasel):
        #setup mainframe, contains all gui-elements
        frame = Frame(master)
        frame.grid() #grid > pack
        self.switch = True
        #"New Thesaurus"-Button
        self.new_thb = Button (frame, text="New Thesaurus", command=self.new_the)
        self.new_thb.grid(row = 0, column = 0)
        
        #"Import Thesaurus"-Button
        self.import_thb = Button (frame, text="Import Thesaurus", command = self.import_the)
        self.import_thb.grid(row = 0, column = 1)
        
        #"Quit"-Button
        self.endb = Button (frame, text="Quit", command = frame.quit)
        self.endb.grid(row=1)
        
        #test:Button to blend out the new_thb:
        self.blend_out_b = Button (frame, text="Ausblenden", command = self.blend_out)
        self.blend_out_b.grid(row=2)
        
        #Create Function-Objects
        self.button_func = Gui_Funcs(bla, fasel)
    #button1 command
    def new_the(self):
        self.button_func._bla_()
    
    #button2 command
    def import_the(self):
        self.button_func._blu_()
    def blend_out(self):
        self.import_thb.grid_remove()
    

#just testing some things here...
class Gui_Funcs(object):
    def __init__(self, bla, fasel):
        self.bla = bla
        self.fasel = fasel
    def _bla_(self):
        print "bla"
        i = 0
        while i != self.fasel:
            print self.bla
            i += 1
    def _blu_(self):
        print "blu"

root = Tk()
app = Gui(root, "bla", 2)

root.mainloop()
