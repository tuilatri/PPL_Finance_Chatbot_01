# International University  
**Vietnam National University - Ho Chi Minh City**  

## 📘 Course: Principles of Programming Languages  
**Project Title:** Finance Chatbot  

---

## 👥 Team Members
| Name               | Student ID     | Role     |
|--------------------|----------------|----------|
| Nguyễn Anh Trí     | ITCSIU22152    | Team Leader |
| Hà Minh Trí        | ITCSIU22194    | Developer |
| Đỗ Hùng Việt       | ITCSIU22197    | Developer |
| Phan Đức Trí       | ITCSIU22151    | Developer |

---

## 📂 Repository Purpose
This repository implements a **Finance Chatbot** that uses **ANTLR4** for grammar parsing and **Python** for handling user interactions, currency conversion, spending analysis, and visualization.

**Responsibilities:**
- Hà Minh Trí – ITCSIU22194  
- Đỗ Hùng Việt – ITCSIU22197  

---

## 💬 Chatbot Command Reference

The chatbot supports the following commands and logs actions in `finance_record.txt`.  
Each section includes a **command syntax** and a **sample screenshot** from the `/image` folder.

### 1. 💵 Input Salary (with currency)
**Command Examples:**
```bash
i have 10.000 vnd
i have 10.000 usd
i have 10.000 eur
i have 10.000 jpy
i have 10.000 cny
```
**Sample:**  
![Salary Input](images/salary_sample.jpg)

---

### 2. 🗂️ Create Spending Categories
**Command Example:**
```bash
i want to have 1.000 USD for Renting, 1.000 CNY for Food, 1.000 EUR for Clothes, 1.000 JPY for Emergency
```
**Sample:**  
![Create Categories](images/spending_categories_sample.jpg)

---

### 3. 💸 Record Spending
**Command Examples:**
```bash
i used 10.000 jpy for Pho
i used 100.000 vnd for Repair in Emergency
```
**Sample:**  
![Record Spending](images/spending_sample.jpg)

---

### 4. 🔄 Change Category Allocation
**Command Example:**
```bash
change the money for Food to 1.000 eur
```
**Sample:**  
![Change Category](images/changing_sample.jpg)

---

### 5. ❌ Delete Category
**Command Example:**
```bash
delete Clothes
```
**Sample:**  
![Delete Category](images/deleting_sample.jpg)

---

### 6. 🔃 Reset All Data
**Command:**
```bash
reset
```
**Sample:**  
![Reset Data](images/resetting_sample.jpg)

---

### 7. 📊 Analyze Spending
**Command:**
```bash
analyzing
```
**Sample:**  
![Analyze Spending](images/analyzing_sample.jpg)

---

### 8. 📈 Show Graph
**Command:**
```bash
graph
```
**Sample:**  
![Show Graph](images/showing_graph_sample.jpg)
![Show Graph](images/pie_chart_sample.jpg)

---

### 9. 🚪 Exit Program
**Command:**
```bash
exit
```
**Sample:**  
![Exit Program](images/exitting_sample.jpg)

---

## 🛠️ How to Run

### 1. Requirements
- Python 3.12.10  
- ANTLR4 4.9.2  
- Files in the `requirements` folder

### 2. Clone the Project
```bash
git clone https://github.com/tuilatri/PPL_Finance_Chatbot_01.git
```

### 3. Create Virtual Environment
```bash
<path_to_python>\python.exe -m venv venv
```

### 4. Activate Environment
```bash
.\venv\Scripts\Activate.ps1

```

### 5. Install Dependencies
```bash
python -m pip install spacy==3.8.2 antlr4-python3-runtime==4.9.2
python -m spacy download en_core_web_sm
python -m pip install matplotlib

```

### 6. Verify Installation
```bash
python -m pip list

```

### 7. Run the Chatbot
```bash
python run.py gen
python run.py test

```

---

## 🧠 Features
**Natural Language Parsing:**
Parses commands like i have 10.000 usd or i used 100.000 vnd for coffee using ANTLR (Finance.g4).

**Multi-Currency Support:**
Converts currencies (VND, USD, EUR, JPY, CNY) using fixed rates. Original values are kept in finance_record.txt.

**User-Friendly Commands:**
Allows intuitive interactions for salary input, budgeting, spending, resetting, and analysis.

**Data Visualization:**
Displays a pie chart (via matplotlib) showing spending distribution with percentages.

**Financial Analysis:**
Uses NLP (via spaCy) to analyze user data and provide advice on overspending or budgeting gaps.

**Persistent Logs:**
All actions are saved in finance_record.txt with formatted entries for continued use.
