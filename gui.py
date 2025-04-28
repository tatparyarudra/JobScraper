import tkinter as tk
from tkinter import ttk
from scraper import scrape_remoteok

def fetch_jobs():
    keyword = entry_keyword.get()
    jobs = scrape_remoteok(keyword)

    print(f"Displaying {len(jobs)} jobs")  # debug

    # Clear old entries
    for row in tree.get_children():
        tree.delete(row)

    # Add new entries
    for job in jobs:
        tree.insert("", "end", values=(job["Title"], job["Company"], job["Location"]))

# GUI setup
root = tk.Tk()
root.title("Remote OK Job Scraper")

frame_search = tk.Frame(root)
frame_search.pack(pady=10)

label_keyword = tk.Label(frame_search, text="Job Keyword:")
label_keyword.pack(side=tk.LEFT)

entry_keyword = tk.Entry(frame_search, width=30)
entry_keyword.pack(side=tk.LEFT, padx=5)

button_search = tk.Button(frame_search, text="Search", command=fetch_jobs)
button_search.pack(side=tk.LEFT)

tree = ttk.Treeview(root, columns=("Title", "Company", "Location"), show="headings")
tree.heading("Title", text="Job Title")
tree.heading("Company", text="Company")
tree.heading("Location", text="Location")
tree.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
