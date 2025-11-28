import  nox
from    collections  import defaultdict
from    subprocess  import run
from    sys  import stderr


@nox.session
@nox.parametrize(
    'pytest', (5, 7, 9)
)
def tests(session, pytest):
    session.run('python', '--version')
    #   XXX `N.0` means exact _N_ but not exact _0_; it may be larger.
    session.install(f'pytest~={pytest}.0')
    session.install('-e', '.')
    session.run('pytest', '--version')

####################################################################
#   Python interpreter discovery/selection.

def python_versions() -> (int,int,int):
    ''' Get all versions of CPython known to ``pythonz`` and reduce the
        list to the latest M.N.p version for each M.N, returning the
        version numbers as (M,N,p) tuples.
    '''
    command = ('pythonz', 'list',
        '-t', 'cpython',            # only standard CPython versions
        '-a',                       # all known versions, installed or not
        )
    try:
        result = run(command, check=True, capture_output=True, text=True)
    except Exception as ex:
        print(f"Cannot run 'pythonz': {ex}", file=stderr)
        exit(1)

    verstrs = ( v.strip()
                for v in result.stdout.split('\n')
                if v.strip() and not '#' in v )
    vertups = ( tuple(map(int, v.split('.'))) for v in verstrs )
    verdict = defaultdict(list)
    for vt in vertups:  verdict[f'{vt[0]}.{vt[1]}'].append(vt)
    vermax  = ( max(vs) for vs in sorted(verdict.values()))
    return vermax

def python_paths(vers:(int,int,int)) -> (str):
    #   XXX not clear what to do about versions that we don't find.
    #   Actually, the overall organisation seems wrong: we want to start
    #   with a list of M.N versions and find out a) what the latest version
    #   known to pythonz is, and b) what the latest installed version is.
    #   Then warn if installed version is older (or not?) and ask for an
    #   install if no version installed.
    for vtup in vers:
        vstr = '.'.join(map(str, vtup))
        print(vstr)

print(python_paths(python_versions()))
exit(99)

