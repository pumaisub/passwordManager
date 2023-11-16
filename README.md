# passwordManager
Python tkinter GUI password manager for different websites and emails, generates passwords, creates and writes to a textfile


When run, this Python program opens up a GUI (graphical user interface) using the Tkinter library and asks you to enter a website,
an email, and a password. Since most people are not great at creating secure passwords, you can click on the 'Generate Password' and
it will generate a secure random password for you and fill the entry space for 'Password'. The password is randomly generated using
a random amount of 8-10 letters,2-4 numbers, and 2-4 symbols.

If spaces are left empty, there will be an error message that pops up reminding you to fill in the blanks.

If spaces are filled, upon clicking the 'Add' button, a message will pop-up to confirm your input. If you click 'OK',
the inputs will be recorded into a data.txt file which will be created if it does not already exist. If one already
exists, the new entries will be appended to the list so that the user can save multiple website/email/password records.
