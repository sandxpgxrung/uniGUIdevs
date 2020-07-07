"""INDIVIDUAL task: food planner (RESUBMISSION) 2018-19 | S5125686, @Sandip Gurung
- This program was designed in purpose of helping users to view caloric contents by food and restaurant menu's """

import requests
import sys
import time
import tkinter as tk
from tkinter import *

window = tk.Tk()  # In order to set height and width
window.title("Food Planner API Program - S5125686")

h = 450
w = 550

app_id = '51466f7d'
app_key = 'b5fe13fe387cb79e0c0594f29cd685e1'

# 'NUTRITIONIX API' was used for this program, link --- >
# https://api.nutritionix.com/v1_1/search/KFC?results=0:20&fields=item_name,brand_name,item_id,nf_calories&appId=51466f7d&appKey=b5fe13fe387cb79e0c0594f29cd685e1

# Food response search


def format_by_food(req_menu_json):  # Gives distinct data values for food search function
    try:
        req_menu_i = (req_menu_json['hits'][0]['fields']['brand_name'],
                      req_menu_json['hits'][0]['fields']['item_name'],
                      req_menu_json['hits'][0]['fields']['nf_calories'])
        req_menu_ii = (req_menu_json['hits'][1]['fields']['brand_name'],
                       req_menu_json['hits'][1]['fields']['item_name'],
                       req_menu_json['hits'][1]['fields']['nf_calories'])
        req_menu_iii = (req_menu_json['hits'][2]['fields']['brand_name'],
                        req_menu_json['hits'][2]['fields']['item_name'],
                        req_menu_json['hits'][2]['fields']['nf_calories'])
        response_str = '\n1.\n Brand: %s \n Item: %s \n  Calories: %s \n' % req_menu_i, \
                       '\n2.\n Brand: %s \n Item: %s \n  Calories: %s \n' % req_menu_ii, \
                       '\n3.\n Brand: %s \n Item: %s \n  Calories: %s \n' % req_menu_iii, \

    except BaseException:

        response_str = 'An error has occurred'
    return response_str

# Restaurant response search


def format_by_restaurant(rpd_menu_json):  # Gives distinct data values for restaurant search function
    try:
        rpd_menu_i = rpd_menu_json['hits'][0]['fields']['item_name'],\
                     rpd_menu_json['hits'][0]['fields']['nf_calories']
        rpd_menu_ii = (rpd_menu_json['hits'][1]['fields']['item_name'],
                       rpd_menu_json['hits'][1]['fields']['nf_calories'])
        rpd_menu_iii = (rpd_menu_json['hits'][2]['fields']['item_name'],
                        rpd_menu_json['hits'][2]['fields']['nf_calories'])

        response_str = '1.\n Food: %s \n  Calories: %s \n' % rpd_menu_i, \
                       '\n2.\n Food: %s \n  Calories: %s \n' % rpd_menu_ii,\
                       '\n3.\n Food: %s \n  Calories: %s \n' % rpd_menu_iii
    except BaseException:

        response_str = 'An unexpected error occurred.'
    return response_str


def get_by_food(search):  # GET
    url = 'https://api.nutritionix.com/v1_1/search/'+search+'?results=0:3&fields=item_name,brand_name,item_id,' \
          'nf_calories&appId=' + app_id + '&appKey=' + app_key
    req_menu = requests.get(url)  # REQUESTS MENU
    req_menu_json = req_menu.json()  # REQ_MENU IN JSON FORMAT
    req_menu_i = (req_menu_json['hits'][0]['fields']['brand_name'], req_menu_json['hits'][0]['fields']['nf_calories'])
    req_menu_ii = (req_menu_json['hits'][1]['fields']['brand_name'], req_menu_json['hits'][1]['fields']['nf_calories'])
    req_menu_iii = (req_menu_json['hits'][2]['fields']['brand_name'], req_menu_json['hits'][2]['fields']['nf_calories'])
    print(req_menu_i, req_menu_ii, req_menu_iii)

    results['text'] = format_by_food(req_menu_json)


def get_by_restaurant(search):  # GET
    url = 'https://api.nutritionix.com/v1_1/search/' + search + '?results=0:3&fields=item_name,brand_name,item_id,' \
                                                                'nf_calories&appId=' + app_id + '&appKey=' + app_key
    req_menu = requests.get(url)  # REQUESTS MENU
    rpd_menu_json = req_menu.json()  # REQ_MENU IN JSON FORMAT
    rpd_menu_i = (rpd_menu_json['hits'][0]['fields']['item_name'], rpd_menu_json['hits'][0]['fields']['nf_calories'])
    rpd_menu_ii = (rpd_menu_json['hits'][1]['fields']['item_name'], rpd_menu_json['hits'][1]['fields']['nf_calories'])
    rpd_menu_iii = (rpd_menu_json['hits'][2]['fields']['item_name'], rpd_menu_json['hits'][2]['fields']['nf_calories'])
    print(rpd_menu_i, rpd_menu_ii, rpd_menu_iii)

    results['text'] = format_by_restaurant(rpd_menu_json)


def tick():  # Helping users keep track of live time (GMT)
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)

C = tk.Canvas(window, height=h, width=w)  # Initialisation for setting height and width
C.pack()

frame = tk.Frame(window, bg='cornflower blue', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=1.0, relheight=0.1, anchor='n')

title = Label(window, text='FOOD PLANNER - NUTRITIONAL INFORMATION - POWERED BY NUTRITIONIX (API)')
title.pack()

textbox = tk.Entry(frame, font=40)  # Creates textbox in the pre-set frame
textbox.place(relwidth=0.35, relheight=1)

button = tk.Button(
    frame,
    text='Search Food',
    font=15,
    bg='light goldenrod',  # i.e. Sets colour for chosen theme
    command=lambda: get_by_food(
        textbox.get()))
button.place(relx=0.4, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(window, bg='cyan', bd=10)
lower_frame.place(
    relx=0.5,  # relx, rely, etc. i.e. for adjusting widgets on the GRID PROPERLY.
    rely=0.2,
    relwidth=1.0,
    relheight=0.75,
    anchor='n')
label = tk.Label(lower_frame, font=('Courier', 18))
label.place(relwidth=1, relheight=1)

bg_color = 'cornflower blue'
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=40, bg=bg_color)
results.place(relwidth=1, relheight=1)

button_two = tk.Button(
    frame,
    text='Search Restaurant',
    font=15, bg='light goldenrod',
    command=lambda: get_by_restaurant(
        textbox.get()))
button_two.place(relx=0.7, relheight=1, relwidth=0.3)

quitButton = tk.Button(  # This is to allow the user to close window via on screen button
    window, text="Exit", font=2,  bg='firebrick1',
    command=window.quit)
quitButton.place(relx=0.9, rely=0, relheight=0.099, relwidth=0.1)


clock = tk.Label(window, font=('Courier', 24, 'bold'))  # Adjusts the clock on GUI
clock.place(relx=0, rely=0, relheight=0.099)
tick()


# ADDITIONAL WIDGETS FOR USER-INTERFACE SUPPORT

menu = Menu(window)

editMenu = Menu(menu)
menu.add_cascade(label="About", menu=editMenu)
editMenu.add_command(label="Made for searching caloric content in foods and viewing live restaurant menus.")

window.config(menu=menu)

subMenu = Menu(menu)  # This is to help user understand about the programs purpose
menu.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="1. Type in entry box i.e. pizza")  # adding menu to drop down subMenu
subMenu.add_command(label="2. Click on the search type of choice")
subMenu.add_separator()  # creates a separator on the drop down list
subMenu.add_command(label="Click exit button to close window")


window.mainloop()
