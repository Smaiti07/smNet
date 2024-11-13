import subprocess

# Define the arguments
arg1 = "General"
arg2 = "0"
# arg2 = "0,1,2,4,5,6,7"

# Run the shell script with arguments
try:
    result = subprocess.run(['./train.sh', arg1, arg2], check=True, text=True, capture_output=True)
    print("Script output:", result.stdout)
except subprocess.CalledProcessError as e:
    print("Error running script:", e.stderr)
