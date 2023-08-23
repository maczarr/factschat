import itertools
import os
import glob
from langchain.document_loaders import TextLoader, PyPDFLoader, UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pickle
# import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from constants import DB_FOLDER, CONTENT_FOLDER, URLS_FILENAME, CONTENT_FILE_TYPES

def load_from_urls(urls_file):
    with open(urls_file, "r") as file:
        urls = [line.strip() for line in file.readlines()]

    if (len(urls) > 0):
        loader = UnstructuredURLLoader(urls=urls)
        return loader.load()
    else:
        print(f"There are no URLs in {urls_file}")
        exit

def load_document(file_path):
    if file_path.endswith(".txt"):
        loader = TextLoader(file_path, encoding="utf-8")
    
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)

    return loader.load()

def load_documents_from_folder(content_folder):
    file_paths = []

    for ext in CONTENT_FILE_TYPES:
        search_pattern = f"{content_folder}/*.{ext}"
        files = glob.glob(search_pattern)
        [file_paths.append(file) for file in files]

    return [load_document(file_path) for file_path in file_paths]

def flatten_list(list_multi_dimensions):
    return list(itertools.chain.from_iterable(list_multi_dimensions))

def main():
    print(f"1. Read content of all URLs in {URLS_FILENAME} (one URL per line)")
    print(f"2. Read content from all files in folder {CONTENT_FOLDER} (txt and pdf supported)")
    source_choice = input("Choose a method for data retrieval: ")
    source = int(source_choice)

    if source == 1:
        data = load_from_urls(URLS_FILENAME)
    elif source == 2:
        data = flatten_list(load_documents_from_folder(CONTENT_FOLDER))

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200)

    docs = text_splitter.split_documents(data)

    embeddings = OpenAIEmbeddings()

    vectorStore_openAI = FAISS.from_documents(docs, embeddings)

    db_file_name = input("Enter a name for the database: ")
    if db_file_name == "":
        exit

    fullpath = os.path.join(DB_FOLDER, f"{db_file_name}.pkl")

    with open(fullpath, "wb") as file:
        pickle.dump(vectorStore_openAI, file)

if __name__ == "__main__":
    main()
