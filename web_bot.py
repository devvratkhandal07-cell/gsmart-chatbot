from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

COMPANY_INFO = """
Company: G Smart Investor LLP

Founder: Shivram Shivhare
Co-Founder: Shriman Narayan Agrawal

Services:
- Investment Consultancy
- Business Registration
- MSME Support
- Global Smart Market
- Franchise Opportunities
- Employment Programs

Franchise:
- Total Project Cost: ₹1 Crore
- Company Investment: ₹70 Lakh
- Franchise Partner Investment: ₹30 Lakh
- Profit Sharing: 60% Company, 40% Partner

Contact:
Phone: +91 98939 93488
Email: globalsmartinvestor@gmail.com
Address: Sewagram, Khajuraho, Chhatarpur, MP 471606
"""

@app.route("/")
def home():
    return "G Smart Chatbot Running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    prompt = f"""
You are the official chatbot of G Smart Investor LLP.

Use only the information below when answering.

{COMPANY_INFO}

User Question:
{user_message}
"""

    response = model.generate_content(prompt)

    return jsonify({
        "response": response.text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
