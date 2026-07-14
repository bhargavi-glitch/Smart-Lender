from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model and label encoders
model = pickle.load(open("model.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    gender = request.form["Gender"]
    married = request.form["Married"]
    dependents = request.form["Dependents"]
    education = request.form["Education"]
    self_employed = request.form["Self_Employed"]
    applicant_income = float(request.form["ApplicantIncome"])
    coapplicant_income = float(request.form["CoapplicantIncome"])
    loan_amount = float(request.form["LoanAmount"])
    loan_term = float(request.form["Loan_Amount_Term"])
    credit_history = float(request.form["Credit_History"])
    property_area = request.form["Property_Area"]

    # Encode categorical values
    gender = label_encoders["Gender"].transform([gender])[0]
    married = label_encoders["Married"].transform([married])[0]
    dependents = label_encoders["Dependents"].transform([dependents])[0]
    education = label_encoders["Education"].transform([education])[0]
    self_employed = label_encoders["Self_Employed"].transform([self_employed])[0]
    property_area = label_encoders["Property_Area"].transform([property_area])[0]

    data = pd.DataFrame([[

        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area

    ]], columns=[

        "Gender",
        "Married",
        "Dependents",
        "Education",
        "Self_Employed",
        "ApplicantIncome",
        "CoapplicantIncome",
        "LoanAmount",
        "Loan_Amount_Term",
        "Credit_History",
        "Property_Area"

    ])

    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "✅ Loan Approved"
    else:
        result = "❌ Loan Not Approved"

    return render_template(
        "result.html",
        prediction=result,
        gender=request.form["Gender"],
        married=request.form["Married"],
        dependents=request.form["Dependents"],
        education=request.form["Education"],
        self_employed=request.form["Self_Employed"],
        applicant_income=request.form["ApplicantIncome"],
        coapplicant_income=request.form["CoapplicantIncome"],
        loan_amount=request.form["LoanAmount"],
        loan_term=request.form["Loan_Amount_Term"],
        credit_history=request.form["Credit_History"],
        property_area=request.form["Property_Area"]
    )



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)