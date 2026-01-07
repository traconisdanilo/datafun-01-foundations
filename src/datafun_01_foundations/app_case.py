"""app_case.py - Project script (example).

Author: Denise Case
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
  Don't edit this file - it should remain a working example.
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

COURSE_NAME: str = "Data Analytics Fundamentals"
COURSE_NUMBER: int = 608
COURSE_HOURS_PER_WEEK: float = 20.0
ASSUMES_PRIOR_EXPERIENCE: bool = (
    False  # NOTE: In Python, True and False are Capitalized (and not quoted).
)

HELPFUL_TRAITS: list[str] = [
    "patience",
    "curiosity",
    "humor",
    "tenacity",
]

# OPTION: To be super-explicit (and super professional),
# use `Final` from the `typing` module for all constants.

PROJECT_NAME: Final[str] = "Project 01"
PROJECT_NUMBER: Final[int] = 1
PROJECT_HOURS_PER_WEEK: Final[float] = 8.0
USES_PROFESSIONAL_PYTHON: Final[bool] = True

REQUIRED_SKILLS: Final[list[str]] = [
    "variables",
    "lists",
    "f-strings",
    "logging",
]


# === DECLARE A FUNCTION TO FORMAT THE INFORMATION ===


def get_summary() -> str:
    """Get a formatted summary of the information held in the global variables.

    Arguments: None (nothing is passed in the parentheses after `get_summary`).

    Returns: - a formatted multi-line string (starts with f and wrapped in triple quotes).
    """
    summary: str = f"""
    Course Information:
        Course name: {COURSE_NAME}
        Course number: {COURSE_NUMBER}
        Course hrs/wk: {COURSE_HOURS_PER_WEEK:.2f}
        Assumes prior experience: {ASSUMES_PRIOR_EXPERIENCE}
        Helpful traits: {HELPFUL_TRAITS}

    Project Information:
        Project name: {PROJECT_NAME}
        Project number: {PROJECT_NUMBER}
        Project hrs/wk: {PROJECT_HOURS_PER_WEEK:.2f}
        Uses professional Python: {USES_PROFESSIONAL_PYTHON}
        Required skills: {REQUIRED_SKILLS}
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
# OBS: Just copy and paste it - do not bother to memorize it.

if __name__ == "__main__":
    main()
