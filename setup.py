import setuptools
import find_packages

setuptools.setup(
    name="TGbit",
    version="0.1.0",
    author="werz",
    author_email="moussarabie40@gmail.com",
    description="A skeleton Telegram shop bot for a testnet Bitcoin node.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/0xWerz/TGbit",
    packages=find_packages(),
    install_requires=["block-io",
                      "telebot",
                      "requests"
                      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "TGbit=TGbit.main:main"
        ]
    },
    project_urls={
        "Bug Tracker": "https://github.com/0xWerz/TGbit/issues",
        "Documentation": "https://github.com/0xWerz/TGbit/blob/main/README.md",
        "Source Code": "https://github.com/0xWerz/TGbit",
    }
)
