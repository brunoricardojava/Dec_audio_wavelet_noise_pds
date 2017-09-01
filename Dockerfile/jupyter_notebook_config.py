

# Password to use for web authentication
c = get_config()
c.NotebookApp.password = u'sha1:aeed80c475e3:eec4bb455f68263fc6825a1b4626312790fc9af0'
c.NotebookApp.iopub_data_rate_limit = 10000000