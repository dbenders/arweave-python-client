from distutils.core import setup

setup(
  name="arweave-python-client",
  packages = ['arweave'], # this must be the same as the name above
  version="1.0.15.pangea",
  description="Client interface for sending transactions on the Arweave permaweb",
  author="Mike Hibbert",
  author_email="mike@hibbertitsolutions.co.uk",
  url="https://github.com/MikeHibbert/arweave-python-client",
  download_url="https://github.com/MikeHibbert/arweave-python-client",
  keywords=['arweave', 'crypto'],
  package_data={'arweave': ['testnet_jwk_file.json']},
  include_package_data=True,
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  install_requires=[
    'arrow',
    'python-jose',
    'pynacl',
    'pycryptodome',
    'cryptography',
    'requests',
    'psutil'
  ],
)
