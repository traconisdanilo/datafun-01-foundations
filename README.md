# datafun-01-foundations

> Professional Python project: creating variables and running code.

## Project Planning

Think about different kinds of data - real or fictional.
Then think about a good name to hold that value in code.

1. A **True or False** value (e.g. `isWorking`, `isParent`, `hasPet`)
2. An **integer** (e.g. `year_starting_grad_school`)
3. A **floating point number** (e.g. `experience_factor`)
4. A **string of characters (text)** (e.g. `city`, `company_name`, `analytic_specialty`)
5. A **list of strings** (e.g., `skills`, `interests`, `favorite_teams`)

Following the example ([`app_case.py`](./src/datafun_01_foundations/app_case.py)),
decide on a name for each type of variable.
Name it according to Python conventions.
Signal the **type** of value that variable holds by using `type hints`.
**Initialize** the variable to some value.
After declaring these as global constant variables,
use Python **f-strings** (formatted strings) to display the information.

---

## This Project Repository

This repository (also known as **repo**) is a **Python project** that illustrates:

- How professional Python projects are **organized**
- How to **declare** variables in Python
- How to **run** Python code from the terminal
- How to **save and share** work using GitHub

There are **many files** in this repository.
**You can ignore most of them.**
For this project, you edit **only one file**.

## Our Focus: Python Code

Python modules (files) are kept in the `src/` folder.
In our projects, there will typically be two files:

1. a working example (don't change it)
2. a similar file that you edit and implement

Everything else just facilitates **collaboration** and **quality**.

## Three Workflows

There are three workflows for analytics projects.
Complete the first two - and then use the third to complete the project.
Details provided below.

- 01: Set Up Machine (Once Per Machine)
- 02: Set Up Project (once Per Project)
- 03: Daily Workflow (Working With Python Project Code)

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

### Step 2.1: From GitHub, Copy The Repo

1. Sign in to GitHub
2. Open this repository in your browser
3. Click **Use this template** or **Copy this template**
4. Create the repository in **your own GitHub account**

### Step 2.2: In Your GitHub Repo Settings, Set Up Pages

1. Open **your new repository** on GitHub
2. Click **Settings** (gear icon)
3. Click **Pages** (left menu)
4. Under **Build and deployment**: Set the Source to: **GitHub Actions**

This enables project documentation later.

### Step 2.3: Clone Your Repo and Open in VS Code

1. From the address bar in your web browser, copy your repository URL from GitHub (it starts with `https://github.com/YOURACCOUNT/datafun-01-foundations`).
2. Open a **terminal** in your `Repos` folder on your machine. For additional help, see [Clone Repo](https://denisecase.github.io/pro-analytics-02/02-set-up-project/03-clone-repo-to-local/).
3. After fixing the URL, type or paste the following commands into your machine's terminal, pressing ENTER after each line. Commands must be exact.

```shell
git clone https://github.com/YOURACCOUNT/datafun-01-foundations
cd datafun-01-foundations
code .
```

What these do:

- `git clone` downloads the project to your machine
- `cd` changes directory into the project folder
- `code .` opens the project in VS Code

### Step 2.4a: Initialize Local Development Environment

1. When VS Code opens the project, accept the recommended extensions and **Install All** (you can see the list in `.vscode/extensions.json`).
2. In VS Code, confirm that **only this project folder is open**.
3. From VS Code Menu, select **Terminal** / **New Terminal**.
4. In the terminal (which will open in the root project folder), run these commands one at a time (hit Enter after each):

```shell
uv self update
uv python pin 3.12
uv sync --extra dev --extra docs --upgrade
```

This will:

1. Update `uv`
2. Pin the Python version for this repo (and install that version if needed)
3. Install project dependencies listed in `pyproject.toml`.


### Step 2.4b: Align VS Code with The Environment (.venv)

1. In VS Code, select the project Python interpreter

- Open the Command Palette (View / Command Palette) or hit Ctrl + Shift + p.
- Type and choose: `Python: Select Interpreter`
- Important: Choose the interpreter inside **this project's `.venv` folder**

2. Restart the Python language server

- Open the Command Palette (View / Command Palette) or hit Ctrl + Shift + p.
- Type or choose: `Developer: Reload Window`

</details>

🛑 Do not continue until all steps are complete and verified.

## 03: Daily Workflow (Working With Python Project Code)

This is where the fun begins.

<mark>
> **Professional habit**: always `git pull` before starting, then repeatedly **EDIT**  > **RUN**  > **CHECK**  > **SAVE** (git `add-commit-push`) as you make progress.
</mark>

### Step 3.1. Git Pull Before Starting Work

When starting a new session always `git pull` to get current content from the GitHub repo.
You might not have changed anything yet, but this one professional habit can save a LOT of time down the road.

```shell
git pull
```

### Step 3.2. Run Code and Checks (Edit and Repeat)

Run the example and your file:

```shell
uv run python src/datafun_01_foundations/app_case.py
uv run python src/datafun_01_foundations/app_yourname.py
```

If you see output and no errors, your environment is set up correctly.
Congratulations!

Run some checks:

```shell
uv run ruff format .
uv run ruff check . --fix
uv run pytest --cov=src --cov-report=term-missing
```

### Step 3.3. Build and Serve Project Documentation:

```shell
uv run mkdocs build --strict
uv run mkdocs serve
```

> To stop a running Python program, press `Ctrl + C` in the terminal

### Step 3.4: Save Progress (add-commit-push)

As we edit project code and docs, we repeat the commands above to run them, check them, and rebuild docs as needed.

When a change works successfully, we save our progress.
Use your VS Code terminal to run these commands one at a time.
Your terminal should be open in the root project folder, `datafun-01-foundations`.

```shell
git add -A
git commit -m "update"
git push -u origin main
```

<details>
<summary><strong>
Click for Details (add-commit-push)
</strong></summary>

We run these commands frequently. These important commands do the following:

- `git add ...` - stages all changes (everything we've added, edited, or deleted)
- `git commit ...` - saves a snapshot with a short message in quotes
- `git push` - pushes changes up to `origin` - the GitHub repo for safe keeping and sharing

Commit messages matter - we use `-m` followed by a short message
(in **quotes**) describing what was done, e.g. "complete first TODO", "final commit", etc.

In the `git push` command, the `-u origin main`
tells Git to remember we push to `origin` (our GitHub repo) on the `main` branch.
Future push commands can simply use `git push`.

Git is powerful and widely used in industry.
School is a great place to learn and get all the initial git mistakes out of the way.
There is nothing critical here at school and if we mess it all up, we just start over.
All practice is good practice.
**Courage** and a **sense of humor** are helpful when starting with Git.

</details>

---

## Project Objectives

Project Task 1. Personalize Your Documentation Links

Open [mkdocs.yaml](./mkdocs.yaml).
This file configures the associated project documentation website (powered by MkDocs)
Use CTRL f to find each occurrence of the source GitHub account (e.g. `denisecase`).
Change each occurrence to point to your GitHub account instead (spacing and capitalization MUST match the URL of your GitHub account **exactly**.)

Project Task 2. Personalize Your Python File

1. Rename `app_yourname.py` to reflect your name or alias.

- Find the file the file in the VS Code Explorer window (top icon on the left).
- Right-click / Rename.
- Follow conventions: name Python files in lower_snake_case, words joined with underscores, and using `.py` extension.

2. Edit this README.md file to change the run command to call your file instead.
   Use CTRL f to search for `app_yourname.py` and replace all occurrences exactly.
3. Preview this README.md to make sure it still appears correctly.
   - Find README.md in the VS Code Explorer window (top icon on the left)
   - Right-click / Preview
   - Fix any issues.
4. Run the updated command to execute **your** Python script.

Project Task 3. Implement Your Python File

1. Read the example code carefully **before** starting.
2. Open your file. Search for "TODO" items. VS Code has icons down the left. Use either TODO Tree (tree, at the bottom) or Search (second from top).
3. Complete each TODO carefully, one at a time.
4. After implementing a TODO, paste your run command in the terminal and hit Enter to re-run it.
5. When it runs without errors, delete the associated TODO command.
6. Keep working through each TODO.
7. When you finish, there should be **zero TODO occurrences** in your project.

**Save often**: After making any useful progress, follow the steps to git add-commit-push.

---

## Out of Scope

- You do not need to add to or modify `tests/`. They are provided for example only.
- You do not need to view or modify any of the supporting **config files**.
- Much of the repo includes silent helpers. Explore as you like, but nothing is required.
- You do NOT need to understand everything. Understanding grows naturally as we do more projects and you see  repetition and reuse across many different analytics projects.

## Troubleshooting

### Stuck at >>> or ...? You're in Python interactive mode

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl c` (both keys together) - or `Ctrl Z` then `Enter` on Windows.

- See [pro-tips](./docs/pro-tips.md)
