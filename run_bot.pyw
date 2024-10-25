import os
import subprocess


directory = os.path.dirname(os.path.abspath(__file__))
# Path to main.py
main_script = os.path.join(directory, 'main.py')


subprocess.run(['python', main_script])
