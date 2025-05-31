import re

def scan_html_js(code):
    issues = []

    # === 1. XSS ===
    if re.search(r'innerHTML\s*=', code):
        issues.append({
            "type": "Cross-Site Scripting (XSS)",
            "severity": "High",
            "code": "innerHTML usage",
            "suggestion": "Use textContent or sanitize user input"
        })

    if re.search(r'document\.write\s*\(', code):
        issues.append({
            "type": "XSS via document.write",
            "severity": "Medium",
            "code": "document.write()",
            "suggestion": "Avoid document.write()"
        })

    # === 2. Dangerous JS functions ===
    if re.search(r'eval\s*\(', code):
        issues.append({
            "type": "Code Injection - eval()",
            "severity": "High",
            "code": "eval()",
            "suggestion": "Avoid using eval(), use safer alternatives"
        })

    if re.search(r'Function\s*\(', code):
        issues.append({
            "type": "Code Injection - Function Constructor",
            "severity": "High",
            "code": "Function() constructor",
            "suggestion": "Avoid Function constructor for dynamic code"
        })

    # === 3. CORS Misconfig (client) ===
    if re.search(r'Access-Control-Allow-Origin:\s*\*', code):
        issues.append({
            "type": "CORS Misconfiguration",
            "severity": "High",
            "code": "Access-Control-Allow-Origin: *",
            "suggestion": "Never allow wildcard origin in production"
        })

    # === 4. Insecure Design ===
    if re.search(r'(apiKey|token|secret)\s*=\s*[\'"].+[\'"]', code):
        issues.append({
            "type": "Hardcoded Secret",
            "severity": "Critical",
            "suggestion": "Do not store API keys or secrets in client-side code"
        })

    # === 5. Console Logs in Prod ===
    if re.search(r'console\.log\s*\(', code) or re.search(r'debugger;', code):
        issues.append({
            "type": "Debug Statements",
            "severity": "Low",
            "suggestion": "Remove console.log or debugger from production code"
        })

    return issues
