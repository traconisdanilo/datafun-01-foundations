# Example Output

After running:

```shell
uv self update
uv python install 3.12
uv sync --extra dev --extra docs --upgrade
uv run python src/datafun_01_foundations/app_case.py
```

```text
2026-MM-DD 11:42:53 | INFO | P01 | project=Foundations of Professional Python
2026-MM-DD 11:42:53 | INFO | P01 | repo_dir=datafun-01-foundations
2026-MM-DD 11:42:53 | INFO | P01 | python=3.12.4
2026-MM-DD 11:42:53 | INFO | P01 | os=Windows 11
2026-MM-DD 11:42:53 | INFO | P01 | shell=powershell
2026-MM-DD 11:42:53 | INFO | P01 | cwd=.
2026-MM-DD 11:42:53 | INFO | P01 | github_actions=False
2026-MM-DD 11:42:53 | INFO | P01 | =================
2026-MM-DD 11:42:53 | INFO | P01 | START main()
2026-MM-DD 11:42:53 | INFO | P01 | Generated summary information.
2026-MM-DD 11:42:53 | INFO | P01 | Returning the summary string to the calling function.
2026-MM-DD 11:42:53 | INFO | P01 |
    Course Information:
        Course name: Project 01
        Course number: 608
        Course hrs/wk: 20.00
        Assumes prior experience: False
        Helpful traits: ['patience', 'curiosity', 'humor', 'tenacity']

    Project Information:
        Project name: Project 01
        Project number: 1
        Project hrs/wk: 8.00
        Uses professional Python: True
        Required skills: ['variables', 'lists', 'f-strings', 'logging']
```

After running:

```shell
uv run python src/datafun_01_foundations/app_yourname.py
```

```text
2026-MM-DD 13:06:54 | INFO | P01 | =================
2026-MM-DD 13:06:54 | INFO | P01 | === RUN START ===
2026-MM-DD 13:06:54 | INFO | P01 | project=Foundations of Professional Python
2026-MM-DD 13:06:54 | INFO | P01 | repo_dir=datafun-01-foundations
2026-MM-DD 13:06:54 | INFO | P01 | python=3.12.4
2026-MM-DD 13:06:54 | INFO | P01 | os=Windows 11
2026-MM-DD 13:06:54 | INFO | P01 | shell=powershell
2026-MM-DD 13:06:54 | INFO | P01 | cwd=.
2026-MM-DD 13:06:54 | INFO | P01 | github_actions=False
2026-MM-DD 13:06:54 | INFO | P01 | =================
2026-MM-DD 13:06:54 | INFO | P01 | START main()
2026-MM-DD 13:06:54 | INFO | P01 | Generated summary information.
2026-MM-DD 13:06:54 | INFO | P01 | Returning the summary string to the calling function.
2026-MM-DD 13:06:54 | INFO | P01 |

    Don't forget to add an f at the start of this string to make it an f-string!


2026-MM-DD 13:06:54 | INFO | P01 | END main()
```
