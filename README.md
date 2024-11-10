# FTP Brute Force Tool

A simple FTP brute force tool written in Python for educational and research purposes. This tool attempts to login to an FTP server by trying different combinations of usernames and passwords from wordlists.

**Created by:** MD. Bayazid  
**Email:** bayazid.mtu@gmail.com  
**Batch:** SSC 2025  

---

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

---

## Features

- **Brute Force FTP Login**: Attempts to log in to an FTP server using provided username and password lists.
- **Custom Timeout**: Allows you to specify a custom timeout for connection attempts.
- **Live Feedback**: Displays which username and password combination is being tried in real time.
- **Logging**: Outputs logs for successful, failed, or warning attempts.

---

## Installation

1. **Clone the repository** (if applicable):
    ```bash
    git clone https://github.com/your-username/ftp-brute-force.git
    cd ftp-brute-force
    ```

2. **Install the necessary dependencies** (Python 3.x recommended):
    The script uses standard Python libraries, so no external dependencies are required. Ensure Python 3 and above is installed.

3. **Run the script**:
    You can now run the script directly from the terminal using the following command.

---

## Usage

### Command Line Arguments:
```bash
python3 ftpc.py <host> <port> <userWordList> <PassWordList> <timeout>
