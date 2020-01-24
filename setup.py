import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='wordslicer',  
    version='0.1.3',
    #scripts=['wordslicer'] ,
    author="Pedro Moreira, Nelson Sousa",
    author_email="a82364@alunos.uminho.pt, a82053@alunos.uminho.pt",
    description="A tool to separate truncated text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bishop19/wordslicer",
    packages=['wordslicer'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )