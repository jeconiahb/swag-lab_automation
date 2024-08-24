
# Selenium Automation with Python

This project uses Selenium with Python for web browser automation. Follow these steps to get started.

## Prerequisites

- **Python 3.x**: [Download and install Python](https://www.python.org/downloads/).
- **WebDriver**: Browser driver for Selenium

## Setup Instructions

### 1. Clone this repo locally

### 2. Install Selenium

Open your terminal and run:

```bash
pip install selenium
```
### 3. Download WebDriver

- **ChromeDriver**: [Download here](https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.84/win64/chromedriver-win64.zip)

Place the WebDriver executable in a directory that's in your system's PATH, or specify the path in your scripts.

### 4. Verify Installation

Create a Python script to check WebDriver:

```python
from selenium import webdriver

driver = webdriver.Chrome()  # Use webdriver.Firefox() for Firefox
driver.get('https://www.google.com')
driver.quit()
```

Run the script to ensure WebDriver is working.


## Running Tests

Execute your tests with:

```bash
python run_all.py
```
