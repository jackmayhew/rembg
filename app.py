from flask import Flask, request, jsonify, send_file
from rembg import remove
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins=["http://localhost:3000", "https://lostpaws.netlify.app"])

@app.route('/')
def home():
    return "hello"

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'}), 200

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['image']
    input_image = file.read()

    output_image = remove(input_image)

    return send_file(BytesIO(output_image), mimetype='image/png', as_attachment=True, download_name='output.png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)