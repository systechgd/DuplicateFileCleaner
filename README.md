# DuplicateFileCleaner

# File Cleaner

File Cleaner is a simple and efficient desktop application that helps users clean up unwanted files and folders from their system. With an intuitive interface and powerful features, it makes file management easy and effective.

## Features

- **Easy File Cleaning**: Quickly remove temporary files, log files, and other unnecessary files to free up disk space.
- **Customizable**: Users can specify file types and directories to clean.
- **Safe**: Files are moved to a temporary holding area before deletion, allowing for easy recovery if needed.
- **Performance Optimization**: Improve system performance by regularly cleaning up cluttered files.
- **User-Friendly Interface**: Simple and intuitive design for ease of use.

## Download
You can download the latest version of the File Cleaner for Windows from the [Releases](https://github.com/systechgd/DuplicateFileCleaner/releases) section on GitHub.

## Installation
1. Download the installer (`FileCleanerSetup.exe`) from the link above.
2. Run the installer and follow the on-screen instructions.
3. Once installed, you can launch File Cleaner from your Start Menu or Desktop.

If you encounter any issues, please check the [Troubleshooting](#troubleshooting)

### Prerequisites

- **Operating System**: Windows 10 or later
- **Python 3.x**: Ensure that Python is installed on your system.

### Installation Steps for Developers

1. Clone the repository:
    ```bash
    git clone https://github.com/systechgd/DuplicateFileCleaner.git
    ```
2. Navigate to the project directory:
    ```bash
    cd DuplicateFileCleaner
    ```
3. Install the required dependencies:
    ```bash
    pip install tk
    pip install pyinstaller
    pip install cx_Freeze
    ```
4. Build Application to make .exe file
   ```bash
    python setup.py build
   ```
6. Run the application:
    ```bash
    Open build folder and duble click on application
    ```

## Usage

1. Launch the application using the simple double click:
2. Browse the folder in which you want to clean.
3. Click the "Delete Duplicates" button to remove the unwanted files.
4. Click the "Clear History" to clean logs

## Contributing

We welcome contributions from the community. If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Description of your changes"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Create a pull request and describe your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

- If you have any questions, issues, or feature requests, please feel free to contact me at systechgd@gmail.com.
- Follow me on LinkedIn www.linkedin.com/in/ganesh-dandavate 

## Acknowledgments

- Thanks to all contributors and open-source libraries that made this project possible.
- Special mention to the developers who provided valuable feedback during the development process.

---

*This README was generated for the File Cleaner project. Feel free to modify it to fit the specifics of your application.*
