sql_errors = [
    "you have an error in your sql syntax",
    "warning: mysql",
    "unclosed quotation mark",
    "quoted string not properly terminated",
    "sqlite error",
    "fatal error",
    "unexpected end of SQL command",
    "mysql_fetch",
    "ORA-00933",
    "PG::SyntaxError",
    "syntax error",
    "unterminated string"
]

def is_vulnerable(response, payload, expected=None):
    if not response:
        return None

    content = response.text.lower()

    # 1. SQL Error = SQLi
    for error in sql_errors:
        if error.lower() in content:
            return "SQLi"

    # 2. Payload reflected = might be XSS, but classify based on expected type
    if payload.lower() in content:
        return expected  # trust the payload category

    return None
