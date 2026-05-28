"""Code validation utilities for snippet generator."""
import ast
from typing import Optional


def validate_python_syntax(code: str) -> tuple[bool, Optional[str]]:
    """Validate Python code syntax.
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, f"Syntax error at line {e.lineno}: {e.msg}"


def validate_javascript_syntax(code: str) -> tuple[bool, Optional[str]]:
    """Basic JavaScript syntax validation.
    
    Note: This is a basic check. For full validation, consider using
    a proper JS parser like 'esprima' or 'acorn'.
    """
    # Basic checks for common issues
    open_braces = code.count("{") - code.count("}")
    open_parens = code.count("(") - code.count(")")
    open_brackets = code.count("[") - code.count("]")
    
    if open_braces != 0:
        return False, f"Mismatched braces: {open_braces} unclosed"
    if open_parens != 0:
        return False, f"Mismatched parentheses: {open_parens} unclosed"
    if open_brackets != 0:
        return False, f"Mismatched brackets: {open_brackets} unclosed"
    
    return True, None


def validate_code(code: str, language: str) -> tuple[bool, Optional[str]]:
    """Validate code based on language.
    
    Args:
        code: The code to validate
        language: Programming language name
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    validators = {
        "python": validate_python_syntax,
        "javascript": validate_javascript_syntax,
    }
    
    validator = validators.get(language.lower())
    if validator:
        return validator(code)
    
    # No validator available, assume valid
    return True, None
