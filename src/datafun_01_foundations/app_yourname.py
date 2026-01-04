"""app_yourname.py - Project 1 main script.

TODO: Replace "yourname" in the filename with your actual name or alias.

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

# Imports from the Python standard library (free stuff that comes with Python).
import logging
from typing import Final

# Imports from external libraries (these must be listed in pyproject.toml).
from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (FILE) ===

LOG: logging.Logger = get_logger("P01", level="DEBUG")

# === DECLARE SOME GLOBAL VARIABLES ===

# All of these global variables are constant - they do NOT change when the program runs.
# By convention, constant variable names are all UPPERCASE_WITH_UNDERSCORES.
# Declare a variable and initialize it with a value for each of these common types:
# str, int, float, bool, list of strings.
# Use `type hints` to make types explicit.
# For example:

MY_ANALYTICS_COMPANY: Final[str] = "DataFun Analytics"
MY_EMPLOYEE_COUNT: Final[int] = 150

# OPTION: To be super-explicit (and super cool), use `Final` from the `typing` module for all constants.


# RECOMMENDED: See the other file for examples.

# TODO: Declare and initialize a string (str) variable of your choice.

# TODO: Declare and initialize an integer (int) variable of your choice.

# TODO: Declare and initialize a float (float) variable of your choice.

# TODO: Declare and initialize a boolean (bool) variable of your choice.

# TODO: Declare and initialize a list of strings (list[str]) variable of your choice.
# Remember that strings must be in quotes, items are separated by commas,
# and the whole list is wrapped in square brackets. (See the other file for examples.)


# === DECLARE ONE FUNCTION TO FORMAT INFORMATION ===


def get_summary() -> str:
    """Get a nicely formatted summary of the information held in the global variables.

    Arguments: None (nothing is passed in the parentheses after `get_summary`).

    Returns: - a formatted multi-line string.
    """
    # TODO: Create and return a multi-line f-string (triple-quoted) that includes
    # all of the global variables you declared above, each on its own line,
    # labeled clearly with descriptive text.
    # See the other file for an example. Remember to start the string with an f!
    summary: str = """

    TODO: Don't forget to add an f at the start of this string to make it an f-string!

    """

    LOG.info("Generated summary information.")
    LOG.info("Returning the summary string to the calling function.")
    return summary


# === DEFINE THE MAIN FUNCTION THAT WILL CALL OUR FUNCTIONS ===


def main() -> None:
    """Entry point for the script.

    Arguments: None (nothing is passed in the parentheses after the `main`).

    Returns: None (nothing is returned when this function runs).

    This function creates what we call `side effects` -
    like logging output to the console and a file.
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
