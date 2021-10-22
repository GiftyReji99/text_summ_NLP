from __future__ import unicode_literals
from flask import Blueprint, render_template, request, jsonify, json
from flask.helpers import flash
import json

from .models import spacy_summ, lex_summ, gen_summ, nltk_summ #, bart_summ, bert_summ, gpt2_summ
import spacy
nlp = spacy.load('en_core_web_sm')

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Fetch Text From Url
def get_text(url):
	page = urlopen(url)
	soup = BeautifulSoup(page, features="lxml")
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	return fetched_text

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route('/txt_summarize',methods=['GET','POST'])
def txt_summarize():
    if request.method == 'POST':
        rawtext = request.form['tt_txt']
        if rawtext == '':
            return render_template('home.html')
        else:
            spacy_final_summary = spacy_summ(rawtext)
        
            # LexRank Summarizer
            lex_final_summary = lex_summ(rawtext)

            # Gensim Summarization
            gensim_final_summary = gen_summ(rawtext)

            # NLTK Summarization
            nltk_final_summary = nltk_summ(rawtext)

        '''# Bart Summarizer
        bart_final_summary = bart_summ(rawtext)

        # Bert Summarizer
        bert_final_summary = bert_summ(rawtext)

        # GPT-2 Summarizer
        gpt2_final_summary = gpt2_summ(rawtext)'''
        
    return render_template('home.html', ctext = rawtext, 
    spacy_final_summary = spacy_final_summary, 
    lex_final_summary = lex_final_summary,
    gensim_final_summary = gensim_final_summary,
    nltk_final_summary = nltk_final_summary)


@views.route('/lnk_summarize',methods=['GET','POST'])
def lnk_summarize():
    if request.method == 'POST':
        raw_url = request.form['tt_lnk']
        rawtext = get_text(raw_url)
        if raw_url == '':
            return render_template('home.html')
        else:
            # Spacy Summarizer
            spacy_final_summary = spacy_summ(rawtext)
        
            # LexRank Summarizer
            lex_final_summary = lex_summ(rawtext)
        
            # Gensim Summarization
            gensim_final_summary = gen_summ(rawtext)

            # NLTK Summarization
            nltk_final_summary = nltk_summ(rawtext)
    return render_template('home.html', dtext = raw_url, 
    spacy_final_summary = spacy_final_summary, 
    lex_final_summary = lex_final_summary,
    gensim_final_summary = gensim_final_summary,
    nltk_final_summary = nltk_final_summary)


@views.route('/about')
def about():
    return render_template("about.html")