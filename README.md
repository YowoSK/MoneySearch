# Bing Search Automation

This project automates searching random words on Bing using Microsoft Edge. It uses the `nltk` library to get a list of English words and the `pyautogui` library to simulate typing and browser interactions.

## Prerequisites

- Python 3.x
- Microsoft Edge
- `pip` (Python package installer)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/bing-search-automation.git
    cd bing-search-automation
    ```

2. **Install the required Python packages:**
    ```sh
    python -m pip install -r requirements.txt
    ```

    If `requirements.txt` is not available, you can install the packages individually:
    ```sh
    python -m pip install nltk pyautogui
    ```

3. **Download the NLTK words corpus:**
    ```sh
    python -c "import nltk; nltk.download('words')"
    ```

## Usage

1. **Run the script:**
    ```sh
    python search_bing.py
    ```

2. **Stop the script:**
    Press `Ctrl+C` in the terminal to stop the script gracefully.

## Script Details

- The script opens Microsoft Edge and performs searches on Bing.
- It generates random search queries by combining a real English word with a random string.
- It types the search query character by character with a random delay.
- It handles multiple tabs and closes the oldest tab if more than one tab is open.
- It handles keyboard interrupts to stop the script gracefully.

## Troubleshooting

- If you encounter a `ModuleNotFoundError`, ensure that the required packages are installed.
- If `pip` is not recognized, ensure that Python and `pip` are added to your system PATH.

## License

This project is licensed under the MIT License. See the LICENSE file for details.