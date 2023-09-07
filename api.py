from flask import Flask, request, jsonify, session
from flask_session import Session  # Import the Session object
import sys, os

sys.path.append(r'C:\Users\Filipe\Desktop\Python\AI\SPRINT-3\consts')
os.chdir(r'C:\Users\Filipe\Desktop\Python\AI\SPRINT-3\scripts')
import constants

from langchain.document_loaders import DirectoryLoader
from langchain.indexes.vectorstore import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

app = Flask(__name__)
app.secret_key = 'system'
app.config['SESSION_TYPE'] = 'filesystem'  
Session(app)  

@app.route('/query', methods=['POST'])
def query_api():
    try:
        print("Starting API call...")  # Log
        data = request.json
        user_query = data['query']

        if 'conversation' not in session:
            print("Initializing new session...")  # Log
            session['conversation'] = []

        session['conversation'].append({"user": user_query})

        os.environ['OPENAI_API_KEY'] = constants.API_KEY

        loader = DirectoryLoader(r'C:\Users\Filipe\Desktop\Python\AI\SPRINT-3\scripts', glob='input_treino.txt')
        index = VectorstoreIndexCreator().from_loaders([loader])

        resposta = index.query(user_query, llm=ChatOpenAI())

        session['conversation'].append({"bot": resposta})

        return jsonify({'response': resposta, 'conversation': session['conversation']})

    except Exception as e:
        print("An error occurred:", e)  # Log
        return jsonify({'error': str(e)}), 500

@app.route('/reset', methods=['GET'])
def reset_session():
    print("Resetting session...")  # Log
    session.clear()
    return "Sessão reiniciada", 200



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
