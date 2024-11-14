



# Python Library Installer

This project provides a Python script that automatically installs some essential and widely-used Python libraries for various tasks like data science, machine learning, web development, and more. By using a single script, you can set up your Python environment with all the necessary libraries quickly and easily.

## Features

- Installs lot of popular and useful Python libraries automatically.
- Libraries are listed and managed via a `requirements.txt` file.
- Ideal for setting up environments for data science, machine learning, web development, image processing, and other Python-based applications.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/AmirakbariSXL/python-library-installer.git
   cd python-library-installer
   ```

2. **Ensure you have Python and `pip` installed**:
   
   Make sure you have Python 3.x installed on your system along with the `pip` package manager. If not, you can install them from the [official Python website](https://www.python.org/downloads/).

3. **Create a virtual environment (optional but recommended)**:

   It's highly recommended to use a virtual environment to manage your project dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

4. **Install the libraries**:

   With the `requirements.txt` file provided in the project, you can install all 700 libraries at once by running the following command:

   ```bash
   python install_libraries.py
   ```

   The script will automatically install all the libraries listed in `requirements.txt` using `pip`.

## How It Works

- The `install_libraries.py` script reads from the `requirements.txt` file.
- It installs all the listed libraries in your active Python environment.
- This saves you time and effort by installing popular libraries for common tasks in a single step.

## Libraries Included

The `requirements.txt` file contains 700 widely-used Python libraries across various domains, including:

- **Data Science**: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `tensorflow`, `pytorch`
- **Web Development**: `Flask`, `Django`, `FastAPI`, `requests`
- **Machine Learning**: `xgboost`, `keras`, `lightgbm`, `spacy`
- **Other**: `beautifulsoup4`, `pytest`, `SQLAlchemy`, `plotly`, `pytest`, and many more.

## Contributing

Feel free to fork this project, open issues, or submit pull requests if you'd like to contribute.

---

### my telegram channel:
- @pythonism_xl
