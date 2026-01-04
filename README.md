# datafun-01-foundations

> Professional Python project: creating variables and running code.

## This Project Repository

This repository is a **Python project** that illustrates:

- How professional Python projects are organized
- How to declare variables in Python
- How to run Python code from the terminal
- How to save and submit work using GitHub

There are **many files** in this repository.
**Ignore most of them.**
For this project, you edit **one file only**.

## Our Focus: Python Source Code

Python code is kept in the `src/` folder.
There are two files: 1) a working example and 2) the file you will edit:

```
src/datafun_01_foundations/app_case.py
src/datafun_01_foundations/app_yourname.py
```

Everything else just facilitates collaboration and quality.

## Project 01 Planning

Think about some different kinds of data attributes - they can be real or fictional.

1. One that holds a **True or False** value (e.g. isWorking, isParent, hasPet)
2. One that holds an **integer** (e.g. year_starting_grad_school)
3. One that holds a **floating point number** (e.g. experience_factor)
4. One that holds a **string of characters (text)** (e.g. city, company_name, analytic_specialty)
5. One that holds a **list of strings** (e.g., skills, interests, favorite_teams)

Following the example (`app_case.py`), decide on a name for each variable.
Name it according to Python conventions.
Signal the type of value that variable holds.
Initialize the variable to some value.
After declaring all these global variables, use Python formatted strings (f-strings) to display the information.

## Process Overview

- First, set up your machine.
- Second, set up the project.
- Third, follow the daily workflow.
- Complete the project objectives.

Details provided below.

## 01: Set Up Machine (Once Per Machine)

<details>
<summary><strong>
Click Here for Details
</strong></summary>

First, **set up your machine**.
Detailed instructions for each step are available at:
[**01 - Set Up Your Machine**](https://denisecase.github.io/pro-analytics-02/01-set-up-machine/)

1. Create a GitHub account.

2. The instructions show how to:

   - See **file extensions** (e.g. `.md`, `.py`)
   - See **hidden** files and folders

3. The instructions show how to install and verify:

   - **Git**
   - **uv**
   - **Visual Studio Code (VS Code)**

4. The instructions show how to configure git with your user.name and user.email.

5. The instructions show how to create `Repos/`, a folder for repos on your machine that is NOT in the automatically-synced Documents folder.

6. Verify these steps carefully.

</details>

🛑 Do not continue until all steps are complete and verified.

## 02: Set Up Project (once Per Project)

<details>
<summary><strong>
Click Here for Details
</strong></summary>

Second, **set up your project**.
Detailed instructions for each step are available at:
[**02 - Set Up Your Project**](https://denisecase.github.io/pro-analytics-02/02-set-up-project/)

### Step 2.1: Start in GitHub

1. Sign in to GitHub
2. Open this repository in your browser
3. Click **Use this template** or **Copy this template**
4. Create the repository in **your own GitHub account**

### Step 2.2: Enable GitHub Pages (once for this repository)

1. Open **your new repository** on GitHub
2. Click **Settings** (gear icon)
3. Click **Pages** (left menu)
4. Under **Build and deployment**: Set the Source to: **GitHub Actions**

This enables project documentation later.

### Step 2.3: Clone To Local And Open in VS Code

1. From the address bar in your web browser, copy your repository URL from GitHub (it starts with `https://github.com/YOURACCOUNT/datafun-01-foundations`).
2. Open a **terminal** in your `Repos` folder on your machine. For help, see [Clone Repo](https://denisecase.github.io/pro-analytics-02/02-set-up-project/03-clone-repo-to-local/).
3. Edit the command to replace YOURACCOUNT with your GitHub account name (e.g. `denisecase`)
4. Type the following commands **exactly**, pressing ENTER after each line:

```shell
git clone https://github.com/YOURACCOUNT/datafun-01-foundations
cd datafun-01-foundations
code .
```

What these do:

- `git clone` downloads the project
- `cd` moves into the project folder
- `code .` opens the project in VS Code

### Step 2.4: Initialize Local Development Environment

1. If VS Code recommends extensions (from .vscode/extensions.json), click **Install All**.
2. In VS Code, confirm only this project folder is open.
3. From VS Code Menu, select **Terminal** / **New Terminal**.
4. In the terminal (at the project root), run these commands one at a time (hit Enter after each):

```shell
uv self update
uv python pin 3.12
uv sync --extra dev --extra docs --upgrade
```

This will:

1. Update `uv`
2. Pin the Python version for this repo (install if needed)
3. Install project dependencies

</details>

🛑 Do not continue until all steps are complete and verified.

## 03: Daily Workflow (Working With Python Project Code)

### Step 3.1. Sync Before Start

When starting a new session always git pull the current content from the GitHub repo.

```shell
git pull
```

You might not have changed anything in the GitHub version but this one habit can save you a lot of time down the road.

### Step 3.2. Run Code and Checks

Run the example and your file:

```shell
uv run python src/datafun_01_foundations/app_case.py
uv run python src/datafun_01_foundations/app_yourname.py
```

If you see output and no errors, your environment is set up correctly.

Run some checks:

```shell
uv run ruff check .
uv run ruff format .
uv run pytest --cov=src --cov-report=term-missing
```

### Step 3.3. Build and Serve Project Documentation:

```shell
uv run mkdocs build --strict
uv run mkdocs serve
```

> To stop a running Python program, press `Ctrl + C` in the terminal

### Step 3.4: Save Progress (add-commit-push)

With git, saving is a 3-step process: add, commit, and push.
Professionals often do this many times a day.
Use your VS Code terminal to run these commands one at a time.
Be sure your terminal is open in the root project folder, `datafun-01-foundations`.

```shell
git add -A
git commit -m "init project"
git push -u origin main
```

<details>
<summary><strong>
Click for Details (add-commit-push)
</strong></summary>

These commands do the following:

- `git add ...` - stages all changes (everything we've added, edited, or deleted)
- `git commit ...` - saves a snapshot with a short message in quotes
- `git push` - pushes changes up to `origin` - the GitHub repo for safe keeping and sharing

- Commit messages matter - we use `-m` followed by a short message in quotes
  describing what was done, e.g. "complete first TODO", "final commit", etc.

- In the `git push` command, the `-u origin main`
  tells Git to remember we push to `origin` (our GitHub repo)
  on the `main` branch.
  Future push commands can simply use `git push`.

- Git is widely used in industry.
  School is a great place to learn (nothing critical here like there will be at work).

</details>

---

## Project Objectives

Project Task 1. Personalize Your Documentation Links

Open [mkdocs.yml](./mkdocs.yaml).
This file configures the associated project documentation website (powered by MkDocs)
Use CTRL f to find each occurance of the source GitHub account (e.g. `denisecase`).
Change each occurance to point to your GitHub account instead (spacing and capitalization MUST match the URL of your GitHub account **exactly**.)

Project Task 2. Implement Custom Variables and Functions

1. Read the example app_case.py carefully first. Then start on yours.
2. Search for "TODO" items. VS Code has icons down the left. Use either TODO Tree (tree, at the bottom) or Search (second from top).
3. Complete each TODO carefully - one at a time.
4. Test the command and ensure your script still runs.
5. When it works without errors, delete the TODO command - do not leave them in your project.

That's an important change so follow the steps above to git add-commit-push again.

## Troubleshooting

### Stuck at >>> or ...? You're in Python interactive mode

If you see something like this in your terminal:

`>>>` or `...`

you accidentally started Python interactive mode.
It happens.

Press `Ctrl c` (both keys together) - or `Ctrl Z` then `Enter` on Windows.

## Tips

- Use the terminal command `clear` to clear output.
- Use the up and down arrow keys to scroll through past commands.
- Use CTRL f to find (and replace) with in a file.
- Use CTRL SHIFT f to find (and replace) across all files (this is powerful and often has unintended consequences - be careful - consider reviewing each change carefully).
  


