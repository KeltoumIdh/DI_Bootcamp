from flask import Flask, jsonify, request
from flask_cors import CORS
from translator_module import trans

app=Flask(__name__)
CORS(app)

@app.route('/translate',methods=['GET'])
def translate_api ():
    try:
        data=request.json
        text=data['text']
        from_lang=data['from_lang']
        to_lang=data['to_lang']
        translation=trans(text,from_lang,to_lang)
        return jsonify({'translation':translation})


    except Exception as e:
        return jsonify({'error':str(e)}),500

if __name__=='__main__':
    app.run(debug=True, port=3000)