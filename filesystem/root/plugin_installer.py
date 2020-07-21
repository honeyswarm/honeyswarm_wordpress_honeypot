import os
import re
import sys
import requests


base_url = "http://127.0.0.1:8080"
auth_url = "{0}/wp-login.php".format(base_url)
upload_url = "{0}/wp-admin/update.php?action=upload-plugin".format(base_url)
install_url = "{0}/wp-admin/plugin-install.php?tab=upload".format(base_url)
username = "admin"
password = "password123"

headers = {
    'Accept-Encoding' : 'none',
    'Cookie':'wordpress_test_cookie=WP Cookie check'
}

auth_form = {
    "log": username,
    "pwd": password,
    "wp-submit": "Log In",
    "redirect_to": install_url,
    "testcookie": 1,
    "rememberme": "forever"

}

def upload_plugin(plugin_filename, wp_nonce):
    plugin_path = os.path.join("plugins", plugin_filename)
    files = {
        'pluginzip': (plugin_filename, open(plugin_path, 'rb')),
        '_wpnonce': (None, wp_nonce),
        '_wp_http_referer': (None, base_url + '/wp-admin/plugin-install.php?tab=upload'),
        'install-plugin-submit': (None,'Install Now')
             }

    upload_response = session.post(upload_url, files=files)
    if upload_response.status_code == 200:
        print("Uploaded plugin")
    else:
        print("Upload Failed {0}".format(upload_response.status_code))
        return False

    if "<p>Plugin installation failed.</p>" in upload_response.text:
        print("Error: Install failed for {0}".format(plugin_filename))
        return False

    if "<p>Plugin installed successfully.</p>" in upload_response.text:
        print("Success: Installed {0}".format(plugin_filename))

    
    # Get the activation link
    activate_pattern = 'href="plugins.php(.*?)"'
    try:
        activate_link = re.search(activate_pattern, upload_response.text).group(1)
    except:
        print("Could not find activation link")

    activate_url = '{0}/wp-admin/plugins.php{1}'.format(base_url, activate_link)

    # Find a better way of decoding this or split out the params
    activate_url = activate_url.replace("&amp;", "&")
    activate_url = activate_url.replace("%2f", "/")

    activate_response = session.get(activate_url)
    if "<p>Plugin activated.</p>" in activate_response.text:
        print("Plugin {0} Activated".format(plugin_filename))

        return True
    else:
        return False


# Setup the session and log in go straight tp plugin upload page
auth_success = False 
session = requests.session()
auth_request = session.post(auth_url, headers=headers, data=auth_form)

# Check for valid auth : presence of a nonce _wpnonce - b9a51ad7d7
nonce_pattern = 'name="_wpnonce" value="(.*?)"'
wp_nonce = None

try:
    wp_nonce = re.search(nonce_pattern, auth_request.text).group(1)
    auth_success = True
except:
    print("Unable to find Nonce are we correctly authenticated>")
    auth_success = False

for filename in os.listdir('plugins'):
    print("Uploading {0}".format(filename))
    upload_plugin(filename, wp_nonce)