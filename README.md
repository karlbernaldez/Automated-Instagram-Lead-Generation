## Instagram Leads Finder

### Description

The Instagram Leads Finder is a Python script that automates the process of finding potential leads on Instagram based on a list of individuals' details sourced from a CSV file. The script logs into an Instagram account, searches for each individual by name, verifies potential matches, retrieves full names from verified profiles, and stores the Instagram usernames and full names of potential leads in a new CSV file.

### Prerequisites

- Python 3.x
- Selenium Python package
- Google Chrome browser
- ChromeDriver (compatible with the version of the Chrome browser you are using)

### Installation

1. Ensure that Python and pip (Python's package installer) are installed on your system. If not, download and install Python from the [official website](https://www.python.org/).
2. Install the Selenium package by running the following command in your terminal or command prompt:
   
   ```
   pip install selenium
   ```

3. Download the ChromeDriver from the [official website](https://sites.google.com/a/chromium.org/chromedriver/) and add its location to your system's PATH.
4. Clone or download this repository to your local machine.

### Usage

1. Update the `csv_file_with_info.csv` file with the individuals' details. The file should contain columns for the name, address, and school of each individual.
2. Open the script in a text editor and update the Instagram login credentials in the `LoginPage(browser).login("johndoe_100123", "Johndoe1001")` line with valid credentials.
3. Run the script in a terminal or command prompt with the command:

   ```
   python script_name.py
   ```

4. The script will execute, performing searches on Instagram based on the names in the CSV file, and verifying potential matches using a subset match of the name words.
5. Potential leads will be saved in a new CSV file named 'possible_leads.csv', which will contain the Instagram usernames and full names of the matches.

### Note

- The Instagram webpage structure and elements might change over time, requiring updates to the CSS selectors used in the script.
- The script currently does not fully utilize the bio details retrieved from the profiles; this is a potential area for further development.
- Ensure to use the script responsibly and in compliance with Instagram's terms of service.

### License

This project is for educational purposes and should be used responsibly and ethically. It is not endorsed by or affiliated with Instagram.

---

Remember that this README assumes that the repository contains only this script and the necessary CSV file. Adjust the details as necessary to fit your repository structure and contents.
