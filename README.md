# PRODIGY_CS_Task4


# Keylogger

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Disclaimer](#disclaimer)
6. [License](#license)

## Introduction
This Keylogger is a simple script that logs all keystrokes on a computer. It logs both alphanumeric and special keys with timestamps to a file named `keylog.txt`.

## Features
- Logs all alphanumeric and special keys with timestamps
- Saves logs to `keylog.txt`
- Handles errors by logging them to `errorlog.txt`

## Installation
### Prerequisites
- Python 3.x
- `pynput` library

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/keylogger.git
    ```
2. Navigate to the project directory:
    ```bash
    cd keylogger
    ```
3. Install the required dependencies:
    ```bash
    pip install pynput
    ```

## Usage
To run the Keylogger, execute the following command:

```bash
python keylogger.py
```

The keylogger will start running and logging keystrokes. Press `ESC` to stop the keylogger.

## Disclaimer
This tool is intended for educational purposes only. Unauthorized use of this keylogger to capture sensitive information is illegal and unethical. Use it responsibly and only on systems you own or have permission to monitor.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to adjust this template to fit any additional information or requirements specific to your project.
