import os
import smtplib
import ssl
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


def send_password_reset_code(to_email: str, code: str, user_name: str) -> None:
    if not all([SMTP_HOST, SMTP_USER, SMTP_PASSWORD, SMTP_FROM_EMAIL]):
        raise RuntimeError("Configuracion SMTP incompleta")

    recipient = DEVELOPMENT_EMAIL_OVERRIDE if DEVELOPMENT_EMAIL_OVERRIDE else to_email

    message = EmailMessage()
    message["Subject"] = "Codigo de recuperacion de contrasena - NuevaSchool"
    message["From"] = f"{SMTP_FROM_NAME} <{SMTP_FROM_EMAIL}>"
    message["To"] = recipient

    message.set_content(
        f"Hola {user_name},\n\n"
        f"Tu codigo de recuperacion es: {code}\n\n"
        f"Este codigo vence en {RESET_CODE_EXPIRE_MINUTES} minutos. "
        "Si no solicitaste este cambio, ignora este correo.\n\n"
        "Soporte de Nueva School"
    )

    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.starttls(context=context)
        smtp.login(SMTP_USER, SMTP_PASSWORD)
        smtp.send_message(message)
