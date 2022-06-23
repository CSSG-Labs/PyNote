import PySimpleGUI as sg

#set the theme for the screen/window
sg.theme('SystemDefault')

#define layout
layout=[[sg.Multiline(size=(80,10),tooltip='Write your Text here')]]

#Define Window
win =sg.Window('PyNote',layout)

#Read values entered by user
events,values = win.read()

#close first window
win.close()