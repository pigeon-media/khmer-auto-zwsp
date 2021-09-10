# -*- coding: utf-8 -*-
import re
from typing import List

from flask.wrappers import Response
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

def khm_segment(text: str) -> List[str]:
    if not text or not isinstance(text, str):
        return []

    text = re.sub("([^\u1780-\u17FF\n ]+)", " \\1 ", text)
    return list(gen_khm_words(text))

@app.route("/", methods = ['post'])
def hello_world():
    data = request.json['data']
    return {'data': khm_segment(data) }

if __name__ == '__main__':
  app.run(debug=False)