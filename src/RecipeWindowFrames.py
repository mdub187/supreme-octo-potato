from imports import CTk


# Set up the customtkinter window
CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")
root = CTk.CTk()
root.title('Recipe Buddy')
root.geometry('700x300')

# Create the Textbox to display results
my_text = CTk.CTkTextbox(root, width=600, height=200)
my_text.pack(pady=20)

# Create a frame for buttons
my_frame = CTk.CTkFrame(root)
my_frame.pack(pady=10)
