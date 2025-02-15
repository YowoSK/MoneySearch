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

## Step-by-Step Guide for Beginners

### Step 1: Install Python

1. Download Python from the official website: https://www.python.org/downloads/
2. Run the installer and follow the instructions. Make sure to check the box that says "Add Python to PATH".

### Step 2: Install Microsoft Edge

1. Download Microsoft Edge from the official website: https://www.microsoft.com/edge
2. Install Microsoft Edge by following the instructions on the website.

### Step 3: Install Git

1. Download Git from the official website: https://git-scm.com/downloads
2. Run the installer and follow the instructions.

### Step 4: Clone the Repository

1. Open a terminal or command prompt.
2. Run the following command to clone the repository:
    ```sh
    git clone https://github.com/yourusername/bing-search-automation.git
    cd bing-search-automation
    ```

### Step 5: Install Required Python Packages

1. In the terminal or command prompt, run the following command to install the required packages:
    ```sh
    python -m pip install -r requirements.txt
    ```

    If `requirements.txt` is not available, you can install the packages individually:
    ```sh
    python -m pip install nltk pyautogui
    ```

### Step 6: Download the NLTK Words Corpus

1. In the terminal or command prompt, run the following command to download the NLTK words corpus:
    ```sh
    python -c "import nltk; nltk.download('words')"
    ```

### Step 7: Run the Script

1. In the terminal or command prompt, run the following command to start the script:
    ```sh
    python search_bing.py
    ```

2. To stop the script, press `Ctrl+C` in the terminal or command prompt.

### Troubleshooting

- If you encounter a `ModuleNotFoundError`, ensure that the required packages are installed by following Step 5.
- If `pip` is not recognized, ensure that Python and `pip` are added to your system PATH by following Step 1.

## Creating an Executable

To create an executable file from the script, follow these steps:

### Step 1: Install PyInstaller

1. Open a terminal or command prompt.
2. Run the following command to install PyInstaller:
    ```sh
    python -m pip install pyinstaller
    ```

### Step 2: Create the Executable

1. Navigate to the directory containing your script:
    ```sh
    cd /d:/Filip/prog/MoneySearch
    ```
2. Run the following command to create the executable:
    ```sh
    pyinstaller --onefile --clean --noupx search_bing.py
    ```

This will generate a `dist` directory containing the `search_bing.exe` file.

### Step 3: Distribute the Executable

1. Navigate to the `dist` directory:
    ```sh
    cd dist
    ```
2. You will find the `search_bing.exe` file there. You can distribute this file to users, and they will be able to run it without needing to install Python or any dependencies.

### Handling Antivirus Issues

If Windows Defender or another antivirus software flags the executable as a virus, you can try the following steps:

1. **Sign the Executable**: Use a code signing certificate from a trusted certificate authority (CA) to sign the executable.
2. **Add an Exception**: Add an exception in Windows Defender for the specific file or folder:
    - Open Windows Security.
    - Go to "Virus & threat protection".
    - Click on "Manage settings" under "Virus & threat protection settings".
    - Scroll down to "Exclusions" and click on "Add or remove exclusions".
    - Add the folder or file you want to exclude.