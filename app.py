# from flask import Flask, render_template, request

# app = Flask(__name__)

# responses = {
#     "hello": "नमस्ते! कथमस्ति भवान्?",
#     "hi": "नमस्ते! अहं संस्कृत-चैटबॉट् अस्मि।",
#     "namaste": "नमस्ते! भवतः स्वागतं अस्ति।",
#     "how are you": "अहं कुशलः अस्मि। धन्यवादः।",
#     "thank you": "धन्यवादः!",
#     "good morning": "सुप्रभातम्!"
# }


# @app.route("/", methods=["GET", "POST"])
# def home():

#     response = ""

#     if request.method == "POST":

#         message = request.form.get("message", "").lower().strip()

#         response = responses.get(
#             message,
#             "क्षम्यताम्। अहं एतत् न जानामि।"
#         )

#     return render_template(
#         "index.html",
#         response=response
#     )


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

# Sprint CI Update: Improved Sanskrit chatbot response handling

from flask import Flask, render_template, request

app = Flask(__name__)


# ==========================================
# SANSKRIT RESPONSES + PRONUNCIATION
# ==========================================

responses = {

    "hello": {
        "sanskrit": "नमस्ते! कथमस्ति भवान्?",
        "pronunciation": "Namaste! Kathamasti Bhavaan?"
    },

    "hi": {
        "sanskrit": "नमस्ते! अहं संस्कृत-चैटबॉट् अस्मि।",
        "pronunciation": "Namaste! Aham Sanskrit Chatbot Asmi."
    },

    "namaste": {
        "sanskrit": "नमस्ते!",
        "pronunciation": "Namaste!"
    },

    "how are you": {
        "sanskrit": "अहं कुशलः अस्मि। धन्यवादः।",
        "pronunciation": "Aham Kushalah Asmi. Dhanyavaadah."
    },

    "thank you": {
        "sanskrit": "धन्यवादः!",
        "pronunciation": "Dhanyavaadah!"
    },

    "good morning": {
        "sanskrit": "सुप्रभातम्!",
        "pronunciation": "Suprabhaatam!"
    },

    "good evening": {
        "sanskrit": "शुभसन्ध्या!",
        "pronunciation": "Shubha Sandhyaa!"
    },

    "good night": {
        "sanskrit": "शुभरात्रिः!",
        "pronunciation": "Shubharaatrih!"
    },

    "welcome": {
        "sanskrit": "स्वागतम्!",
        "pronunciation": "Svaagatam!"
    },

    "what is your name": {
        "sanskrit": "मम नाम संस्कृत-चैटबॉट् अस्ति।",
        "pronunciation": "Mama Naama Sanskrit Chatbot Asti."
    },

    "who are you": {
        "sanskrit": "अहं संस्कृत-चैटबॉट् अस्मि।",
        "pronunciation": "Aham Sanskrit Chatbot Asmi."
    },

    "bye": {
        "sanskrit": "पुनर्मिलामः!",
        "pronunciation": "Punarmilaamah!"
    },

    "goodbye": {
        "sanskrit": "पुनर्मिलामः!",
        "pronunciation": "Punarmilaamah!"
    }

}


# ==========================================
# HOME
# ==========================================

@app.route("/", methods=["GET", "POST"])
def home():

    response = None
    pronunciation = None
    user_message = ""

    if request.method == "POST":

        user_message = request.form.get(
            "message",
            ""
        ).lower().strip()

        result = responses.get(user_message)

        if result:

            response = result["sanskrit"]
            pronunciation = result["pronunciation"]

        else:

            response = "क्षम्यताम्। अहं एतत् न जानामि।"

            pronunciation = (
                "Kshamyataam. Aham Etat Na Janaami."
            )

    return render_template(
        "index.html",
        response=response,
        pronunciation=pronunciation,
        user_message=user_message
    )


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )