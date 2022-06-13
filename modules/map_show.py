from tkinter import *
import tkintermapview


def mapview(subway):
    root = Toplevel()
    root.geometry(f"{800}x{600}") 
    root.title("map_view_example.py") 

    map_widget = tkintermapview.TkinterMapView(root, width=800, height=500, corner_radius=0) 
    map_widget.pack()
    # 주소 위치지정 
    marker_1 = map_widget.set_address(subway, marker=True)
    print(marker_1.position, marker_1.text) # get position and text 
    marker_1.set_text(subway) # set new text 
    map_widget.set_zoom(15) # 0~19 (19 is the highest zoom level) 
