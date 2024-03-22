print("empty")

# wc -l – Prints the number of lines in a file.
# wc -w – prints the number of words in a file.
# wc -c – Displays the count of bytes in a file.
# wc -m – prints the count of characters from a file.
# wc -L – prints only the length of the longest line in a file.
from setuptools import setup, find_packages

setup(
    name='helper_module',
    version='0.1',
    py_modules=['helper_module'],
)
