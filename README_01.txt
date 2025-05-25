# International University  
**Vietnam National University - Ho Chi Minh City**  

## Course: Principle of Programming Language  
**Topic:** Finance Chatbot

---

## Team Members
- Hà Minh Trí - ITCSIU22194  
- Đỗ Hùng Việt - ITCSIU22197  
- Nguyễn Anh Trí - ITCSIU22152 *(Leader)*  
- Phan Đức Trí - ITCSIU22151  

---

## Repository Purpose
This repository is designed to handle the logic and grammar processing for a Finance Chatbot using ANTLR and Python.

### Responsible for:
- Hà Minh Trí - ITCSIU22194  
- Đỗ Hùng Việt - ITCSIU22197  

---

## Chatbot Commands

The chatbot accepts the following commands and records actions in `finance_record.txt`:

### Input salary in different currency:
- **Command:**
  `i have 10.000 cny`
  `i have 10.000 jpy`
  `i have 10.000 usd`
  `i have 10.000 vnd`
  `i have 10.000 eur`
- **Sample:**
(here will be an image with the link from folder /image)

### Creating spending category(ies)
- **Command:**
  `i want to have 1.000 USD for Renting, 1.000 CNY for Food, 1.000 EUR for Clothes, 1.000 JPY for Emergency`
- **Sample:**
(here will be an image with the link from folder /image)

### Using
- **Command:**
  `i used 10.000 jpy for Pho`
  `i used 100.000 vnd for Repair in Emergency`
- **Sample:**
(here will be an image with the link from folder /image)

### Changing
- **Command:**
  `change the money for Food to 1.000 eur`
- **Sample:**
(here will be an image with the link from folder /image)

### Delete
- **Command:**
  `delete Clothes`
- **Sample:**
(here will be an image with the link from folder /image)

### Resetting
- **Command:**
  `reset`
- **Sample:**
(here will be an image with the link from folder /image)

### Analyzing
- **Command:**
  `analyzing`
- **Sample:**
(here will be an image with the link from folder /image)

### Showing Graph
- **Command:**
  `graph`
- **Sample:**
(here will be an image with the link from folder /image)

### Exitting
- **Command:**
  `exit`
- **Sample:**
(here will be an image with the link from folder /image)

---

## How to run
1. Requirements: 
- I have put some files that you should download first in the requirements folder.
- Python: Version 3.12.10
- Antlr4: Version 4.9.2

2. Clone Project:
- Turn on your terminal
- Direct to the folder that you want
- git clone https://github.com/tuilatri/PPL_Finance_Chatbot_01.git

3. Identify the path of requirements' files

4. Create virtual environment:
- ____\python.exe -m venv venv (replace ____ with your python's path)

5. Use virtual environment:
- .\venv\Scripts\Activate.ps1

6. Download dependencies:
- python -m pip install spacy==3.8.2 antlr4-python3-runtime==4.9.2
- python -m spacy download en_core_web_sm
- python -m pip install matplotlib

7. Check dependencies:
- python -m pip list

8. Run:
- python run.py gen
- python run.py test

---

## Functions:
- Parse Natural Language Input: Uses ANTLR (Finance.g4, parser.py) to tokenize and parse user commands (e.g., i have 10.000 usd, i used 10.000 jpy for Pho) into structured intents, supporting Vietnamese number format (e.g., 10.000.000) and category inference (e.g., “Pho” → “Food”).
- Support Multiple Currencies: Converts amounts in VND, USD, EUR, JPY, CNY to VND using fixed exchange rates (utils.py), storing original amounts and currencies in finance_record.txt (e.g., 250.000.000 VND (10.000 USD)).
- Handle User-Friendly Commands: Processes intuitive commands (chatbot.py, Finance.g4) for adding salary, allocating/spending money, modifying/deleting categories, resetting data, analyzing spending, and visualizing graphs, with synonyms (e.g., graph/show graph).
- Visualize Spending by Category: Generates a pie chart (visualizer.py) in a pop-up window (6x4 inches, customizable) showing spending proportions (e.g., Food: 94.4%) with a legend, white 12-point percentage text, and startangle=140.
- Provide Financial Advice: Analyzes spending patterns (advisor.py) using spacy NLP to offer advice on high spending (>50% of salary), unallocated funds (>70%), frequent items, and balanced spending, with entity recognition (e.g., “Pho” as PRODUCT).
- Persist Data: Stores financial data (salary, categories, actions) in finance_record.txt (utils.py) with VND formatting (e.g., 10.000.000) and detailed action logs for persistence across sessions.

---

## Notes
- All commands must follow the specified format.
- The chatbot may output parsing warnings due to the custom grammar, but will still proceed with valid commands.
- The grammar file `Finance.g4` defines the structure of acceptable commands, and `chatbot.py` manages the logic and interaction.

---
