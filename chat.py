import os
import pickle
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chat_models import ChatOpenAI
from custom_prompt import QUESTION_PROMPT
from constants import DB_FOLDER, MODEL, TEMPERATURE

def main():
    files = os.listdir(DB_FOLDER)
    db_files = [file for file in files if file.endswith('.pkl')]

    if (len(db_files) == 0):
        print("No database yet, create one with create_embeddings.py")
    else:
        print("Choose a database:")

        for i, file in enumerate(db_files):
            print(f"{i+1}. {file}")

        file_choice = input("Enter the number of the database to use: ")
        file_index = int(file_choice) - 1

        if file_index < 0 or file_index >= len(db_files):
            print("invalid input")
        else:
            selected_file = db_files[file_index]
            fullpath = os.path.join(DB_FOLDER, selected_file)

            with open(fullpath, "rb") as file:
                VectorStore = pickle.load(file)

            llm = ChatOpenAI(temperature=TEMPERATURE, model_name=MODEL)

            chain = RetrievalQAWithSourcesChain.from_llm(
                llm=llm,
                retriever=VectorStore.as_retriever(),
                question_prompt=QUESTION_PROMPT
            )

            while True:
                query = input("\nYou're question: ")
                if query in ["exit", "bye"]:
                    break
                
                response = chain(
                    {"question": query},
                    return_only_outputs=True,
                    include_run_info=True
                )

                print("\n> Answer:")
                print(response["answer"])

                print("\n> Source(s):")
                for source in response["sources"].split(", "):
                    print("- " + source)

if __name__ == "__main__":
    main()