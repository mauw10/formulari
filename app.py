from flask import Flask, request, render_template, redirect, url_for
import mail_dict

app = Flask(__name__)

@app.route("/")
def inici():
    return redirect(url_for('getmail'))

@app.route('/getmail', methods=['POST', 'GET'])
def getmail():
    correu = None
    result_msg = None
    nom = None  # Inicializar 'nom' antes del bloque if
    if request.method == 'POST':
        nom = request.form['nom']
        nom = nom.capitalize()
        correu = mail_dict.getmaildict(nom)
        if correu:
            result_msg = "El correo electrónico asociado al usuario '{}' es '{}'.".format(nom, correu)
        else:
            result_msg = "El usuario '{}' no existe.".format(nom)
    return render_template('getmail.html', nom=nom, correu=correu, result_msg=result_msg)


@app.route('/addmail', methods=['POST', 'GET'])
def addmail():
    if request.method == 'POST':
        modif = False
        nom = request.form['nom']
        nom = nom.capitalize()
        correu = request.form['correu']
        if 'modif' in request.form:
            modif = True
        result_msg = mail_dict.addmaildict(nom, correu, modif)
        return render_template('addmail.html', nom=nom, correu=correu, result_msg=result_msg)
    else:
        return render_template('addmail.html')

if __name__ == '__main__':
    app.run(debug=True)


