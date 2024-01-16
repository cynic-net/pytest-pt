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

Versions Supported
------------------

This supports only pytest 5 and pytest 7; pytest 6 doesn't seem worth
supporting because we have no legacy users of it.

- Python 6 probably works, but is not tested due to tox being unhappy about
  using it.
- pytest 5 is supported on versions of Python up to 3.9, but not on 3.10
  and above.
- pytest 7 is tested on Pythons up to 3.12, and will probably work on newer
  versions of Python when they are released.

### Testing

The top-level `./Test` script runs tests for all supported versions of
Python and pytest. You do not need `tox` installed (or even `pip` or
`virtualenv`); the script will take care of bootstrapping those into a
local virtualenv using [pactivate].

The script assumes you're using [pythonz] to supply the various versions of
Python this is tested with; if it cannot find pythonz it will complain and
stop. Giving `-B` as the first option to `./Test` will install or update
pythonz if necessary, and build the latest patch version of Python for each
of the minor releases that are tested.

The test script can be updated to use Pythons from other sources, if
there is any call for it.


Further Documentation
---------------------

This documentation should be expanded to explain more about the purpose of
this, how it works, and how the tests (run with `./Test`) work. Contact the
author if you're needing further documentation or help: Curt J. Sampson
<cjs@cynic.net>.



<!-------------------------------------------------------------------->
[conftest]: ./pylib/conftest.py
[pactivate]: https://github.com/cynic-net/pactivate
[pytest]: https://pytest.org/
[pytest_pt]: ./pylib/pytest_pt.py
[pythonz]: https://github.com/saghul/pythonz
