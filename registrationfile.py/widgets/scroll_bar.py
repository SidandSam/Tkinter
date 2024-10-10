import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Scrollbar Example")

# Create a Text widget
text_widget = tk.Text(root, wrap='none')  # 'wrap=none' to prevent automatic line wrapping
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar and associate it with the Text widget
scrollbar = tk.Scrollbar(root, command=text_widget.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Configure the Text widget to use the scrollbar
text_widget.config(yscrollcommand=scrollbar.set)

# Insert some sample text
for i in range(100):
    text_widget.insert(tk.END, f"This is line number {i}\n")

# Run the application
root.mainloop()