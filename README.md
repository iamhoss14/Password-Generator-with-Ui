
# Password Generator Web Application

## Overview
This project is a Python-based password generator application that provides users with multiple password options, including PINs, random passwords, and memorable passwords. The application is built using the Streamlit framework for the user interface and various password generation algorithms for different types of passwords.

## Features
- **PIN Generator:** Generates secure PINs of customizable lengths.
- **Random Password Generator:** Generates random passwords with options to include numbers and symbols.
- **Memorable Password Generator:** Generates passwords composed of random words that are easier to remember. Allows customization for word count, capitalization, and separators.
- **Interactive Web Interface:** Built using Streamlit for an interactive experience.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-generator.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run dashboard.py
   ```

## File Breakdown

### `dashboard.py`
This file contains the Streamlit web interface where users can select the type of password they want to generate. It allows for:
- PIN generation
- Random password generation with customizable length, numbers, and symbols
- Memorable password generation using words (with an option to capitalize and customize separators)

**Streamlit Components:**
- Image display
- Radio buttons for password type selection
- Sliders for length selection
- Checkboxes for including numbers and symbols
- Text input for customizing the separator in memorable passwords

### `my_password_utils.py`
This file contains the core logic for password generation, with the following classes:
- **PasswordGenerator (Abstract Base Class)**: A base class for password generators.
- **PinGenerator**: Generates PINs of a specified length.
- **RandomPasswordGenerator**: Generates random passwords with optional numbers and symbols.
- **MemorablePasswordGenerator**: Generates memorable passwords by selecting random words from a predefined vocabulary.

### `nltk_words` Integration
The `MemorablePasswordGenerator` uses the `nltk` package's "words" corpus to select random words for generating memorable passwords. If `nltk` is not installed or if the "words" corpus is not available, it defaults to a small set of common words.

## Usage

1. **PIN Generator**: 
   - Select "PIN" from the options, and choose a length (between 6 to 12 characters).
   - The app will generate a random PIN.

2. **Random Password Generator**:
   - Select "Random Password" and specify the length (between 8 to 24 characters).
   - Choose whether to include numbers and symbols.

3. **Memorable Password Generator**:
   - Select "Memorable Password" and set the number of words (between 2 to 6).
   - Choose a separator (e.g., `-`).
   - Decide whether to capitalize the words.

## Requirements

- Python 3.x
- Streamlit
- NLTK (for generating memorable passwords using the word corpus)

To install the required dependencies, run:
```bash
pip install streamlit nltk
```

## Contributing

Contributions are welcome! If you would like to improve this project, please fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Streamlit**: For the easy-to-use framework to build the UI.
- **NLTK**: For providing the word corpus used for generating memorable passwords.

---

## Example Screenshots

![Password Generator App Screenshot](images/download.png)

This is a preview of the user interface of the password generator application. The interface is simple, interactive, and allows for customization based on the user's needs.
