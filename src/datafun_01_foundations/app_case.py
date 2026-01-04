"""app_case.py - Project 1 main script.

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

COURSE_NAME: str = "Project 01"
COURSE_NUMBER: int = 608
COURSE_HOURS_PER_WEEK: float = 20.0
ASSUMES_PRIOR_EXPERIENCE: bool = (
    False  # NOTE: In Python, True and False are capitalized.
)

HELPFUL_TRAITS: list[str] = [
    "patience",
    "curiosity",
    "humor",
    "tenacity",
]

# To be super-explicit (and super cool), use `Final` from the `typing` module for all constants.

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


# === DECLARE ONE FUNCTION TO FORMAT INFORMATION ===


def get_summary() -> str:
    """Get a nicely formatted summary of the information held in the global variables.

    Arguments: None (nothing is passed in the parentheses after `get_summary`).

    Returns: - a formatted multi-line string.
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
