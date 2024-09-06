from src._shared.errors.bad_request import BadRequestError
from src._shared.services.email_service_interface import EmailServiceInterface
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailService(EmailServiceInterface):

    def __init__(self):
        self.__email = 'mrplatoplatform@gmail.com'
        self.__senha = 'eull xgig yyni uhgp '
        self.__servidor_smtp = 'smtp.gmail.com'
        self.__porta_smtp = 587

    def send(self, to, subject, content):
        msg = MIMEMultipart()
        msg['From'] = self.__email
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(content, 'plain'))
        try:
            servidor = smtplib.SMTP(host=self.__servidor_smtp, port=self.__porta_smtp)
            servidor.starttls()
            servidor.login(self.__email, self.__senha)
            texto_email = msg.as_string()
            servidor.sendmail(self.__email, to, texto_email)
        except Exception as error:
            raise BadRequestError(message=error)
        finally:
            servidor.quit()