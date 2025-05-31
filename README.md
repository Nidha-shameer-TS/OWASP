# OWASP-SCANNER

The OWASP Vulnerability Scanner is a lightweight web-based tool designed to identify common security vulnerabilities in HTML and JavaScript code snippets based on the OWASP Top 10 security risks.his project aims to promote secure coding practices among developers and students by providing instant feedback on potential flaws such as Cross-Site Scripting (XSS), Injection attacks, Broken Access Control, Security Misconfiguration, and other critical issues. Users can paste their frontend code into the scanner, which then analyzes it using static analysis techniques, pattern matching, and open-source security libraries. The tool highlights unsafe coding patterns like the use of eval(), unsanitized inputs, open CORS policies, and hardcoded secrets. By detecting these vulnerabilities early, the scanner encourages developers to adopt more secure development habits and better understand the risks associated with insecure code. This project serves as both an educational tool and a basic security utility for small-scale applications.

## Requirements

-flask
-flask-cors
-beautifulsoup4
-lxml

# To Run the Project

## 1)Clone the Repository
## 2)Install Python requirements
pip install -r requirements.txt

## 3)Start backend
cd backend
python app.py

## 4)Start the Frontend
open index.html in a browser


# 🛡️ OWASP Vulnerability Scanner

![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Made With Python](https://img.shields.io/badge/made%20with-Python-blue)

A lightweight 🔍 web-based tool to detect common vulnerabilities in HTML and JavaScript code snippets, based on the **OWASP Top 10** security risks. This project helps developers and students identify issues like XSS, injection flaws, open CORS policies, and more — encouraging secure coding habits through real-time feedback.

---

## 🚀 Features

- ✅ Detects common OWASP Top 10 issues:
  - ❌ Cross-Site Scripting (XSS)
  - ❌ Injection attacks (e.g., `eval`, SQL patterns)
  - ❌ Open CORS policy
  - ❌ Hardcoded credentials
- 🧠 Uses static code analysis and pattern matching
- 📄 Simple HTML/JS paste-and-scan interface
- 📦 Built with Python Flask & BeautifulSoup

---

## 🖼️ Demo

> Paste your frontend code and click "Scan" to get an instant security report.

![Demo GIF or Screenshot Placeholder](https://via.placeholder.com/800x400?text=Project+Demo+Screenshot)

---

## 📦 Requirements

Install the following dependencies before running:

```bash
pip install flask flask-cors beautifulsoup4 lxml

