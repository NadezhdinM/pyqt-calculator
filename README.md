# PyQt Calculator

This is a simple calculator application built using PyQt5. It provides a graphical user interface (GUI) for basic arithmetic operations.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- Clear button to reset the calculation.
- Real-time display of the current expression and result.

## Requirements

- Python 3.6+
- PyQt5
- pyqt5-tools (for compiling resources, if needed)

## Installation

1. Clone the repository or download the source code.

```bash
git clone https://github.com/NadezhdinM/pyqt-calculator.git
cd pyqt5-calculator
```

2. Create and activate a virtual environment (optional but recommended).

```bash
# Install virtualenv if you don't have it
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS and Linux
source venv/bin/activate
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

# Usage

1. Run the application.
```bash
python main.py
```
2. The calculator GUI will appear. Use the buttons to perform calculations.

## Project Structure

1. `main.py`: Main file to run the application.
2. `calculator_ui.py`: Contains the user interface design.
3. `calculator_logic.py`: Contains the logic for performing calculations.
4. `styles.qss`: Contains the styles for the application.
5. `resources.qrc`: Contains resources (such as images) for the application.

## Customization

1. `Styles`: You can customize the look and feel of the calculator by editing the styles.qss file.
2. `Resources`: If you need to add or change resources, update the resources.qrc file and compile it using the following command:

```bash
pyrcc5 resources.qrc -o resources_rc.py
```

## Troubleshooting

If you encounter any issues while installing dependencies or running the application, try the following steps:

1. Ensure you have Python 3.6 or higher installed.
2. Make sure all dependencies are installed correctly by checking `requirements.txt`.
3. If you are using a virtual environment, ensure it is activated.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

This project uses PyQt5 for the graphical user interface.

```bash
This `README.md` file provides a comprehensive overview of your calculator application, including installation instructions, usage, project structure, customization options, and troubleshooting tips. Feel free to modify and expand it according to your project's specific details and requirements.
```
# Contributors

1. Nadezhdin Maksim
