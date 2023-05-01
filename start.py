import subprocess

# Run the "chmod 777" commands

subprocess.Popen(["chmod", "777", "bombsquad_server"])

subprocess.Popen(["chmod", "777", "bs_headless"])

# Run the "./bombsquad_server" command

subprocess.Popen(["./bombsquad_server"])

