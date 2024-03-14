import tkinter as tk
from tkinter import messagebox
import pyperclip
import requests

def shorten_url():
    long_url = url_entry.get()
    api_url = 'https://tinyurl.com/api-create.php?url='
    response = requests.get(api_url + long_url)
    if response.status_code == 200:
        short_url = response.text
        shortened_url_label.config(text=f'Shortened URL: {short_url}')
        shortened_url_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky='nsew')
        copy_button.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky='nsew')
    else:
        messagebox.showerror('Error', 'Failed to shorten URL')

def copy_to_clipboard():
    short_url = shortened_url_label.cget('text').split(': ')[1]
    pyperclip.copy(short_url)
    messagebox.showinfo('Success', 'Shortened URL copied to clipboard')

# Create the main application window
app = tk.Tk()
app.title('SnipSnap - URL Shortener')

# Create widgets
url_label = tk.Label(app, text='Enter URL:', font=("Arial", 14))
url_entry = tk.Entry(app, width=40, font=("Arial", 14))
shorten_button = tk.Button(app, text='Shorten', command=shorten_url, font=("Arial", 14))
shortened_url_label = tk.Label(app, text='', font=("Arial", 14))

copy_button = tk.Button(app, text='Copy URL', command=copy_to_clipboard, font=("Arial", 14))

# Arrange widgets using grid layout
url_label.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')
url_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky='nsew')
shorten_button.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky='nsew')

# Run the application
app.mainloop()
