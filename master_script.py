import subprocess
import time

# Define a function to execute a subprocess and capture its output
def run_subprocess(script_name):
    print(f"Starting {script_name}...")
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    process = subprocess.Popen(['python3', script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"Started at: {start_time}")
    print(f"Ended at:   {end_time}")
    print(stdout)
    
    if process.returncode != 0:
        print(f"{script_name} failed with error:\n{stderr}")
        exit(1)

# Define paths to the scripts
unzip_script = 'unzip_file.py'
import_db_script = 'import_database_file.py'
update_db_script = 'update_database2.py'
update_file_script = 'update_file.py'

# Execute the Unzip script
run_subprocess(unzip_script)

# Execute the Database Import script
run_subprocess(import_db_script)

# Execute the Database Update script
run_subprocess(update_db_script)

# Execute the File Update script
run_subprocess(update_file_script)

print("All scripts executed successfully.")
