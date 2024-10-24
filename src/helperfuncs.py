from imports import pd
from imports import ttk

# Helper function to search in DataFrame
def is_name_in_csv(search_term, df):
    if isinstance(df, pd.DataFrame):
        mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
        return df.loc[mask]
    else:
        return pd.DataFrame()  # Return an empty DataFrame

from RecipeWindowFrames import root

# TreeView setup
tree = ttk.Treeview(root, columns=['title', 'ingredients', 'directions', 'link', 'source', 'NER'], show='headings')
tree.pack()

# Populate TreeView
def populate_treeview():
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))
