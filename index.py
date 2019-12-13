from flask import Flask, render_template
import os

app = Flask(__name__)

image_folder = os.path.join('static', 'fav_movies')
app.config['UPLOAD_FOLDER'] = image_folder

@app.route('/')
def index():
    full_image = os.path.join(app.config['UPLOAD_FOLDER'], 'coverphoto_1.png' )
    return render_template('index.html', index_image = full_image)

@app.route('/movies')
def movies():
  return render_template('movies.html')

@app.route('/movies/godfather')
def godfather():
    full_image = os.path.join(app.config['UPLOAD_FOLDER'], 'godfather.jpg')
    return render_template('godfather.html', godfather = full_image)

@app.route('/movies/psycho')
def psycho():
    full_image = os.path.join(app.config['UPLOAD_FOLDER'], 'psycho.jpg')
    return render_template('psycho.html', psycho = full_image)

@app.route('/movies/irishman')
def irishman():
    full_image = os.path.join(app.config['UPLOAD_FOLDER'], 'irishman.jpg')
    return render_template('irishman.html', psycho = full_image)

@app.route('/movies/inglorious')
def inglorious():
    full_image = os.path.join(app.config['UPLOAD_FOLDER'], 'inglorious.jpg')
    return render_template('inglorious.html', inglorious = full_image)

@app.route('/movies/killbill')
def killbill():
    full_image = os.path.join(app.config['UPLOAD_FOLDER'], 'killbill.jpg')
    return render_template('killbill.html', killbill = full_image)

@app.route('/directors')
def directors():
    return render_template('directors.html')

@app.route('/directors/tarantino')
def tarantino():
    full_image = os.path.join(app.config['UPLOAD_FOLDER'], 'quentin-tarantino.jpg')
    return render_template('tarantino.html', tarantino = full_image)

@app.route('/directors/scorsese')
def scorsese():
    full_image = os.path.join(app.config['UPLOAD_FOLDER'], 'scorsese.jpg')
    return render_template('scorsese.html', scorsese = full_image)

@app.route('/directors/anderson')
def anderson():
    full_image = os.path.join(app.config['UPLOAD_FOLDER'], 'anderson.jpg')
    return render_template('anderson.html', anderson = full_image)

@app.route('/directors/lynch')
def lynch():
    full_image = os.path.join(app.config['UPLOAD_FOLDER'], 'lynch.jpg')
    return render_template('lynch.html', lynch = full_image)

@app.route('/directors/hitchcock')
def hitchcock():
   return render_template('hitchcock.html') 

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)