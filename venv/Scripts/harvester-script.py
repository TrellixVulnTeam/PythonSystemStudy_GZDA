#!G:\PythonSystemStudy\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'captcha-harvester==2.1.1','console_scripts','harvester'
__requires__ = 'captcha-harvester==2.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('captcha-harvester==2.1.1', 'console_scripts', 'harvester')()
    )
