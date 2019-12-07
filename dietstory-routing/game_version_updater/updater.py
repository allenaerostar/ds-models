from apscheduler.schedulers.background import BackgroundScheduler
from .updateGameVersion import add_all_jobs


def start():
    version_update_scheduler.start()
    add_all_jobs(version_update_scheduler)


version_update_scheduler = BackgroundScheduler()
