
from setuptools import setup, find_packages

setup(
    name='etranslate',
    version='0.1.0',
    description='etranslate is a free and unlimited python library for translate your texts',
    long_description=open('README.md').read() + '\n\n' +open('CHANGELOG.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/ixabolfazl/etranslate',
    author='Abolfazl Khalili',
    author_email='kabolfazl39@gmail.com.org',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    keywords='translate',
    packages=find_packages(),
    install_requires=['requests'],
    python_requires=">=3.7",
)
