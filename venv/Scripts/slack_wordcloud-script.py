#!G:\PythonSystemStudy\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'slack-wordcloud==1.0.4','console_scripts','slack_wordcloud'
__requires__ = 'slack-wordcloud==1.0.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('slack-wordcloud==1.0.4', 'console_scripts', 'slack_wordcloud')()
    )
