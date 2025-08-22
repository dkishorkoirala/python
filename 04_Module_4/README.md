# Module 4 – Data Analysis with NumPy & Pandas (Days 62–106)

This module covers NumPy and Pandas through slow, day-by-day practice. It includes clear explanations, multiple mini‑tasks, and challenge projects. This README explains how to **set up a virtual environment**, **install `requirements.txt`**, and **run the daily code** on both **Windows** and **Linux**.

---

## 🐍 Create & Use a Virtual Environment

> You mentioned you’re using a virtual environment and already have a `requirements.txt`. Below are **step-by-step** commands for **Windows** and **Linux**.

### ✅ Windows (PowerShell or CMD)

```powershell
# 1) Navigate to your module folder
cd path	o\module_4_numpy_pandas

# 2) Create a virtual environment named .venv
py -m venv .venv

# 3) Activate the environment
# PowerShell:
.venv\Scripts\Activate.ps1
# CMD:
.venv\Scripts\Activate

# 4) Upgrade pip (recommended)
py -m pip install --upgrade pip

# 5) Install requirements inside the venv
pip install -r requirements.txt

# 6) Verify installs
py -c "import numpy, pandas; print(numpy.__version__, pandas.__version__)"
```

**Deactivate when done:**
```powershell
deactivate
```

> ⚠️ If activation is blocked in PowerShell, run:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```

---

### 🐧 Linux (or macOS) – Bash/Zsh

```bash
# 1) Navigate to your module folder
cd /path/to/module_4_numpy_pandas

# 2) Create a virtual environment named .venv
python3 -m venv .venv

# If venv is missing on Ubuntu/Debian:
# sudo apt-get update && sudo apt-get install -y python3-venv

# 3) Activate the environment
source .venv/bin/activate

# 4) Upgrade pip (recommended)
python -m pip install --upgrade pip

# 5) Install requirements inside the venv
pip install -r requirements.txt

# 6) Verify installs
python - << 'PY'
import numpy, pandas
print(numpy.__version__, pandas.__version__)
PY
```

**Deactivate when done:**
```bash
deactivate
```

---

## 📦 `requirements.txt` (example)

If you already have one—great! If not, here’s a simple example you can adapt:

```
numpy>=1.26
pandas>=2.2
python-dateutil>=2.8
```
> You can capture exact versions from your current environment:
> ```bash
> pip freeze > requirements.txt
> ```

---

## ▶️ Running the Daily Code

Each day’s folder will usually include a `main.py` (or multiple scripts). Activate your **virtual environment** first, then run:

### Windows
```powershell
.venv\Scripts\Activate.ps1
py 62_day_62_numpy_intro\main.py
```

### Linux/macOS
```bash
source .venv/bin/activate
python3 62_day_62_numpy_intro/main.py
```

> Tip: For scripts that need input, run them directly and follow prompts in the terminal.

---

## 🧪 Quick Smoke Test

After installing requirements, confirm NumPy & Pandas work:

```python
# save as test_env.py in the module root
import numpy as np
import pandas as pd

print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)

a = np.array([1, 2, 3]) * 5
print("Array x 5:", a)

df = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
print(df.head())
```

Run:

- **Windows:** `py test_env.py`  
- **Linux/macOS:** `python test_env.py`

---

## 🧰 Troubleshooting

- **PowerShell activation error:** Use `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` and try again.  
- **`venv` not found (Linux):** `sudo apt-get install -y python3-venv`.  
- **Permission issues (Linux):** try `python3 -m venv .venv` and `pip install --user` is **not** needed inside a venv.  
- **Wrong interpreter in VS Code:** Select Python interpreter from `.venv` (Ctrl/Cmd+Shift+P → “Python: Select Interpreter”).  
- **Mixing global & venv pip:** Always activate the venv first. Verify with `which python` (Linux/macOS) or `where python` (Windows).

---

## 🗂️ .gitignore (recommended)

```
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
.DS_Store
```

---

## ✅ Workflow Summary (Both OS)

1. Create venv → **activate** it.  
2. `pip install -r requirements.txt`.  
3. Run the day’s script from its folder.  
4. Update `requirements.txt` when you add new libs: `pip freeze > requirements.txt`.  
5. Commit code; never commit `.venv`.  

Happy coding! 🚀