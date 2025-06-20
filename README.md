# Recommender System Using Collaborative Filtering

This project implements a collaborative filtering-based recommender system using Python. It is designed for educational and research purposes, focusing on user-based and item-based recommendation techniques.

## Key points to not for collaborative filtering
- User-based collaborative filtering: Recommends items to a user based on the preferences of similar users.
- Item-based collaborative filtering: Recommends items similar to those the user has already liked/rated.

## Features
- Data loading and preprocessing
- User-based and item-based collaborative filtering
- Evaluation with RMSE, precision, recall, and F1-score
- Modular code for easy experimentation

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Download the MovieLens dataset and place it in the `data/` folder.
3. Run the main script or use the provided Jupyter notebooks for exploration.

## Project Structure
- `data/` - Datasets
- `notebooks/` - Jupyter notebooks for EDA and prototyping
- `src/` - Source code modules
- `tests/` - Unit tests

## Author
Tumbu Nkeng John 

Supervisor: Dr. Denis Nkweteyim

# Installing Visual Studio Build Tools for Python Package Compilation

Some Python packages (like numpy, pandas, scikit-learn, and scipy) require C++ build tools to compile native code, especially on Windows. If you encounter errors about missing build dependencies, follow these steps to install the required tools.

---

## Option 1: Manual Download and Installation

1. **Download the Visual Studio Build Tools Installer**
   - Go to the official Microsoft download page: https://visualstudio.microsoft.com/visual-cpp-build-tools/
   - Download the installer (e.g., `vs_BuildTools.exe`).

2. **Run the Installer**
   - Double-click the downloaded `.exe` file to launch the Visual Studio Installer.

3. **Select Workloads**
   - In the installer, select **"Desktop development with C++"** or **"C++ build tools"**.
   - Under "Installation details," ensure the following are checked:
     - MSVC v142 or v143 - VS 2019/2022 C++ x64/x86 build tools
     - Windows 10/11 SDK
     - C++ CMake tools for Windows

4. **Install and Restart**
   - Click **Install** and wait for the process to complete.
   - Restart your computer if prompted.

5. **Verify Installation**
   - Open a new Command Prompt and run:
     ```
     cl
     ```
   - You should see Microsoft C/C++ compiler version info.

---

## Option 2: Command Line Installation

1. **Download the Bootstrapper (if needed):**
   ```powershell
   curl -LO https://aka.ms/vs/17/release/vs_BuildTools.exe
   ```

2. **Run the Installer with Required Components:**
   ```powershell
   .\vs_BuildTools.exe --add Microsoft.VisualStudio.Workload.VCTools --includeRecommended --quiet --wait
   ```

3. **Restart Your Computer**

4. **Verify Installation**
   - Open a new Command Prompt and run:
     ```
     cl
     ```
   - You should see Microsoft C/C++ compiler version info.

---

## After Installation
- Open a new terminal and run your pip install commands again:
  ```powershell
  pip install numpy pandas scikit-learn scipy scikit-surprise jupyter pytest
  ```
- If you still encounter errors, check the error message and ensure your Python version is compatible with the packages you are installing.

---

**Tip:** Always restart your terminal after installing new build tools to ensure environment variables are updated.

# Recommended: Using Miniconda/Anaconda for Python Data Science Projects

For Windows users, especially those with slow or unreliable internet connections, it is highly recommended to use Miniconda or Anaconda as your Python environment manager. These distributions provide pre-built binaries for scientific packages, eliminating the need for large downloads or C++ build tools.

## Why Use Miniconda/Anaconda?
- **No need for Visual Studio Build Tools**: Packages like numpy, pandas, scikit-learn, and scipy are available as pre-built binaries.
- **Easy installation**: Install all required packages with a single command.
- **Reliable and fast**: Avoids compilation errors and large downloads.

## How to Set Up Miniconda
1. Download Miniconda from the official site: https://docs.conda.io/en/latest/miniconda.html
2. Run the installer and follow the prompts.
3. Open a new terminal (Anaconda Prompt or Command Prompt).
4. Create a new environment (optional but recommended):
   ```
   conda create -n recommender python=3.10
   conda activate recommender
   ```
5. Install required packages:
   ```
   conda install numpy pandas scikit-learn scipy jupyter pytest
   ```
6. You are now ready to work on your project without needing to install any additional build tools!

## Alternative: Use Anaconda
- Anaconda is a larger distribution that comes with even more packages pre-installed. The setup process is similar.

## Cloud Option
- If you want to avoid local setup entirely, use Google Colab or Kaggle Notebooks, which have all scientific packages pre-installed.

---

**Summary:**
Using Miniconda or Anaconda is the easiest and most reliable way to set up a Python data science environment on Windows, especially if you have bandwidth or installation constraints.

## Data Source
This project uses the [MovieLens dataset](https://grouplens.org/datasets/movielens/latest/), provided by [GroupLens Research](https://grouplens.org/). MovieLens is a widely used public dataset for recommender system research and experimentation.
