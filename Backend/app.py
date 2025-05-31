from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # Allow frontend to access this API

@app.route("/scan", methods=["POST"])
def scan_code():
    data = request.get_json()
    code = data.get("code", "")
    issues = []

    # Rule 1: XSS - innerHTML
    matches = list(re.finditer(r'\.innerHTML\s*=\s*', code))
    for match in matches:
        issues.append({
            "type": "Cross-Site Scripting (XSS)",
            "severity": "High",
            "code": get_code_line(code, match.start()),
            "suggestion": "Use textContent or sanitize input"
        })

    # Rule 2: JS Injection - eval()
    matches = list(re.finditer(r'eval\s*\(', code))
    for match in matches:
        issues.append({
            "type": "JS Injection - eval()",
            "severity": "High",
            "code": get_code_line(code, match.start()),
            "suggestion": "Avoid using eval(). Use JSON.parse or safe alternatives."
        })

    # Rule 3: Debug statements
    if 'console.log' in code or 'debugger' in code:
        issues.append({
            "type": "Debug Statements in Production",
            "severity": "Medium",
            "code": "console.log/debugger found",
            "suggestion": "Remove debug logs before deploying to production."
        })

    # Rule 4: Hardcoded tokens
    matches = list(re.finditer(r'(token|apiKey)\s*=\s*[\'"]', code, re.IGNORECASE))
    for match in matches:
        issues.append({
            "type": "Hardcoded Credentials",
            "severity": "High",
            "code": get_code_line(code, match.start()),
            "suggestion": "Store secrets in environment variables, not code."
        })

    return jsonify(issues)

def get_code_line(code, index):
    """Return the line of code where the issue was found."""
    lines = code.splitlines()
    char_count = 0
    for line in lines:
        if char_count + len(line) >= index:
            return line.strip()
        char_count += len(line) + 1
    return ""
    
if __name__ == "__main__":
    app.run(debug=True)
