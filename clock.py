from apscheduler.schedulers.blocking import BlockingScheduler
from twitterweatherscrapper import runFilesendMail
sched = BlockingScheduler()

#SETTING CLOCK TO 120 MINS (2HRS) interval, after which we send the latest data via email periodacally with a 2hr interval.
@sched.scheduled_job('interval', minutes=120)
def scheduled_job():
    runFilesendMail()
sched.start()