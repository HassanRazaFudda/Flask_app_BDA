# Flask Student Management Application

This is a simple Flask application for managing student data. Below are step-by-step installation and running instructions for beginners.

## Download and Setup Instructions

### Step 1: Download the Repository

1. Go to the GitHub repository page
2. Click the green **"Code"** button
3. Select **"Download ZIP"**
4. The ZIP file will be downloaded to your computer

### Step 2: Extract the ZIP File

1. Right-click on the downloaded ZIP file
2. Select **"Extract All"**
3. Choose your preferred location (e.g., `C:\Projects\`)
4. Open the extracted folder

### Step 3: Install Python (If not already installed)

1. Download Python from [Python.org](https://www.python.org/downloads/) (Python 3.8 or later)
2. During installation, make sure to check the **"Add Python to PATH"** checkbox
3. Wait for the installation to complete

### Step 4: Open Command Prompt/PowerShell

1. Type **"cmd"** or **"PowerShell"** in Windows Search
2. Open Command Prompt or PowerShell
3. Navigate to the extracted folder:
   ```bash
   cd C:\Projects\Flask_app_BDA
   ```
   _(Change this to match your actual path)_

### Step 5: Create a Virtual Environment

Run this command to create a virtual environment:

```bash
python -m venv venv
```

### Step 6: Activate the Virtual Environment

**For PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**If you get an error in PowerShell, first run this command:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**For Command Prompt (CMD):**

```bash
venv\Scripts\activate
```

After successful activation, you'll see `(venv)` at the beginning of your terminal prompt.

### Step 7: Install Dependencies

After activating the virtual environment, run this command:

```bash
pip install -r requirements.txt
```

This command will install all required libraries (Flask, SQLAlchemy, etc.)

### Step 8: Run the Application

Now use this command to run the application:

```bash
python app.py
```

### Step 9: Access the Application

1. After the application runs successfully, you'll see a URL in the terminal (e.g., `http://127.0.0.1:5000`)
2. Open this URL in your web browser
3. The application homepage will appear!

## Stopping the Application

- To stop the application, press **`Ctrl + C`** in the terminal
- To exit the virtual environment, type **`deactivate`** in the terminal

## Common Issues and Solutions

### Issue 1: "Python is not recognized"

**Solution:** Add Python to PATH or reinstall Python with the "Add to PATH" option checked.

### Issue 2: "cannot be loaded because running scripts is disabled" in PowerShell

**Solution:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue 3: Port 5000 is already in use

**Solution:** An error will appear in the terminal. Close any other application using port 5000, or change the port number in `app.py`.

## Project Structure

```
Flask_app_BDA/
│
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # Ye file
│
├── instance/             # Database files yahan store honge
│
└── templates/            # HTML templates
    ├── form.html
    ├── index.html
    ├── profile.html
    └── show.html
```

## Features

- Add student data
- View list of students
- Uses SQLite database (will be created automatically)

## Help and Support

If you encounter any issues:

1. Carefully recheck the commands
2. Ensure the virtual environment is properly activated
3. Confirm all dependencies are installed

---

**Happy Learning! 🎓**
