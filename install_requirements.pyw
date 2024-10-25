import os
import subprocess
import sys


directory = os.path.dirname(os.path.abspath(__file__))

requirements_file = os.path.join(directory, 'requirements.txt')


subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
