from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head><title>Devops Plat</title></head>
    <body>
        <h1>Build and Deployment platform</h1>
        <p>Running on Kubernetes via k3s inside vagrant</p>
        <p>Post hostname: {}</p>
    </body>
    </html>
    '''.format(socket.gethostname())
    
@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'host': socket.gethostname()
    }), 200
    
@app.route('/info')
def info():
    return jsonify({
        'app': 'devops-platform',
        'version': '1.0.0',
        'environment': os.getenv('APP_ENV', 'development')
    }), 200
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
