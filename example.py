import streamlit as st
from annotated_text import annotated_text, annotation


"""
# User Name Annotation
{“username”: “dumbdongshithead”, “result”: {“toxic”: 1, “exact”: 1, “details”: {“dumb d ong sh it head”: [[“inappropriate”, “dumb”]]}}

"""

annotated_text(


    "username ",
    ("dumbdongshithead", "toxic", "#FF0000"),
    " result ",
    ("toxic", "1", "#faa"),
    ("exact", "1", "#afa"),
    " details ",
    ("“dumb d ong sh it head", "inappropriate", "#fea"),
)
