from setuptools import setup, find_packages

setup(
    name="chatgpt",
    version="2023.10",
    packages=find_packages(),
    install_requires=["openai"],
    entry_points={"console_scripts": ["chatgpt = chatgpt.cli:entrypoint"]},
)
