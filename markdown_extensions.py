"""
Preload all python-markdown extensions
"""

# By default sublime only imports python packages from the top level of the plugin directory.
# Trying to import packages from subdirectories dynamically at a later time is NOT possible.

# This package automatically imports all packages from the extension directory
# so they are available when we need them.

import sublime, os, pkgutil

packages_path = sublime.packages_path()
package_name ="Markdown Preview"
extension_module = "markdown.extensions"


for  _, package, _ in pkgutil.walk_packages("."):
	if package.startswith(extension_module):
		print "Reloading plugin extension %s" % os.path.join(packages_path, package_name, *package.split(".")) + ".py"
		__import__(package)
