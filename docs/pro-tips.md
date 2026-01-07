# Pro-Tips

## Terminal Tips

- Use the terminal command `clear` to clear output.
- Use the **UP ARROW** key and **DOWN ARROW** key to scroll through past commands.
- Use **CTRL f** to find (and replace) with in a file.
- Use **CTRL SHIFT f** to find (and replace) across all files.

Global changes in a file or across the repo may have unintended consequences.
Be careful - review each change carefully.

## Trouble-Shooting

### ERROR: Stuck at >>> or ...? You're in Python interactive mode

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl c` (both keys together) - or `Ctrl Z` then `Enter` on Windows.

### ERROR: Failed to canonicalize path

Try to reinstall:

```shell
uv sync --extra dev --reinstall
```
