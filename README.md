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

### Add
- **Example:**  
  `Food: Milktea (50.000 VND)`

### Change
- **Example:**  
  `Change Food (2.000.000 VND)`

### Delete
- **Example:**  
  `Delete Food`

### Reset
- **Example:**  
  `Reset`

---

## Notes
- All commands must follow the specified format.
- The chatbot may output parsing warnings due to the custom grammar, but will still proceed with valid commands.
- The grammar file `Finance.g4` defines the structure of acceptable commands, and `chatbot.py` manages the logic and interaction.

---

