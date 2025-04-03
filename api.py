from flask import Flask,jsonify
import assemblyai  as aai
from flask_cors import CORS,cross_origin

app=Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS']='Content-Type'
aai.settings.api_key = "bf8f8c33c20146da844a964cbdfa2a66"
transcriber = aai.Transcriber()

test={}

@app.route('/')
def home():
    print("new request came")
    if 'audio_test' in test.keys():
        data={
            'transcribe': test['audio_test']
        }
        return jsonify(data)
    else:
        transcript = transcriber.transcribe("C://Users//mohitkumar//Downloads//audio_test.m4a")
    # transcript = transcriber.transcribe("./my-local-audio-file.wav")
        print(transcript.text)
        test['audio_test']=transcript.text
        data={
            'transcribe': test['audio_test']
        }
        return jsonify(data)
@app.route('/test')
def main():
    print("new request test")
    data={"check":{
        'name':'Mohit',
        'profession':'software'
    }}
    return jsonify(data)


if __name__=='__main__':
    app.run(debug=True)