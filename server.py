# -*- coding: utf-8 -*-
"""
Wrapper for PyICU word segmentation
https://github.com/ovalhub/pyicu/blob/master/samples/break.py
https://github.com/danhhong/khmer_segment/blob/main/khmer_segment_icu.py
"""
import re
from typing import List

from waitress import serve
from icu import BreakIterator, Locale 
from flask import Flask, request, jsonify

app = Flask(__name__)

def gen_khm_words(text: str) -> str:
    bi = BreakIterator.createWordInstance(Locale("km"))
    bi.setText(text)
    start = bi.first()
    for end in bi:
        yield text[start:end]
        start = end

def insert_word_break(text: str) -> str:
    values = list(gen_khm_words(text))
    return '\u200b'.join(values)

def khm_segment(text: str) -> List[str]:
    if not text or not isinstance(text, str):
        return []
        
    text = text.replace('\u200b', '');
    content = text

    # detect Khmer words only
    pattern = re.compile(r'[\u1780-\u17FF]+')
    for m in re.finditer(pattern, text):
        value = m.group(0)
        content = content.replace(value, insert_word_break(value), 1)
    
    return content

@app.route("/", methods = ['post'])
def index():
    data = request.json['data']
    return {'data': khm_segment(data) }

serve(app, port=5000)
