import sys
import os
import re

import customtkinter as CTk
customtkinter = CTk
#from CTk import CTkTextbox
import customtkinter.windows

#import tkinter
from tkinter import ttk

import pandas as pd
#from pandas import columns
import urllib.request
from pandas.core.api import notnull
from pandas.core.indexes.datetimelike import RangeIndex
from pandas.core.series import pandas

# Data load and manipulation
def recipes_data():

#mysql.__file__.endswith(".csv")

    pd = df

# Load the CSV data into a DataFrame
#df = pd.read_csv#("recipes_data.csv", usecols=max)
# Load the CSV data into a DataFrame (move this out of the function)
chunk_size = 100  # Adjust this size to balance memory usage
df = pd.read_csv('recipes_data.csv')  # or use your path and settings
columns_needed = "100 rows x 7 columns"
RangeIndex = "start=0, stop=100, step=1",


#pd.Index=[('title', 'ingredients', 'directions', 'link', 'source', 'NER', 'site'] dtype='object')
columns_needed = ['title', 'ingredients', 'directions', 'link', 'source', 'NER', 'site']  # Adjust to your actual columns
    # Process each chunk
#from window2 import thing

# sample data
data = {
    'Recipe': ['Recipe 1', 'Recipe 2', 'Recipe 3'],
    'Source': ['Source 1', 'Source 2', 'Source 3'],
    'URL': ['http://source1.com', 'http://source2.com', 'http://source3.com'],
    'Ingredients': ["*, *, *"],
    'Cook Time': ['30 min', '45 min', '60 min']
}




# Set up the customtkinter window
CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")

root = CTk.CTk()
root.title('Recipe Buddy')
root.geometry('700x700')

# Create the Textbox to display results
my_text = CTk.CTkTextbox(root,
    width=2000,
    height=400,
    corner_radius=1,
    border_width=10,
    border_color="#003660",
    border_spacing=10,
    fg_color="silver",
    text_color="black",
    font=("Helvetica", 18),
    wrap="word",
    activate_scrollbars=True,
    scrollbar_button_color="blue",
    scrollbar_button_hover_color="red",
)
my_text.pack(pady=20)

# This code block is not needed and can be removed
        # Do your processing here for each chunk
#print(results)  # Example[(2231142 rows x 7 columns)> RangeIndex(start=0, stop=2231142, step=1) Index(['title', 'ingredients', 'directions', 'link', 'source', 'NER', 'site'] dtype='object')

# Create a frame for buttons
my_frame = CTk.CTkFrame(root)
my_frame.pack(pady=10)

# Function to delete content from the Textbox
def delete():
    my_text.delete(0.0, 'end')

# Function to perform the search
def search():
    search_term = my_text.get("1.0", 'end-1c').strip()  # Get the text from the textbox
    if search_term:
        results = is_name_in_csv(search_term, df)  # Call the search function with df
        if not results.empty:
            my_text.delete(0.0, 'end')  # Clear the Textbox
            my_text.insert('end', results.to_string())  # Display the search results
        else:
            my_text.insert('end', f"No results found for: {search_term}")
    else:
        my_text.insert('end', "Please enter a search term.")

# Helper function to check if a search term exists in the DataFrame
def is_name_in_csv(search_term, df):
    # Ensure df is a pandas DataFrame
    if isinstance(df, pd.DataFrame):
        return df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
    else:
        print("Error: df is not a DataFrame")
        return pd.DataFrame()  # Return an empty DataFrame if df is not valid

# 2nd window function
def open_new_window(root):
    new_window = CTk.CTkFrame(root)
    new_window.pack()


# Set up TreeView columns
tree = ttk.Treeview(root, columns=['title', 'ingredients', 'directions', 'link', 'source', 'NER'], show='headings')
tree.pack()

# Set up the Treeview headings and columns
for col in ['title', 'ingredients', 'directions', 'link', 'source', 'NER']:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Function to insert data into Treeview
def populate_treeview():
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

tree.pack()

# Add an event binding for item selection to open the URL
def on_tree_select(event):
    selected_item = tree.selection()[0]
    selected_url = tree.item(selected_item)['values'][2]  # Assuming URL is in the 3rd column
    webbrowser.open(selected_url)

tree.bind("<Double-1>", on_tree_select)


tree.pack()

# Select to choose recipe
def select():
    if urllib.request.HTTPHandler:
        import webbrowser
import webbrowser
def open_link(url):
    webbrowser.open(url)
if urllib.request.HTTPHandler:


# Modify the data insertion part in the Treeview setup
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))


# Function to fetch some source (demo placeholder)
def source():
    with urllib.request.urlopen('<some url>/') as response:
        html = response.read()
        my_text.insert('end', "Source content goes here.")  # Replace with actual data

# Add buttons
delete_button = CTk.CTkButton(my_frame, text="Delete", command=delete)
search_button = CTk.CTkButton(my_frame, text="Search", command=search)
source_button = CTk.CTkButton(my_frame, text="Source", command=source)
select_button = CTk.CTkButton(my_frame, text="Select", command=select)

select_button.grid(row=0, column=0)
delete_button.grid(row=0, column=1)
search_button.grid(row=0, column=2)
source_button.grid(row=0, column=3)

# Making the second window
from tkinter import Frame, Label

#def event 1
def event1(source_button):
    if event1:
        print(df.description.source)

#def event2
        def show_recipe_details(recipe):
            def event2(print_recipe):
                if event2:
                    print(detail_frame)
            if event2:
            # Hide current frame
                for widget in root.winfo_children():
                    widget.pack_forget()

    # Create a new frame for recipe details
        detail_frame = Frame(root)
        detail_frame.pack()

    # Show recipe details in the new frame
        Label(detail_frame, text=f"Details for {recipe}").pack()
        def event2(print_recipe):
            if event2:
                print(detail_frame)

#def event3
tree.bind("<Double-1>", on_tree_select)
def event3(source_button):
    if event3:
        on_tree_select_for_details=ttk.Treeview=Treeview.GetItem(Path).Rectangle
        selected_item = tree.selection()[0]
        selected_recipe = tree.item(selected_item)['values'][0]  # Assuming the recipe name is in the first column
        show_recipe_details(selected_recipe)
        tree.bind("<Double-1>", on_tree_select_for_details)

# Start the GUI
root.mainloop()
