# Adapted from a script by Eli Bendersky
# http://eli.thegreenplace.net/2013/04/20/bootstrapping-virtualenv

import sys
import subprocess

VENV_VERSION = '15.0.3'


#PYPI_VENV_BASE = 'http://pypi.python.org/packages/source/v/virtualenv'
# https://bitbucket.org/pypa/pypi/issues/438/backwards-compatible-un-hashed-package
# https://wiki.debian.org/debian/watch
PYPI_VENV_BASE = 'http://pypi.debian.net/virtualenv'

PYTHON = 'python'
INITIAL_ENV = 'venv'

def shellcmd(cmd, echo=True):
    """ Run 'cmd' in the shell and return its standard out.
    """
    if echo: print '[cmd] {0}'.format(cmd)
    out = subprocess.check_output(cmd, stderr=sys.stderr, shell=True)
    if echo: print out
    return out

dirname = 'virtualenv-' + VENV_VERSION
tgz_file = dirname + '.tar.gz'

# Fetch virtualenv from PyPI
venv_url = PYPI_VENV_BASE + '/' + tgz_file
shellcmd('curl -LO {0}'.format(venv_url))

# Untar
shellcmd('tar xzf {0}'.format(tgz_file))

# Create the initial env
shellcmd('{0} {1}/virtualenv.py {2}'.format(PYTHON, dirname, INITIAL_ENV))

# Install the virtualenv package itself into the initial env
shellcmd('{0}/bin/pip install {1}'.format(INITIAL_ENV, tgz_file))

# Cleanup
shellcmd('rm -rf {0} {1}'.format(dirname, tgz_file))
