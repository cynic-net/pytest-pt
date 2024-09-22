Changelog
=========

This file follows most, but not all, of the conventions described at
[keepachangelog.com]. Especially we always use [ISO dates]. Subsections or
notations for changes may include Added, Changed, Deprecated, Fixed,
Removed, and Security.

Release version numbers follow the [Python packaging
specifications][pyver], which are generally consistent with [semantic
versioning][semver]: are _major.minor.patch_ Development versions use the
version number of the _next_ release with _.devN_ appended; `1.2.3.dev4` is
considered to be earlier than `1.2.3`.

On any change to the programs or libraries (not, generally, the tests), the
previous release version number is bumped and `.devN` is appended to it, if
this hasn't already been done. A `.devN` suffix will stay until the next
release, though its _N_ need not be bumped unless the developer feels the
need.

Releases are usually tagged with `vN.N.N`. Potentially not all releases
will be tagged, but specific releases can also be fetched via the Git
commit ID.

#### dev

#### 1.0.0 (2024-09-22)
- Changed: Upgraded dev status to "Production/Stable"
- Changed: Official package name, URLs, etc. is `pytest-pt` (`_`→`-`)
- Docs: Update installation/activate instructions.

#### 0.0.2 (2024-05-15)
- Changed: Package metadata now includes URLs, license, etc.

#### 0.0.1 (2024-05-15)
- Initial release as distribution package.



<!-------------------------------------------------------------------->
[ISO dates]: https://xkcd.com/1179/
[keepachangelog.com]: https://keepachangelog.com/
[pyver]: https://packaging.python.org/en/latest/specifications/version-specifiers/#version-specifiers
[semver]: https://en.wikipedia.org/wiki/Software_versioning#Semantic_versioning
