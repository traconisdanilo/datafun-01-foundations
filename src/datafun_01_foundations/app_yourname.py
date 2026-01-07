"""app_yourname.py - Project script.

TODO: Replace "yourname" in the name of this file with your name or alias.
TODO: Update the associated command to run your file in the README.md file.

TODO: Update this module docstring with your name or alias and the date below.

Author: Your Name or Alias
Date: 2026-01

  Practice key Python skills:
  - docstring comments (triple quotes) used at the start of each module and function
  - inline comments (these start with the hash symbol #)
  - declaring variables (common kinds)
  - using type hints (to make types explicit)
  - declaring lists (widely used collections)
  - using f-strings (formatted string literals to combine text and variables)
  - logging (preferred over print - creates an external record of program runs)
  - declaring common functions like main()
  - using the standard Python entry point pattern (if __name__ == "__main__":)
  - that way, we can run this file as a script OR import it as a module into other code files

OBS:
  This is your file to practice and customize.
  Find the TODO comments, and as you complete each task, remove the TODO note.
"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

# Python standard library
import logging  # only needed so we can type hint the logger variable
from typing import Final  # only needed for type hinting constants

# External (must be listed in pyproject.toml)
# logging helps track program execution and is preferred over print statements
# We'll use a pre-configured logger that respects privacy.
from datafun_toolkit.logger import (
    get_logger,
    log_header,
)

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

# Call the get_logger() function, pass in a phrase and the logging level we want.
# The phrase helps identify the source of log messages.
# The level could be "DEBUG", "INFO", "WARNING", "ERROR", or "CRITICAL".
# Use DEBUG for development, INFO for production.
LOG: logging.Logger = get_logger("P01", level="INFO")

# === DECLARE GLOBAL CONSTANTS ===

# All of these global variables are CONSTANT and do NOT change when the program runs.
# By convention, constant variable names are all UPPERCASE_WITH_UNDERSCORES.
# Declare a variable and initialize it with a value for each of these common types:
#    str, int, float, bool, list of strings.
# Code like a pro: Use optional Python `type hints` to make types explicit
# Just add a colon and the type before the equals sign.

# See the example file for reference.
# Then, declare your own variables as per the TODOs below.
# Examples:

MY_ANALYTICS_COMPANY: Final[str] = "DataFun Analytics"
MY_EMPLOYEE_COUNT: Final[int] = 150

# OPTION: To be super-explicit (and super professional),
# use `Final` from the `typing` module for all constants.

# RECOMMENDED: See the other file for examples.

# TODO: Declare and initialize a string (str) variable of your choice.


# TODO: Declare and initialize an integer (int) variable of your choice.


# TODO: Declare and initialize a float (float) variable of your choice.


# TODO: Declare and initialize a boolean (bool) variable of your choice (True or False).


# TODO: Declare and initialize a list of strings (list[str]) variable of your choice.
# Remember that strings must be in quotes, items are separated by commas,
# and the whole list is wrapped in square brackets. (See the other file for examples.)


# === DECLARE A FUNCTION TO FORMAT THE INFORMATION ===


def get_summary() -> str:
    """Get a formatted summary of the information held in the global variables.

    Arguments: None (nothing is passed in the parentheses after `get_summary`).

    Returns: - a formatted multi-line string (starts with f and wrapped in triple quotes).
    """
    # TODO: Create and return a multi-line f-string (triple-quoted) that includes
    # all of the global variables you declared above, each on its own line,
    # labeled clearly with descriptive text.
    # See the other file for an example. Remember to start the string with an f!
    summary: str = """

    TODO: Don't forget to add an f at the start of this string to make it an f-string!
    Your Summary will be about half the size because you can choose
    to declare variables either WITH or WITHOUT Final, as you prefer.
    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Entry point when running this file as a Python script.

    Arguments: None (nothing is passed in the parentheses after the `main`).

    Returns: None (nothing is returned when this function runs).

    This function creates what we call `side effects` -
    it just logs output to the console and a file.

    Use the LOG variable to call info() methods to log messages.
    Call the log_header() function once to log some key details that can help with debugging.
    Call the get_summary() function to get the formatted summary string,
    Log the summary string we get back from get_summary().
    """
    LOG.info("=================")
    log_header(LOG, "Foundations of Professional Python")
    LOG.info("=================")

    LOG.info("START main()")

    summary: str = get_summary()
    LOG.info(summary)

    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If running this file as a script, then call main() function.
# OBS: This is just standard Python boilerplate.
# OBS: We copy and paste it and do not bother to memorize it.

if __name__ == "__main__":
    main()
