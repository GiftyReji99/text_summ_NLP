This is a WebApp for Text Summarization Using Python Flask.
It has two sections: one for Summarizing Text and another for the Text from URL.
It gives summary on the Text using different NLP models such as NLTK, Spacy, Gensim and LexRank.

Following are the Steps you need to follow before running the website.
1. Download and Install Visual Studio Code
https://code.visualstudio.com/

2. Check Python version on Windows Terminal using
  python --version
OR else Download and Install Python 3.8.10 
https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe
(Note: If you have an earlier version, its alright
but if you have 3.9 or 3.10, the gensim model will not work and will cause error)

3. Download or clone the github repository and open it on Visual Studio Code.

4. download the packages from requirements.txt using "pip install -r requirements.txt".
(It is better if you download these packages on a python virtual environment within the folder.
  for creating a virtual environment, open command prompt on this folder and
  a. pip install virtualenv
  b. virtualenv <env_name>
  c. env_name\Scripts\activate.bat) 
6. Run the main.py file and then go to http://127.0.0.1:5000/
