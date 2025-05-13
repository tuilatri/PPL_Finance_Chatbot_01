import os
import sys

# === Define your variables ===
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'C:\\Application\\antlr4.9.2\\antlr4-4.9.2-complete.jar'  # Update if needed
CPL_Dest = os.path.join(DIR, 'CompiledFiles')
SRC = os.path.join(DIR, 'Finance.g4')
# "C:\\Application\\antlr4\\antlr-4.13.2-complete.jar"
def generate():
    if not os.path.exists(ANTLR_JAR):
        print(f"Error: ANTLR JAR not found at {ANTLR_JAR}")
        sys.exit(1)
    if not os.path.exists(SRC):
        print(f"Error: Grammar file not found at {SRC}")
        sys.exit(1)
    if not os.path.exists(CPL_Dest):
        os.makedirs(CPL_Dest)
    os.system(f'java -jar "{ANTLR_JAR}" -Dlanguage=Python3 -o "{CPL_Dest}" "{SRC}"')
    print("Generated parser successfully.")

def run_chatbot():
    try:
        import chatbot
        chatbot.main()
    except ImportError:
        print("Error: chatbot.py not found or CompiledFiles not generated. Run 'python run.py gen' first.")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python run.py [gen|test]")
        sys.exit(1)
    elif sys.argv[1] == "gen":
        generate()
    elif sys.argv[1] == "test":
        run_chatbot()
    else:
        print("Invalid argument. Use 'gen' or 'test'.")
        sys.exit(1)