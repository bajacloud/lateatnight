from flask import Flask
import sys
import pkg_resources
from PIL import Image

app = Flask(__name__)

# Dummy operation with Pillow to ensure it's loaded
dummy_image = Image.new('RGB', (10, 10), color='white')

@app.route('/')
def list_packages():
    # Explicit reference to Flask and Pillow
    flask_ref = Flask
    pillow_ref = Image

    # List of all installed packages
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    installed_packages_list = '<br>'.join(sorted(installed_packages))

    # List of actively loaded modules (attempting a more direct approach)
    loaded_modules = {pkg.key for pkg in pkg_resources.working_set if pkg.key in sys.modules}
    loaded_modules_list = '<br>'.join(sorted(loaded_modules))

    # Calculate the delta: Packages installed but not actively loaded
    unused_packages = installed_packages - loaded_modules
    unused_packages_list = '<br>'.join(sorted(unused_packages))

    # HTML to display all three lists
    html = f"""
    <h2>Installed Packages</h2>
    <div style='border:1px solid black; margin-bottom:20px; padding:10px;'>
        {installed_packages_list}
    </div>
    <h2>Actively Loaded Modules</h2>
    <div style='border:1px solid black; margin-bottom:20px; padding:10px;'>
        {loaded_modules_list}
    </div>
    <h2>Unused Packages (Installed but Not Loaded)</h2>
    <div style='border:1px solid black; margin-bottom:20px; padding:10px;'>
        {unused_packages_list}
    </div>
    """

    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
