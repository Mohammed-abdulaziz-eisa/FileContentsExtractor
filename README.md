# FileContentsExtractor: Effortless File Organization

**FileContentsExtractor** is a robust Python utility designed to simplify file management within directory structures. It excels at organizing projects where filenames leverage numerical prefixes, automating a previously tedious task.

**Key Benefits:**

* **Streamlined Organization:** Effortlessly organize files based on numeric prefixes, ensuring a well-structured directory layout.
* **Intelligent Sorting:** Leverages sophisticated algorithms to sort file names meticulously, including those with decimals, for intuitive retrieval.
* **Duplicate Elimination:** Maintains data integrity by meticulously removing duplicate entries, resulting in clean and accurate output.
* **Customized File Output:** Generates dedicated text files (`.txt`) for each folder, providing clear overviews of sorted and unique filenames.

**Technical Specifications:**

* **Programming Language:** Python 3.x (ensuring broad compatibility)
* **Dependencies:**
    * `os` module (built-in, facilitates operating system interactions)
    * `re` module (built-in, empowers powerful regular expression pattern matching)

## Installation

**Installation:**

1. **Clone the Repository:**

   ```bash
   git clone [https://github.com/Mohammed-abdulaziz-eisa/FileContentsExtractor.git](https://github.com/Mohammed-abdulaziz-eisa/FileContentsExtractor.git)
   ```

2. Navigate to the cloned repository:
   ```bash
   cd FileContentsExtractor
   ```
3. optional Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install any necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place the script in the directory you want to organize.
2. Run the script:
   ```bash
   python FileContentsExtractor.py
   ```
3. The script will create a text file for each folder in the current directory, named foldername_contents.txt, containing the sorted file names.
## Illustrative Example
Consider a folder named "3. Model-to-App Packaging Production Codebase Design". The script will create a file named "3. Model-to-App Packaging Production Codebase Design_contents.txt". The contents might resemble:

1. From Jupyter to Application Code Transformation
2. Python Dependency Management Setup with Poetry
3. Python Parametrization Setup with Pydantic
4. Python Logging Setup with Loguru
5. Database Setup and Python Connectivity with Sqlalchemy

## Contributing
We actively encourage your contributions! If you possess valuable suggestions or enhancements for this utility, feel free to submit a pull request through the project's repository.

## License
FileContentsExtractor is open-source software, distributed under the permissive MIT License. Refer to the LICENSE file for comprehensive details.