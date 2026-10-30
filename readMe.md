# Wiggler 🖱️

Wiggler is a simple Python script that mimics real human behavior by randomly moving the mouse and pressing the `Shift` key in bursts. It keeps your computer awake and prevents the screen from locking while you step away.

## 🛠️ Prerequisites (Both Mac & Windows)
1. **Install Python**: Make sure Python is installed on your computer.
    - **Mac**: Usually pre-installed, but can be downloaded from [python.org](https://www.python.org/).
    - **Windows**: Download from [python.org](https://www.python.org/). **Important:** During the Windows installation, make sure to check the box that says **"Add Python to PATH"** at the bottom of the installer window!
2. **Download this project**: Save the `wiggler` folder to a dedicated location. The setup below assumes you saved it to `~/git/wiggler` (which translates to `C:\Users\YourName\git\wiggler` on Windows).
3. **Install required libraries**: Open your terminal (Mac) or PowerShell (Windows) and run:
   ```bash
   pip install pyautogui
   ```

---

## 🍎 Mac Setup

To be able to run Wiggler from anywhere by just typing `wiggle`, we need to add a quick function to your terminal settings.

1. Open your Terminal.
2. Open your Zsh configuration file in a text editor (like nano):
   ```bash
   nano ~/.zshrc
   ```
3. Scroll to the bottom and paste the following code:
   ```bash
   wiggle() {
       pushd ~/git/wiggler > /dev/null && python3 wiggle.py "$@" && popd > /dev/null
   }
   ```
   *(Note: Adjust `~/git/wiggler` if you saved the folder somewhere else).*
4. Save and exit (In nano, press `Ctrl+O`, `Enter`, then `Ctrl+X`).
5. Reload your settings by running:
   ```bash
   source ~/.zshrc
   ```

---

## 🪟 Windows Setup

To get the exact same experience on Windows, we'll add a function to your PowerShell Profile.

1. Open **PowerShell**.
2. First, check if you already have a profile file created by running this command:
   ```powershell
   Test-Path $PROFILE
   ```
3. If it returns `False`, run this command to create one:
   ```powershell
   New-Item -Type File -Force $PROFILE
   ```
4. Now, open the profile file in Notepad:
   ```powershell
   notepad $PROFILE
   ```
5. Paste the following code at the bottom of the file:
   ```powershell
   function wiggle {
       Push-Location "$env:USERPROFILE\git\wiggler"
       python wiggle.py $args
       Pop-Location
   }
   ```
   *(Note: Adjust the path if you saved the folder somewhere other than `git\wiggler` inside your user folder).*
6. Save the file in Notepad and close it.
7. Restart PowerShell for the changes to take effect.
   *Note: If Windows gives you an error about "running scripts is disabled" when you restart PowerShell, run this command once as Administrator: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`, then press `Y`.*

---

## 🚀 How to Use

Open your Terminal or PowerShell from anywhere on your computer and type:

```bash
# Run for the default time (2 hours)
wiggle

# Run for a specific amount of time (e.g., 4.5 hours)
wiggle -hours 4.5
```
