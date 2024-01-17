Notes on Using tox
==================

Below, where the command `tox ...` is run, you will need instead to run
`./.build/virtualenv/bin/tox ...` when not in an activated virtual
environment.

After editing the config file, run `tox config` and check for lines
containing warnings like `# !!! unused: ignore_base_python_conflict`. This
indicates that you've put a setting in the wrong section of the `tox.ini`
file (in this case, in `[testenv]` instead of `[tox]`).
