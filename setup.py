from setuptools import setup

setup(
    name='lsub',
    version='dev',

    url='https://github.com/lordkrandel/lsub',
    author='Lordkrandel',
    author_email='lordkrandel@gmail.com',

    py_modules=['lsub'],
    options={"bdist_wheel": {"universal": True}}
)
