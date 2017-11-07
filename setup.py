"""Strict safe JSON decoding to objects in Python

Inspired by Golang's json.Unmarshal
"""

from setuptools import setup

setup(
    name="json_obj",
    version="2.0.1",
    description="Safe JSON decoding to objects in Python",
    author="Emmanuel Goh",
    author_email="emmanuel.goh.7@gmail.com",
    license="MIT",
    url="https://github.com/emman27/json_obj",
    install_requires=[
        'python-dateutil'
    ]
)
