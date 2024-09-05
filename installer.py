import PyInstaller.__main__

PyInstaller.__main__.run([
    '--name=MyApp',
    '--onefile',  # Generate a single executable
    '--windowed',  # No console window (use '--console' if you want a console)
    'app.py',  # Your main application file
])
