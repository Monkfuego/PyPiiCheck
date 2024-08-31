# setup.py

from setuptools import setup, find_packages

setup(
    name='gov_id_detector',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyPDF2',
        'pytesseract',
        'Pillow',
        'python-docx'
    ],
    entry_points={
        'console_scripts': [
            'gov-id-detector = gov_id_detector.__main__:main'
        ]
    }
)
