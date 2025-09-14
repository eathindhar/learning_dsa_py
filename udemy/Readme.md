# Create a virtual environment named "myenv"
python -m venv myenv

# PowerShell
myenv\Scripts\Activate.ps1


# Deactivating venv 
deactivate

# Install from requirements file
pip install -r requirements.txt

# List all packages
pip list

# List with versions
pip freeze

# Save to requirements file
pip freeze > requirements.txt