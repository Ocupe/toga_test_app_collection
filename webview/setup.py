#!/usr/bin/env python
import io
import re
from setuptools import setup, find_packages
import sys

with io.open('./WebView/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='WebView',
    version=version,
    description='Test the webview widget.',
    long_description=long_description,
    author='Jonas Schell',
    author_email='jonasschell@ocupe.org',
    license='MIT license',
    packages=find_packages(
        exclude=[
            'docs', 'tests',
            'windows', 'macOS', 'linux',
            'iOS', 'android',
            'django'
        ]
    ),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT license',
    ],
    install_requires=[
    ],
    options={
        'app': {
            'formal_name': 'webview',
            'bundle': 'org.pybee'
        },

        # Desktop/laptop deployments
        'macos': {
            'app_requires': [
                'toga-cocoa',
            ]
        },
        'linux': {
            'app_requires': [
                'toga-gtk',
            ]
        },
        'windows': {
            'app_requires': [
                'toga-winforms',
            ]
        },

        # Mobile deployments
        'ios': {
            'app_requires': [
                'toga-ios',
            ]
        },
        'android': {
            'app_requires': [
                'toga-android',
            ]
        },

        # Web deployments
        'django': {
            'app_requires': [
                'toga-django',
            ]
        },
    }
)
