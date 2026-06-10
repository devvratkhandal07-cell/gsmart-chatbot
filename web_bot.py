from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os

app = Flask(__name__)
CORS(app)

GROQ_API_KEY = os.getenv("GROQ_API_KEY") 
client = Groq(api_key=GROQ_API_KEY)


COMPANY_INFO = """
G Smart Investor LLP

Tagline:
Empowering Rural & Semi-Urban India

About Company:
G Smart Investor LLP is a fintech-driven consultancy and investment platform built to bridge the financial gap for India's rural communities, MSMEs, entrepreneurs, startups, women, farmers, and youth.

The company provides accessible investment models, business consultancy, MSME support, employment opportunities, and a growing franchise network called Global Smart Market.

Mission:
To contribute towards Vikshit Bharat by promoting entrepreneurship, financial inclusion, employment generation, and grassroots economic development.

Founder:
Shivram Shivhare

Co-Founder:
Shriman Narayan Agrawal

Industry:
Marketing, Consultancy, Fintech

Established:
18 December 2018

Startup Recognition Date:
15 January 2019

Registrations:

DPIIT Certified (DIPP30770)
MCA Registered
LLP No. AAN-7914

Registered Office:
Sewagram, Khajuraho, Block Rajnagar, District Chhatarpur, Madhya Pradesh – 471606

Core Services:

Business Registration
Quick and affordable business registration services for MSMEs, startups, and entrepreneurs.
Starting from ₹118.
Investment Consultancy
Professional investment guidance and financial planning services.
Starting from ₹1000 + GST.
MSME Registration & Support
Startup Guidance & Mentorship
Global Business Center
Global Smart Market
Employment Programs
Franchise Opportunities
Enterprise Development Projects
Financial Literacy Programs

Global Smart Market Franchise:

Project Cost:
₹1 Crore

Company Investment:
₹70 Lakhs

Franchise Partner Investment:
₹30 Lakhs

Profit Sharing:
60% Company
40% Franchise Partner

Expected Annual ROI:
15% to 20%

Company Responsibilities:

Store Setup
Branding
Interior Design
Supply Chain
Operations Management

Partner Responsibilities:

5000 to 8000 sq.ft Property
Local Operations Management

Revenue Streams:

Registration Fees
Consultancy Fees
Investment Programs
Referral Programs
Franchise Revenue
Enterprise Projects

Employment Goal:
1000+ Jobs

Target Market:

Rural India
Tier 2 Cities
Tier 3 Cities
MSMEs
Farmers
Entrepreneurs
Startups

Achievements:

2500+ Farmers Engaged
DPIIT Recognized Startup
MCA Registered LLP
Active Projects in Biodiversity, Natural Farming, and Women Farmer Training

Vision:
Zero Poverty, Financial Inclusion, Employment Generation, MSME Growth, Women Empowerment, and Global Market Access.

Funding Requirement:
₹1 Crore Growth Funding

Fund Allocation:
40% Business Expansion & Franchise Setup
25% Technology Development
20% Marketing & Outreach
15% Working Capital & Contingency

Contact Information:

Phone:
+91 98939 93488

Email:
globalsmartinvestor@gmail.com

Founder:
Shivram Shivhare

Address:
Sewagram, Khajuraho, Block Rajnagar, District Chhatarpur, Madhya Pradesh – 471606

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

You can answer questions about:
- Investment Consultancy
- Business Registration
- MSME Support
- Global Smart Market
- Franchise Opportunities
- Employment Programs
- Company Information

IMPORTANT RULES:

If the user asks about services, franchise, startup, MSME, funding, business registration, employment programs, company background, founder details, market opportunity, investment opportunity, vision, registrations, achievements, or contact information, provide a detailed answer using the company information.

Do not give very short answers. Explain clearly in simple language with relevant details from the company information.

1. If the user asks about franchise, partnership, investment, business enquiry, contact details, phone number, email, meeting, support, founder details, or wants more information, ALWAYS include:

📞 Phone: +91 98939 93488
📧 Email: globalsmartinvestor@gmail.com
📍 Address: Sewagram, Khajuraho, Chhatarpur, MP 471606

2. If you are unsure of any answer, politely tell the user to contact the company directly using the contact details above.

3. Keep answers professional, concise, and helpful.

Company Information:

{COMPANY_INFO}

User Question:
{user_message}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=800
        )

        return jsonify({
            "response": response.choices[0].message.content
        })

    except Exception as e:
        return jsonify({
            "response": str(e)
        })
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
