# OWASP-SCANNER

The OWASP Vulnerability Scanner is a lightweight web-based tool designed to identify common security vulnerabilities in HTML and JavaScript code snippets based on the OWASP Top 10 security risks.his project aims to promote secure coding practices among developers and students by providing instant feedback on potential flaws such as Cross-Site Scripting (XSS), Injection attacks, Broken Access Control, Security Misconfiguration, and other critical issues. Users can paste their frontend code into the scanner, which then analyzes it using static analysis techniques, pattern matching, and open-source security libraries. The tool highlights unsafe coding patterns like the use of eval(), unsanitized inputs, open CORS policies, and hardcoded secrets. By detecting these vulnerabilities early, the scanner encourages developers to adopt more secure development habits and better understand the risks associated with insecure code. This project serves as both an educational tool and a basic security utility for small-scale applications.

## Requirements

-flask
-flask-cors
-beautifulsoup4
-lxml

## To Run the Project

#  Clone the Repository
# Install Python requirements
pip install -r requirements.txt

# Start backend
cd backend
python app.py

# Start the Frontend
open index.html in a browser

