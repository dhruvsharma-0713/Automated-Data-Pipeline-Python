import schedule
import time
import subprocess

def run_scraper():
    print("Running the data scraper and visualization script...")
    try:
        # We use subprocess to run the scraper.py script
        subprocess.run(['python', 'scraper.py'], check=True)
        print("Script finished successfully!")
    except subprocess.CalledProcessError as e:
        print(f"The script failed with error: {e}")

# Schedule the job to run every day at 10:30 AM
schedule.every().day.at("10:30").do(run_scraper)

# to run every 1 minute (remove the '#'):
# schedule.every(1).minutes.do(run_scraper)

print("Automation script started. Waiting for the scheduled time to run the job...")

# This loop constantly checks if it's time to run a job
while True:
    schedule.run_pending()
    time.sleep(1)