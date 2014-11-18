from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('pypi:pybuilder_header_plugin')
use_plugin("exec")

url = 'https://github.com/labase/carinhas'
description = "Please visit {url}".format(url=url)
authors = [Author('Carlo Oliveira', 'carlo@ufrj.br')]
license = 'GNU General Public License v2 (GPLv2)'
summary = "A game of matching faces."
version = '0.1.1'
default_task = ['analyze', 'check_source_file_headers', 'publish']
analyze_command = "mv src/main/python/_init__.py src/main/python/__init__.py"

@init
def initialize(project):
    project.set_property('distutils_classifiers', [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Bottle',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: Portuguese (Brazilian)',
        'Topic :: Games/Entertainment :: Puzzle Games',
        'Topic :: Education',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'])
    header = open('header.py').read()
    project.set_property('pybuilder_header_plugin_expected_header', header)
    project.set_property('pybuilder_header_plugin_break_build', True)
