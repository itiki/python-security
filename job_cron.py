from crontab import CronTab


def main():

    cron = CronTab(user=True)
    job = cron.new(command='/home/xinali/.pyenv/shims/python /home/xinali/python/get_job.py', comment='get job')
    job.setall("*/1 * * * *")
    cron.write()

if __name__ == '__main__':
    main()
