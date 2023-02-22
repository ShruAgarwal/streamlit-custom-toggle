from os.path import dirname
from os.path import join
import setuptools

def readme() -> str:
    
    """Utility function to read the README file.
    Used for the long_description.
    :return: content of README.md
    """
    
    return open(join(dirname(__file__), "README.md")).read()

setuptools.setup(
    name="streamlit-custom-toggle",
    version="0.1.1",
    author="Shruti Agarwal",
    author_email="shruagarwal01@gmail.com",
    description="A Streamlit custom component to load heart-shaped Toggle Switch",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ShruAgarwal/streamlit-custom-toggle",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
