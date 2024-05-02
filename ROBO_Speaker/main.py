import os

if __name__ == '__main__':
    print("Welcome to ROBO_Speaker. ");
    x = input("Enter sentence to speak : ")
    command = f"mshta (""SAPI.SpVoice"").Speak {x})"
    
    os.system(command)