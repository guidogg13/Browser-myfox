import objc
from Cocoa import (
    NSApplication, NSWindow, NSBackingStoreBuffered,
    NSMakeRect, NSURL, NSURLRequest,
    NSTitledWindowMask, NSClosableWindowMask,
    NSResizableWindowMask, NSMiniaturizableWindowMask,
    NSTextField, NSButton, NSView,
    NSColor
)
from WebKit import (
    WKWebView,
    WKWebViewConfiguration,
)
import AppKit


class BrowserDelegate(AppKit.NSObject):

    def initWithBrowser_(self, browser):
        self = objc.super(BrowserDelegate, self).init()
        if self is None:
            return None
        self.browser = browser
        return self

    def webView_didFinishNavigation_(self, webview, navigation):
        title = webview.title() or "EISI Browser"
        self.browser.window.setTitle_(title)
        url = webview.URL()
        if url:
            self.browser.url_field.setStringValue_(url.absoluteString())

    def webView_didFailNavigation_withError_(self, webview, navigation, error):
        print(f"Errore navigazione: {error.localizedDescription()}")

    def webView_navigationResponse_didBecomeDownload_(self, webview, response, download):
        download.setDelegate_(self)

    def download_decideDestinationUsingResponse_suggestedFilename_completionHandler_(
        self, download, response, filename, handler
    ):
        panel = AppKit.NSSavePanel.savePanel()
        panel.setNameFieldStringValue_(filename)
        result = panel.runModal()
        if result == 1:
            handler(panel.URL())
        else:
            handler(None)


class Browser:
    def __init__(self):
        self.app = NSApplication.sharedApplication()
        self.app.setActivationPolicy_(0)

        style = (
            NSTitledWindowMask |
            NSClosableWindowMask |
            NSResizableWindowMask |
            NSMiniaturizableWindowMask
        )

        self.window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            NSMakeRect(100, 100, 1200, 800),
            style,
            NSBackingStoreBuffered,
            False
        )
        self.window.setTitle_("EISI Browser")

        content = self.window.contentView()
        content_frame = content.bounds()
        W = content_frame.size.width
        H = content_frame.size.height

        # — Toolbar —
        toolbar_h = 40
        toolbar = NSView.alloc().initWithFrame_(
            NSMakeRect(0, H - toolbar_h, W, toolbar_h)
        )
        toolbar.setAutoresizingMask_(18 | 4)

        # Pulsante indietro
        self.btn_back = NSButton.alloc().initWithFrame_(NSMakeRect(8, 6, 36, 28))
        self.btn_back.setTitle_("‹")
        self.btn_back.setBezelStyle_(1)  # NSBezelStyleRounded
        self.btn_back.setTarget_(self)
        self.btn_back.setAction_(objc.selector(self.goBack_, signature=b'v@:@'))

        # Pulsante avanti
        self.btn_forward = NSButton.alloc().initWithFrame_(NSMakeRect(48, 6, 36, 28))
        self.btn_forward.setTitle_("›")
        self.btn_forward.setBezelStyle_(1)  # NSBezelStyleRounded
        self.btn_forward.setTarget_(self)
        self.btn_forward.setAction_(objc.selector(self.goForward_, signature=b'v@:@'))

        # Campo URL
        self.url_field = NSTextField.alloc().initWithFrame_(
            NSMakeRect(92, 8, W - 100, 24)
        )
        self.url_field.setAutoresizingMask_(2)
        self.url_field.setStringValue_("https://www.google.com")
        self.url_field.setTarget_(self)
        self.url_field.setAction_(objc.selector(self.loadURL_, signature=b'v@:@'))

        toolbar.addSubview_(self.btn_back)
        toolbar.addSubview_(self.btn_forward)
        toolbar.addSubview_(self.url_field)

        # — WebView —
        config = WKWebViewConfiguration.alloc().init()

        self.webview = WKWebView.alloc().initWithFrame_configuration_(
            NSMakeRect(0, 0, W, H - toolbar_h),
            config
        )
        self.webview.setAutoresizingMask_(18)

        self.delegate = BrowserDelegate.alloc().initWithBrowser_(self)
        self.webview.setNavigationDelegate_(self.delegate)

        content.addSubview_(toolbar)
        content.addSubview_(self.webview)

        url = NSURL.URLWithString_("https://www.google.com")
        self.webview.loadRequest_(NSURLRequest.requestWithURL_(url))

        self.window.makeKeyAndOrderFront_(None)
        self.app.activateIgnoringOtherApps_(True)
        self.app.run()

    def goBack_(self, sender):
        if self.webview.canGoBack():
            self.webview.goBack()

    def goForward_(self, sender):
        if self.webview.canGoForward():
            self.webview.goForward()

    def loadURL_(self, sender):
        url_str = self.url_field.stringValue()
        if not url_str.startswith("http"):
            url_str = "https://" + url_str
        url = NSURL.URLWithString_(url_str)
        self.webview.loadRequest_(NSURLRequest.requestWithURL_(url))


if __name__ == "__main__":
    Browser()