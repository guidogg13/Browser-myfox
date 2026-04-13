Hi, I'm Guido, I'm 12 years old. I've always been passionate about programming, and this project is my own web browser written entirely in Python.

I built this browser using PyObjC, which allows Python to interact directly with native macOS frameworks. Thanks to this, the browser uses the same underlying WebKit engine that macOS applications rely on, giving it fast performance and excellent compatibility with modern websites.

At the moment, the browser does not support file downloads. This feature is planned and will be added in the next update. For now, the browser is mainly intended for simple and fast navigation, testing, and educational purposes.

This project is not designed for everyday browsing. Instead, it is aimed at developers, students, or anyone curious about how a minimal web browser works internally. The code is intentionally clean and easy to read, so that others can study it, modify it, or use it as a base for their own experiments.

IMPORTANT: THIS BROWSER IS ONLY COMPATIBLE WITH macOS

----------------------------------------
Installation (macOS only)

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate
pip install pyobjc

Then run the browser:

python3 browser.py
----------------------------------------

Final Notes:

It is strongly recommended to use Python version 3.14.x to ensure full compatibility with PyObjC and the latest macOS APIs.

I hope you enjoy my project. If you want to see more of my work, feel free to visit my GitHub profile and explore my other repositories. I'm always learning, experimenting, and building new things.
