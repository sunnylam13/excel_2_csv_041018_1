try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'This program lets you convert hundreds of Excel files to CSVs, to avoid hours of clicking.',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/excel_2_csv_041018_1',
	'download_url': 'https://github.com/sunnylam13/excel_2_csv_041018_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'Excel to CSV Converter'
}

setup(**config)