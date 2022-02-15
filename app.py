import joblib
from flask import Flask, request, jsonify, render_template

MODEL_PATH = "model.joblib"

app = Flask(__name__)

@app.route("/") #c'est la racine de notre site internet 
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"]) #on crée une nouvelle route un nouveau pt d'accès qui va exécuter la fonction qu'on va décrire ci_dessous
# cette route doit s'appeler predict et on va utiliser la méthode post qui va me permettre de récupérer un json

def predict():
    # on vérifie si on a un json si oui on entre dans cette condition 
    if request.json:
        # je récupère un dictionnaire avec un certain input à l'intérieur
        json_input = request.get_json()
        # Check mandatory key
        if "input" in json_input.keys():
            # je vais charger mon modèle avec le chemin décrit ci_dessus
            classifier = joblib.load(MODEL_PATH)
            # une fois que j'ai mon modèle je vais faire ma prédiction  
            prediction = classifier.predict(json_input["input"]) #ça me renvoie une liste 
            # Return the result as JSON but first we need to transform the
            # result so as to be serializable by jsonify()
            prediction = prediction.tolist()
            # # Je mets la prédiction dans un dictionnaire 
            response = {
                "prediction": prediction,
            }
            return jsonify(response), 200 # je vais transformer ce dictionnaire en json et je vais le renvoyer à l'utilisateur
    return jsonify({"msg": "Error: not a JSON or no 'input' key in your request"})# l'utilisateur a fait une méthode post 
    # mais il n'a pas mis du json on lui met un message d'erreur 


if __name__ == "__main__":
    app.run(debug=True, port=5002)

