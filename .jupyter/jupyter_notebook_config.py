import os

c.NotebookApp.allow_origin = '*'
c.NotebookApp.disable_check_xsrf = True
c.NotebookApp.token = ''
c.NotebookApp.password = ''
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.notebook_dir = os.getcwd()
