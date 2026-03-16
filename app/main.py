import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == '__main__':
    from app.infrastructure.user_interfaces.console.console import ConsoleUI
    console = ConsoleUI()
    console.start()