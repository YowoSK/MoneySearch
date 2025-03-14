"""
Author: Filip Šulík
Date: February 2025
Description: This script performs automated searches on Bing using random words and strings.
Version: 1.1.1
License: MIT
Dependencies: 
    - pyautogui
    - nltk
Usage: 
    1. Ensure all dependencies are installed.
    2. Run the script using 'python search_bing.py' or start_search.sh or .bat
"""

import webbrowser
import random
import time
import os
import logging
import tkinter as tk
from tkinter import messagebox

try:
    import pyautogui
except ModuleNotFoundError:
    print("pyautogui module is not installed. Please install it using 'pip install pyautogui'")
    exit()

try:
    import nltk
    from nltk.corpus import words
    nltk.download('words')
    english_words = words.words()
except ModuleNotFoundError:
    print("nltk module is not installed. Please install it using 'pip install nltk'")
    english_words = []
except Exception as e:
    print(f"An error occurred while downloading or loading nltk words: {e}")
    english_words = []

# Configure logging
logging.basicConfig(filename='search_bing.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_string(length):
    randomadded = 'abcdefghijklmnopqrstuvwxyz123456789'
    return ''.join(random.choice(randomadded) for i in range(length))

def get_user_input(prompt, default):
    user_input = input(f"{prompt} (default: {default}): ")
    return type(default)(user_input) if user_input else default

def get_search_speed():
    print("Choose search speed preset:")
    print("slow - Slow")
    print("medium - Medium")
    print("fast - Fast")
    speed_choice = input("Enter your choice: ").lower()
    if speed_choice == 'slow':
        return 2, 0.1, 0.2, 2  # Slow: search_delay, type_delay_min, type_delay_max, tab_close_delay
    elif speed_choice == 'medium':
        return 1, 0.05, 0.1, 1  # Medium
    elif speed_choice == 'fast':
        return 0.5, 0.01, 0.05, 0.5  # Fast
    else:
        print("Invalid choice. Defaulting to Medium speed.")
        return 1, 0.05, 0.1, 1

def perform_searches(num_searches, search_delay, type_delay_min, type_delay_max, tab_close_delay):
    try:
        if os.name == 'nt':  # Windows
            edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
        else:  # Linux
            edge_path = '/usr/bin/edge %s'
        browser = webbrowser.get(edge_path)
    except webbrowser.Error as e:
        logging.error(f"An error occurred while getting the browser: {e}")
        exit()

    try:
        random.shuffle(english_words)
        unique_real_words = english_words[:num_searches]
    except Exception as e:
        logging.error(f"An error occurred while shuffling or slicing the words list: {e}")
        unique_real_words = []

    open_tabs = 0

    try:
        for real_word in unique_real_words:
            random_string = generate_random_string(10)
            search_query = real_word + " " + random_string

            try:
                browser.open_new_tab('https://www.bing.com')
                open_tabs += 1
                logging.info(f"Opened new tab for search query: {search_query}")
            except Exception as e:
                logging.error(f"An error occurred while opening a new tab: {e}")
                continue

            time.sleep(search_delay)

            try:
                for char in search_query:
                    pyautogui.typewrite(char)
                    time.sleep(random.uniform(type_delay_min, type_delay_max))
                pyautogui.press('enter')
                logging.info(f"Typed and submitted search query: {search_query}")
            except Exception as e:
                logging.error(f"An error occurred while typing the search query: {e}")
                continue

            time.sleep(tab_close_delay)

            if open_tabs > 1:
                try:
                    pyautogui.hotkey('ctrl', '1')
                    time.sleep(tab_close_delay)
                    pyautogui.hotkey('ctrl', 'w')
                    open_tabs -= 1
                    logging.info("Closed a tab")
                except Exception as e:
                    logging.error(f"An error occurred while closing a tab: {e}")
                    continue

    except KeyboardInterrupt:
        logging.info("Script stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def start_search():
    try:
        if not any([search_delay_var.get(), type_delay_min_var.get(), type_delay_max_var.get(), tab_close_delay_var.get()]):
            messagebox.showerror("Preset not selected", "Please select a speed preset before starting the search.")
            return

        num_searches = int(num_searches_entry.get())
        search_delay = float(search_delay_var.get())
        type_delay_min = float(type_delay_min_var.get())
        type_delay_max = float(type_delay_max_var.get())
        tab_close_delay = float(tab_close_delay_var.get())

        confirmation = messagebox.askyesno("Confirmation", "This script will perform automated searches on Bing. Do you want to proceed?")
        if confirmation:
            perform_searches(num_searches, search_delay, type_delay_min, type_delay_max, tab_close_delay)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid values.")

def set_preset(preset):
    if preset == 'slow':
        search_delay_var.set(2)
        type_delay_min_var.set(0.1)
        type_delay_max_var.set(0.2)
        tab_close_delay_var.set(2)
        update_button_colors('slow')
    elif preset == 'medium':
        search_delay_var.set(1)
        type_delay_min_var.set(0.05)
        type_delay_max_var.set(0.1)
        tab_close_delay_var.set(1)
        update_button_colors('medium')
    elif preset == 'fast':
        search_delay_var.set(0.5)
        type_delay_min_var.set(0.01)
        type_delay_max_var.set(0.05)
        tab_close_delay_var.set(0.5)
        update_button_colors('fast')

def update_button_colors(active_preset):
    slow_button.config(bg=button_bg_color if active_preset != 'slow' else active_button_color)
    medium_button.config(bg=button_bg_color if active_preset != 'medium' else active_button_color)
    fast_button.config(bg=button_bg_color if active_preset != 'fast' else active_button_color)

# GUI setup
root = tk.Tk()
root.title("Bing Search Automation")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Enter the number of searches:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
num_searches_entry = tk.Entry(root)
num_searches_entry.grid(row=0, column=1, padx=10, pady=10)

search_delay_var = tk.DoubleVar()
type_delay_min_var = tk.DoubleVar()
type_delay_max_var = tk.DoubleVar()
tab_close_delay_var = tk.DoubleVar()

button_bg_color = "#4682b4"
button_fg_color = "whitesmoke"
active_button_color = "#27408b"  # color for active preset

preset_frame = tk.Frame(root, bg="#f0f0f0")
preset_frame.grid(row=1, column=0, columnspan=2, pady=10)

slow_button = tk.Button(preset_frame, text="Slow Preset\n(fakt pomalé)", command=lambda: set_preset('slow'), bg=button_bg_color, fg=button_fg_color, padx=20, pady=10)
slow_button.pack(side=tk.LEFT, padx=10)
medium_button = tk.Button(preset_frame, text="Medium Preset\n(default)", command=lambda: set_preset('medium'), bg=button_bg_color, fg=button_fg_color, padx=20, pady=10)
medium_button.pack(side=tk.LEFT, padx=10)
fast_button = tk.Button(preset_frame, text="Fast Preset\n(neodporúčam)", command=lambda: set_preset('fast'), bg=button_bg_color, fg=button_fg_color, padx=20, pady=10)
fast_button.pack(side=tk.LEFT, padx=10)

tk.Button(root, text="Start", command=start_search, bg=button_bg_color, fg=button_fg_color, padx=20, pady=10).grid(row=2, column=0, columnspan=2, pady=20)

if __name__ == "__main__":
    try:
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except Exception as e:
        logging.error(f"An error occurred while hiding the console window: {e}")

    root.mainloop()