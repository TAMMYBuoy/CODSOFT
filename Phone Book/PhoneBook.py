import tkinter as tk
from tkinter import messagebox
import json
import os
import tkinter as tk
from tkinter import *
from random import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import PhotoImage
from itertools import cycle

root = tk.Tk()
root.geometry("400x600")

#class AnimatedGIFBackground:
#    def __init__(self, root, gif_path):
#        self.root = root
#        self.gif_path = gif_path
#        self.frames = self.load_frames()
#        self.frames_cycle = cycle(self.frames)
#        self.current_frame = None
#        self.bg_label = tk.Label(root)
#        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
#        self.update_frame()
#
#    def load_frames(self):
#        # Load the GIF and iterate over its frames
#        frames = []
#        gif = PhotoImage(file=self.gif_path)
#        try:
#            for i in range(100):  # Assuming the GIF has fewer than 100 frames
#                frame = PhotoImage(file=self.gif_path, format=f"gif -index {i}")
#                frames.append(frame)
#        except tk.TclError:
#            pass  # Reached the end of the GIF frames
#        return frames
#
#    def update_frame(self):
#        if self.frames:
#            self.current_frame = next(self.frames_cycle)  # Get the next frame
#            self.bg_label.config(image=self.current_frame)
#            self.root.after(100, self.update_frame)


class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts_file = "contacts.txt"  # File where contacts will be stored
        self.contacts = self.load_contacts()
        self.load_contacts()

        # Load the background GIF
        self.bg_image = tk.PhotoImage(file="photos/CZk.gif")
        
        # Create a canvas for the background
        self.bg_canvas = Canvas(root, width=400, height=600)
        self.bg_canvas.pack(fill="both", expand=True)
        
        # Set the GIF as the background
        self.bg_canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        
        # Now create a frame for your content that will be placed on top of the canvas
        self.center_frame = tk.Frame(self.bg_canvas)
        self.center_frame_window = self.bg_canvas.create_window(200, 300, window=self.center_frame, anchor="center")
        self.setup_ui()


        # Create a frame that will hold all content and center it
        self.center_frame = tk.Frame(root)
        self.center_frame.pack( side="top", )






        ###################animated_bg = AnimatedGIFBackground(root, "photos/CZk.gif")










        # Set up the UI components within the center frame
        self.setup_ui()

    def setup_ui(self):
        # First Name Field
        tk.Label(self.center_frame, text='First Name:').grid(row=0, column=0, pady=10,padx=20, sticky="w", )
        self.first_name_var = tk.StringVar()
        tk.Entry(self.center_frame, textvariable=self.first_name_var, width=20).grid(row=0, column=1, pady=10, sticky="w")

        # Last Name Field
        tk.Label(self.center_frame, text='Last Name:').grid(row=1,padx=20, column=0, pady=10, sticky="w")
        self.last_name_var = tk.StringVar()
        tk.Entry(self.center_frame, textvariable=self.last_name_var, width=20).grid(row=1, column=1, pady=10)

        # Phone Field
        tk.Label(self.center_frame, text='Phone:').grid(row=2,padx=20, column=0, pady=10, sticky="w")
        self.phone_var = tk.StringVar()
        tk.Entry(self.center_frame, textvariable=self.phone_var, width=20).grid(row=2, column=1, pady=10)

        # Email Field
        tk.Label(self.center_frame, text='Email:').grid(row=3,padx=20, column=0, pady=10, sticky="w")
        self.email_var = tk.StringVar()
        tk.Entry(self.center_frame, textvariable=self.email_var, width=20).grid(row=3, column=1, pady=10)

        # Add Contact Button
        tk.Button(self.center_frame, text='Add Contact', command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)

        # Search Field and Button
        tk.Label(self.center_frame, text='Search by First Name:').grid(row=5,padx=20, column=0, pady=10, sticky="w")
        self.search_var = tk.StringVar()
        tk.Entry(self.center_frame, textvariable=self.search_var, width=20).grid(row=5, column=1, pady=10)
        tk.Button(self.center_frame, text='Search', command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=10)

        # Contact Display Frame
        self.contact_display_frame = tk.Frame(self.center_frame)
        self.contact_display_frame.grid(row=7, column=0, columnspan=2, pady=10)

    def add_contact(self):
        first_name = self.first_name_var.get().strip()
        last_name = self.last_name_var.get().strip()
        phone = self.phone_var.get().strip()
        email = self.email_var.get().strip()

        if first_name and phone and email:  # Assuming last name is optional
            full_name = f"{first_name} {last_name}".strip()
            self.contacts[full_name] = {'First Name': first_name, 'Last Name': last_name, 'Phone': phone, 'Email': email}
            self.clear_entry_fields()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "First Name, Phone, and Email are required fields.")

    def search_contact(self):
        search_name = self.search_var.get().strip()
        found = False
        for name, info in self.contacts.items():
            if info['First Name'].lower() == search_name.lower():
                self.display_contact_info(name, info)
                found = True
                break
        if not found:
            messagebox.showerror("Not Found", "Contact not found.")

    def display_contact_info(self, name, info):
        for widget in self.contact_display_frame.winfo_children():
            widget.destroy()

        tk.Label(self.contact_display_frame, text=f"Name: {name}", font=("Arial", 12)).pack()
        tk.Label(self.contact_display_frame, text=f"Phone: {info['Phone']}", font=("Arial", 12)).pack()
        tk.Label(self.contact_display_frame, text=f"Email: {info['Email']}", font=("Arial", 12)).pack()

    def clear_entry_fields(self):
        self.first_name_var.set('')
        self.last_name_var.set('')
        self.phone_var.set('')
        self.email_var.set('')
        self.search_var.set('')




    def load_contacts(self):
        """Load contacts from a file."""
        try:
            if os.path.exists(self.contacts_file):
                with open(self.contacts_file, 'r') as file:
                    file_content = file.read()
                    if file_content:
                        self.contacts = eval(file_content)
                    print("Loaded contacts:", self.contacts)  # For debugging
            else:
                print("Contacts file does not exist. Starting with an empty contact list.")
        except Exception as e:
            print("Failed to load contacts:", e)

    def save_contacts(self):
        """Save contacts to a file."""
        try:
            with open(self.contacts_file, 'w') as file:
                file.write(repr(self.contacts))
                print("Saved contacts:", self.contacts)  # For debugging
        except Exception as e:
            print("Failed to save contacts:", e)

    def on_closing(self):
        """Handle the window closing event."""
        self.save_contacts()
        self.root.destroy()

if __name__ == "__main__":
    #root = tk.Tk()
    #root.geometry("400x600")
    app = ContactBook(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
