from .emails import send_issue_tracking

from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@task(name="send_issue_tracking_task")
def send_issue_tracking_task(name,receiver):
    """sends an email when contact form is filled successfully"""
    logger.info("Sent feedback email")
    return send_issue_tracking(name,receiver)