import webbrowser
import random
import time
import os

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

def generate_random_string(length):
    randomadded = 'abcdefghijklmnopqrstuvwxyz123456789'
    return ''.join(random.choice(randomadded) for i in range(length))

def get_user_input(prompt, default):
    user_input = input(f"{prompt} (default: {default}): ")
    return type(default)(user_input) if user_input else default

# Configuration
num_searches = get_user_input("Enter the number of searches", 90)
search_delay = get_user_input("Enter the delay between searches in seconds", 1)
type_delay_min = get_user_input("Enter the minimum delay between typing characters", 0.05)
type_delay_max = get_user_input("Enter the maximum delay between typing characters", 0.1)
tab_close_delay = get_user_input("Enter the delay before closing a tab", 1)

try:
    if os.name == 'nt':  # Windows
        edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
    else:  # Linux
        edge_path = '/usr/bin/edge %s'
    browser = webbrowser.get(edge_path)
except webbrowser.Error as e:
    print(f"An error occurred while getting the browser: {e}")
    exit()

try:
    random.shuffle(english_words)
    unique_real_words = english_words[:num_searches]
except Exception as e:
    print(f"An error occurred while shuffling or slicing the words list: {e}")
    unique_real_words = []

open_tabs = 0

try:
    for real_word in unique_real_words:
        random_string = generate_random_string(10)
        
        search_query = real_word + " " + random_string
        
        try:
            browser.open_new_tab('https://www.bing.com')
            open_tabs += 1
        except Exception as e:
            print(f"An error occurred while opening a new tab: {e}")
            continue
        
        time.sleep(search_delay)
        
        try:
            for char in search_query:
                pyautogui.typewrite(char)
                time.sleep(random.uniform(type_delay_min, type_delay_max))
            pyautogui.press('enter')
        except Exception as e:
            print(f"An error occurred while typing the search query: {e}")
            continue
        
        time.sleep(tab_close_delay)
        
        if open_tabs > 1:
            try:
                pyautogui.hotkey('ctrl', '1')
                time.sleep(tab_close_delay)
                pyautogui.hotkey('ctrl', 'w')
                open_tabs -= 1
            except Exception as e:
                print(f"An error occurred while closing a tab: {e}")
                continue

except KeyboardInterrupt:
    print("Script stopped.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")