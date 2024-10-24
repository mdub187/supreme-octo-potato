from imports import CTk
from RecipeWindowFrames import my_text, my_frame


# Delete function
def delete():
    my_text.delete(0.0, 'end')

# Search function
def insert_text_in_chunks(text_widget, text, chunk_size=1000):
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        text_widget.insert('end', chunk)

from helperfuncs import is_name_in_csv, df

def search():
    search_term = my_text.get("1.0", 'end-1c').strip()  # Get the text from the textbox
    if search_term:
        results = is_name_in_csv(search_term, df)
        if not results.empty:
            my_text.delete(0.0, 'end')  # Clear the Textbox
            insert_text_in_chunks(my_text, results.to_string())  # Insert the search results in chunks
        else:
            my_text.insert('end', f"No results found for: {search_term}")
    else:
        my_text.insert('end', "Please enter a search term.")



# Add buttons
delete_button = CTk.CTkButton(my_frame, text="Delete", command=delete)
search_button = CTk.CTkButton(my_frame, text="Search", command=search)
delete_button.grid(row=0, column=0)
search_button.grid(row=0, column=1, padx=10)
