def CreateWebviewApp(appurl, appname):
    import subprocess
    import sys

    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    try:
        import webview

    except ModuleNotFoundError:
        print("Installing Webview on your PC ;)")
        install("pywebview")
    if appurl != "" and appname != "":
        fp = open(appname + '.py', 'w')
        fp.write('import webview\nwebview.create_window("' + appname + '", "' + appurl + '")\nwebview.start()\nprint("Your app is now running!")')
        fp.close()
    else:
        print("Please enter a URL and a name for your app")

appName = input("Name of your app: ")
appUrl = input("URL of your app: ")
CreateWebviewApp(appUrl, appName)