import subprocess
import os
import sys
runner_path = os.path.join(os.path.dirname(__file__), 'Runner.exe')
lock_file_path = os.path.join(os.path.dirname(__file__), 'runner.lock')

with open('Game.Path', 'r') as game_path_file:
    game_path = game_path_file.read().strip()
if os.path.exists(lock_file_path):
    print("The program is already running!")
    sys.exit()
with open(lock_file_path, 'w') as lock_file:
    lock_file.write("")
try:
    process = subprocess.Popen([runner_path, '-game', game_path])
    print("Game running!")
    process.wait()
except Exception as e:
    print(f"Error has occurred: {e}")
finally:
    if os.path.exists(lock_file_path):
        try:
            os.remove(lock_file_path)
        except Exception as e:
            print(f"Failed to delete .lock file: {e}")
sys.exit()