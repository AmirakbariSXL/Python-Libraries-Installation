import subprocess
import sys

#requirements.txt
def install_libraries(requirements_file='requirements.txt'):
    try:
        #requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print("تمام کتابخانه‌ها با موفقیت نصب شدند.")
    except subprocess.CalledProcessError as e:
        print(f"خطا در نصب کتابخانه‌ها: {e}")
        
if __name__ == "__main__":
    install_libraries()