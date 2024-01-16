pytest_pt: pytest plugin to use `*.pt` files as tests
=====================================================

This [pytest] plugin will collect `*.pt` files as test modules. It
uses a custom module loader that always uses importlib (like specifying
`importmode=importlib` to the standard pytest loader) and generates
a module name ending in `~pt` to prevent namespace collisions.

Use this by deposting the [`pylib/pytest_pt.py`][pytest_pt] in any
directory where it will be found as the code for a (top-level) module, and
import it in a [`conftest.py`][conftest] in one or more directories under
which you want to collect `*.pt` files:

    from pytest_pt import *     # Plugin to find/execute .pt files as tests

This documentation should be expanded to explain more about the purpose of
this, how it works, and how the tests (run with `./Test`) work. Contact the
author if you're needing further documentation or help: Curt J. Sampson
<cjs@cynic.net>.



<!-------------------------------------------------------------------->
[conftest]: ./pylib/conftest.py
[pytest]: https://pytest.org/
[pytest_pt]: ./pylib/pytest_pt.py
