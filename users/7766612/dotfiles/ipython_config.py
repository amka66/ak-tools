# Get the config object
c = get_config()

# Load extensions
c.InteractiveShellApp.extensions = ['autoreload',  'ipython_cells']

# Run extention configuration
c.InteractiveShellApp.exec_lines = ['%autoreload 2']
