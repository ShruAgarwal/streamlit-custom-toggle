import setuptools

setuptools.setup(
    name="streamlit-custom-toggle",
    version="0.0.1",
    author="Shruti Agarwal",
    author_email="shruagarwal01@gmail.com",
    description="A Streamlit custom component to load heart-shaped Toggle Switch",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/ShruAgarwal/streamlit-custom-toggle",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
