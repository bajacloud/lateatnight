from flask import Flask
import sys
import pkg_resources
from PIL import Image, ImageDraw

app = Flask(__name__)

# Simple use of Pillow to ensure it's loaded
def create_dummy_image():
    image = Image.new('RGB', (100, 100), color = (73, 109, 137))
    d = ImageDraw.Draw(image)
    d.text((10, 10), "Hello", fill=(255, 255, 0))
    return image

dummy_image = create_dummy_image()

@app.route('/')
def list_packages():
    # List of all installed packages
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    installed_packages_list = '<br>'.join(sorted(installed_packages))

    # List of all actively loaded modules
    loaded_modules = set(sys.modules) & set(globals())
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
