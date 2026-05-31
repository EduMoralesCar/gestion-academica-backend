import os
import smtplib
import ssl
import urllib.request
import urllib.error
import json
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_FROM_NAME = os.getenv("SMTP_FROM_NAME", "NuevaSchool")
SMTP_FROM_EMAIL = os.getenv("SMTP_FROM_EMAIL", SMTP_USER)
RESET_CODE_EXPIRE_MINUTES = int(os.getenv("RESET_CODE_EXPIRE_MINUTES", 10))
DEVELOPMENT_EMAIL_OVERRIDE = os.getenv("DEVELOPMENT_EMAIL_OVERRIDE")

BREVO_API_KEY = os.getenv("BREVO_API_KEY")
RESEND_API_KEY = os.getenv("RESEND_API_KEY")


def send_password_reset_code(to_email: str, code: str, user_name: str) -> None:
    recipient = DEVELOPMENT_EMAIL_OVERRIDE if DEVELOPMENT_EMAIL_OVERRIDE else to_email

    subject = "Codigo de recuperacion de contrasena - NuevaSchool"
    content = (
        f"Hola {user_name},\n\n"
        f"Tu codigo de recuperacion es: {code}\n\n"
        f"Este codigo vence en {RESET_CODE_EXPIRE_MINUTES} minutos. "
        "Si no solicitaste este cambio, ignora este correo.\n\n"
        "Soporte de Nueva School"
    )

    # 1. Resend HTTP API (Puerto 443 - Nunca bloqueado en la nube)
    if RESEND_API_KEY:
        url = "https://api.resend.com/emails"
        headers = {
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        # Resend requiere enviar desde 'onboarding@resend.dev' en el plan gratuito/sandbox
        # a menos que tengas un dominio propio verificado (no se permiten correos públicos como Gmail).
        sender_email = "onboarding@resend.dev"
        if SMTP_FROM_EMAIL and "@" in SMTP_FROM_EMAIL:
            domain = SMTP_FROM_EMAIL.split("@")[-1].lower()
            if domain not in ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "live.com"]:
                sender_email = SMTP_FROM_EMAIL

        data = {
            "from": f"{SMTP_FROM_NAME} <{sender_email}>",
            "to": [recipient],
            "subject": subject,
            "text": content
        }
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(data).encode("utf-8"),
                headers=headers,
                method="POST"
            )
            with urllib.request.urlopen(req) as response:
                response.read()
        except urllib.error.HTTPError as he:
            try:
                error_body = he.read().decode("utf-8")
                print("--- RESEND API ERROR DETAILS ---")
                print(f"Status Code: {he.code}")
                print(f"Response Body: {error_body}")
            except Exception:
                pass
            raise he
        return

    # 2. Brevo (Sendinblue) HTTP API (Puerto 443 - Nunca bloqueado en la nube)
    if BREVO_API_KEY:
        url = "https://api.brevo.com/v3/smtp/email"
        headers = {
            "api-key": BREVO_API_KEY,
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        data = {
            "sender": {"name": SMTP_FROM_NAME, "email": SMTP_FROM_EMAIL},
            "to": [{"email": recipient}],
            "subject": subject,
            "textContent": content
        }
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(data).encode("utf-8"),
                headers=headers,
                method="POST"
            )
            with urllib.request.urlopen(req) as response:
                response.read()
        except urllib.error.HTTPError as he:
            try:
                error_body = he.read().decode("utf-8")
                print("--- BREVO API ERROR DETAILS ---")
                print(f"Status Code: {he.code}")
                print(f"Response Body: {error_body}")
            except Exception:
                pass
            raise he
        return

    # 3. SMTP clásico (Gmail, etc. - Funciona en local, pero suele estar bloqueado en servidores gratuitos como Render)
    if not all([SMTP_HOST, SMTP_USER, SMTP_PASSWORD, SMTP_FROM_EMAIL]):
        raise RuntimeError("Configuracion de correo (SMTP o HTTP API) incompleta")

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = f"{SMTP_FROM_NAME} <{SMTP_FROM_EMAIL}>"
    message["To"] = recipient
    message.set_content(content)

    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.starttls(context=context)
        smtp.login(SMTP_USER, SMTP_PASSWORD)
        smtp.send_message(message)

