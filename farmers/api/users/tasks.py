from .emails import send_welcome_email,send_password_reset_token

from celery.decorators import task
from celery.utils.log import get_task_logger
from celery import app

logger = get_task_logger(__name__)

@task(name="send_confimation_email_task")
def send_confirmation_email_task(name,receiver,uid,b,token):
    """sends an email when feedback form is filled successfully"""
    logger.info("Sent feedback email")
    return send_welcome_email(name,receiver,uid,b,token)

@task(name="send_password_reset_token")
def send_password_reset_token_task(name,receiver,uid,b,token):
    logger.info("sends passwords resets token")
    return send_password_reset_token(name,receiver,uid,b,token)