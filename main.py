import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk as ui

'''from os import system as command
from platform import system as sys

def clr():
    if sys() == "Linux":
        command("clear")

    if sys() == "Darwin":
        command("clear")
    
    if sys() == "Windows":
        command("cls")

    
def pause(st = ""):
    input(st)

def main():
    while True:
        pause("""
        Welcome to the Python Learning Program. This program will teach you about python from the basics
        of python(Only as much as i know about python, which is not much). 

        Expect this project to grow with time as more and more developers find their interests in it

        ***Please note that this program does not provide a formal degree or something that you can add to
        your job resume or something like that. This is only a fun project with great motives. All the content
        used here is either self made or used under the conditions of "fair-use".***
        
        Hope you will have fun! Please press enter to continue!
        """)
'''

class Main:
    def __init__(self):
        ui_template = "Tuitor_gui.glade"
        self.builder = ui.Builder()
        self.builder.add_from_file(ui_template)


if __name__ == "__main__":
    main = Main()
    ui.main()