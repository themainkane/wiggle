import pyautogui
import time
import random
import argparse

# Parse arguments for the desired wait time
parser = argparse.ArgumentParser(description="Wiggler script to prevent screen lock.")
parser.add_argument('-hours', type=float, default=2.0, help="Number of hours to run the wiggler (default: 2.0)")
args = parser.parse_args()

# Set the duration (in seconds)
duration_seconds = args.hours * 60 * 60
end_time = time.time() + duration_seconds

print("Starting the Wiggler...")
print(f"The script will run for {args.hours} hours. Press Ctrl+C in this terminal to stop it early.")

# PyAutoGUI has a fail-safe: if you slam your mouse to any of the 4 corners
# of your screen, it will abort the script automatically.
pyautogui.FAILSAFE = True

try:
    while time.time() < end_time:
        # Wait for an irregular interval between bursts (e.g., 1 to 5 minutes)
        idle_time = random.randint(60, 300)
        time.sleep(min(idle_time, max(0, end_time - time.time())))

        if time.time() >= end_time:
            break

        # Start a burst of activity lasting 30 seconds to 1 minute
        burst_duration = random.randint(30, 60)
        burst_end = time.time() + burst_duration

        while time.time() < burst_end and time.time() < end_time:
            # Generate a small random movement
            x_offset = random.randint(-15, 15)
            y_offset = random.randint(-15, 15)

            # Move the mouse relative to its current position
            pyautogui.move(x_offset, y_offset, duration=0.25)

            # Press the shift key (registers as activity but rarely disrupts anything)
            pyautogui.press('shift')

            # Wait for a short, random time between actions within the burst (1 to 5 seconds)
            time.sleep(random.randint(1, 5))

except KeyboardInterrupt:
    print("\nWiggler stopped manually by user.")

print(f"\nFinished {args.hours}-hour run. Welcome back!")
