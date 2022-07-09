from setuptools import setup

setup(
    name='sub',
    version='dev',

    url='https://github.com/lordkrandel/sub',
    author='Lordkrandel',
    author_email='lordkrandel@gmail.com',

    py_modules=['sub'],
    options={"bdist_wheel": {"universal": True}}
)
