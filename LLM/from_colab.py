# !pip install langchain
# !pip install unstructured # The unstructured library provides open-source components for pre-processing text documents such as PDFs, HTML and Word Documents.
# !pip install openai
# !pip install pybind11 # pybind11 is a lightweight header-only library that exposes C++ types in Python
# !pip install chromadb # the AI-native open-source embedding database
# # !pip install Cython # Cython is an optimising static compiler for both the Python programming language
# !pip3 install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI" # COCO is a large image dataset designed for object detection, segmentation, person keypoints detection, stuff segmentation, and caption generation
# !pip install unstructured[local-inference]
# !CC=clang CXX=clang++ ARCHFLAGS="-arch x86_64" pip install 'git+https://github.com/facebookresearch/detectron2.git' # Detectron2 is Facebook AI Research's next generation library that provides state-of-the-art detection and segmentation algorithms.
# !pip install layoutparser[layoutmodels,tesseract] # A Unified Toolkit for Deep Learning Based Document Image Analysis
# !pip install pytesseract # Python-tesseract is an optical character recognition (OCR) tool for python.
# !pip install Pillow==9.0.0 # The Python Imaging Library adds image processing capabilities to your Python interpreter. Need this version, otherwise errors occur.
# !pip install pyspark

import os
os.environ['OPENAI_API_KEY'] = 'your_api_key_here'

from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes import VectorstoreIndexCreator

from detectron2.config import get_cfg
cfg = get_cfg()
cfg.MODEL.DEVICE = 'cpu' #GPU is recommended

!wget https://s21.q4cdn.com/399680738/files/doc_financials/2022/q4/Meta-12.31.2022-Exhibit-99.1-FINAL.pdf #meta earnings; replace with any pdf

!mkdir docs
!mv Meta-12.31.2022-Exhibit-99.1-FINAL.pdf docs

text_folder = 'docs'
loaders = [UnstructuredPDFLoader(os.path.join(text_folder, fn)) for fn in os.listdir(text_folder)]

!apt-get install poppler-utils # error occurs without this, pdf rendering library

index = VectorstoreIndexCreator().from_loaders(loaders)

query = "How much revenue did Meta make in 2022?"
index.query(query)

query = "What are meta's biggest risks?"
index.query(query)