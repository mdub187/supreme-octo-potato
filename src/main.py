from imports import *

import RecipeWindowFrames
# definitions
df = pd.read_csv('recipes_data.csv')
print(RecipeWindowFrames)

import RecipeButtons
print(RecipeButtons)

import helperfuncs
print(helperfuncs)

# Start the GUI
from RecipeWindowFrames import root
root.mainloop()
