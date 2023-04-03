import os

c.NotebookApp.allow_origin = '*'
c.NotebookApp.disable_check_xsrf = True
c.NotebookApp.allow_credentials = True
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.notebook_dir = os.getcwd()
c.NotebookApp.password = 'sha1:2c5b5574939c:7e4edf4c4ec3f75c3c7e26c3d1f8f1adad8029ba'
c.NotebookApp.disable_check_xsrf = True
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' *"
    }
}
