from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # URL de la imagen externa que proporcionaste
    imagen_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlX7Ufu-zoF0RdTWvWAHroa4z3MCvPZbSAig43-EuDm-g57v6EWH6DYHJeOCYJScHydac&usqp=CAU"
    
    return f"""
    <div style="text-align: center;">
        <h1>Hola desde Flask con Traefik 🚀</h1>
        <img src="{imagen_url}" alt="Imagen de bienvenida" style="max-width: 300px; border-radius: 10px;">
        <p>Imagen desde URL externa</p>
    </div>
    """

@app.route('/saludo/<nombre>')
def saludo(nombre): 
    return f"<h2>Hola {nombre}, bienvenido a pgmoreno.byronrm.com</h2>"

if __name__ == '__main__':
    # debug=True ayuda a ver errores si la imagen no carga
    app.run(host='0.0.0.0', port=80, debug=True)