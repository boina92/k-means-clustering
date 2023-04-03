import os

c.NotebookApp.allow_origin = '*'
c.NotebookApp.disable_check_xsrf = True
c.NotebookApp.allow_credentials = True
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.notebook_dir = os.getcwd()
c.NotebookApp.token = ''
c.NotebookApp.password = u''
c.NotebookApp.password_required = False
c.NotebookApp.disable_check_xsrf = True
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' *"
    }
}
