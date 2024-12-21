from flask import Flask, request, jsonify, send_file
from rembg import remove
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    return "ok"

# Hello Route
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'}), 200

# Background Removal Route
@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['image']
    input_image = file.read()

    # Remove the background
    output_image = remove(input_image)

    # Return the image
    return send_file(BytesIO(output_image), mimetype='image/png', as_attachment=True, download_name='output.png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

