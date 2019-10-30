from flask import Flask , render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def hola():
   return "Hola dinosaurios del PLUG..." 

@app.route('/ex')
def ex():
    with open("vi.txt","r") as f:
        content = f.read()
    return  render_template('tem.html', content=content)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port='8081', debug=False)
