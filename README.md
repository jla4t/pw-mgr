Password Manager

This Python script creates a simple password manager application using the Tkinter library. It allows the user to generate passwords, add passwords for different websites, and store them in a data file. The generated passwords can be copied to the clipboard for easy use.
Features

    Generates a random password with a combination of uppercase and lowercase letters, digits, and special characters ('!', '@', '#', '$', '?').
    Allows the user to repeatedly generate passwords until they accept one.
    Saves the entered website, email/username, and password to a data file.
    Provides confirmation to the user before saving the password.
    Copies the generated password to the clipboard for easy pasting.
    Provides a simple UI with labels, entry fields, and buttons for user interaction.

Dependencies

    Python 3.x
    Tkinter library (included in standard Python library)

Usage

    Run the script in a Python environment.
    Enter the website, email/username, and password in the respective entry fields.
    Click the "Add Password" button to save the entered data to a data file.
    Click the "Generate Password" button to generate a random password.
    Click "Yes" or "No" in the messagebox to confirm or decline the generated password, respectively.
    If confirmed, the password will be copied to the clipboard and saved to the data file.
    Repeat the above steps for adding more passwords as needed.

Note

    The generated passwords are 10 characters in length and include a combination of uppercase and lowercase letters, digits, and the special characters '!', '@', '#', '$', '?'.
    The data file "data.txt" is used to store the entered website, email/username, and password in a comma-separated format.
    The "logo.png" file is expected to be present in the same directory as the script and is used as the logo for the application.

Disclaimer

    This is a simple password manager application and may not have all the security features of a professional password manager.
    Always exercise caution and follow best practices when managing and storing passwords.
    Use at your own risk. The author is not responsible for any misuse or damage caused by the use of this script.
