import os


def get_password() -> str:
    """Récupère le mot de passe depuis l'environnement, sans l'afficher."""
    password = os.getenv("APP_PASSWORD")
    if not password:
        raise RuntimeError("APP_PASSWORD n'est pas configuré")
    return password


def calculate(a: float, b: float, operation: str) -> float:
    """Effectue une opération parmi une liste blanche."""
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        if b == 0:
            raise ValueError("Division par zéro")
        return a / b
    raise ValueError("Opération non autorisée")
