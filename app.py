from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
import io
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    if 'imagen' not in request.files:
        return "No se subió ninguna imagen"

    archivo = request.files['imagen']
    input_data = archivo.read()
    output_data = remove(input_data)
    output_image = Image.open(io.BytesIO(output_data))

    buffer = io.BytesIO()
    output_image.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='sin_fondo.png')

if __name__ == '__main__':
    app.run(debug=True)
