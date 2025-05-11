import os
import sys

# === Define your variables ===
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'C:\\Application\\antlr4.9.2\\antlr4-4.9.2-complete.jar'  # Update if needed
CPL_Dest = os.path.join(DIR, 'CompiledFiles')
SRC = os.path.join(DIR, 'Finance.g4')

def generate():
    if not os.path.exists(CPL_Dest):
        os.makedirs(CPL_Dest)
    os.system(f'java -jar "{ANTLR_JAR}" -Dlanguage=Python3 -o "{CPL_Dest}" "{SRC}"')
    print("Generated parser successfully.")

def run_chatbot():
    import chatbot
    chatbot.main()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python run.py [gen|test]")
    elif sys.argv[1] == "gen":
        generate()
    elif sys.argv[1] == "test":
        run_chatbot()
