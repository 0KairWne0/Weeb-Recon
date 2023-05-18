Certainly! Here's a README file that provides an overview of the code:

# Website Reconnaissance Script

This Python script allows you to perform various website analysis and reconnaissance tasks. It prompts the user for input regarding the website URL, wordlists, user agent, and preferences for different operations.

## Prerequisites

- Python 3.x
- Required tools installed: `wget`, `dirb`, `gobuster`, `curl`, `whatweb`, `lynx`

## Usage
1. Install the requirements.txt `pip install -r requirements.txt`
2. Run the script using `python3 WeebRecon.py`.
3. Follow the prompts and provide the necessary information.
4. The script will execute the selected operations based on your preferences.

## Functionality

The script provides the following functionality:

- Cloning the web page using `wget` if desired.
- Performing a brute force on directories and files using `dirb` and `gobuster` if desired.
- Performing a subdomain brute force using `gobuster` and DNS enumeration if desired.
- Fetching the website's HTTP headers using `curl` if desired.
- Identifying the technologies used on the website using `whatweb` if desired.
- Identifying pages on the internet with a specified extension using `lynx` and Google search if desired.

Please use this script responsibly and ensure that you have the appropriate permissions and legal rights before performing any scanning or reconnaissance activities.

## Disclaimer

The script is provided as-is and without any warranty. Use it at your own risk. The author are not responsible for any misuse or illegal activities conducted with this script.

Feel free to modify the code according to your specific needs and requirements.
