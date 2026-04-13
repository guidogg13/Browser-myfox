🌟 Hi! I'm Guido — I'm 12 years old and I've always been super passionate about programming.  
This project is one of the things I'm most proud of: **a real web browser written in Python**, built completely by me!

💻 I created this browser using **PyObjC**, a bridge that lets Python communicate directly with macOS native frameworks.  
Thanks to this, the browser uses the same underlying WebKit engine used by macOS apps, giving it fast performance, smooth rendering, and excellent compatibility with modern websites.

────────────────────────────────────────
🚀 HOW I BUILT THIS BROWSER
────────────────────────────────────────

I started with a simple idea:  
*"Can I make a real browser using Python?"*

At first, it sounded impossible. Browsers are complicated, right?  
But step by step, I discovered that macOS gives developers access to WebKit — the same engine used by many native apps — and PyObjC lets Python talk to it.

So I began experimenting:

• I created a basic window  
• I added a WebView component  
• I connected Python functions to macOS events  
• I implemented navigation buttons  
• I added URL handling  
• I improved the UI to make it cleaner and faster  

Every time qualcosa funzionava, ero felicissimo.  
Every time qualcosa NON funzionava… beh, imparavo qualcosa di nuovo 😄

This project taught me:

✨ how native macOS apps work  
✨ how Python can control system frameworks  
✨ how browsers load and render pages  
✨ how to structure a real software project  
✨ how to debug (tantissimo 😂)

────────────────────────────────────────
⚠️ IMPORTANT COMPATIBILITY NOTE
────────────────────────────────────────

❗ **THIS BROWSER IS ONLY COMPATIBLE WITH macOS**  
It will NOT run on Windows or Linux because it depends on macOS frameworks.

────────────────────────────────────────
📦 INSTALLATION (macOS only)
────────────────────────────────────────

Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
pip install pyobjc
```


Then run the browser:

```
python3 browser.py
```



────────────────────────────────────────
📌 FINAL NOTES
────────────────────────────────────────

🔧 It is strongly recommended to use **Python 3.14.x** for full compatibility.  
Older versions may not work correctly with the latest PyObjC releases.

💬 I hope you enjoy my project!  
If you want to see more of my work, feel free to visit my GitHub profile and explore my other repositories.  
I'm always learning, experimenting, and building new things — and this browser is just the beginning 🚀

Thanks for reading! 😄
