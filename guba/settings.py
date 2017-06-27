# -*- coding: utf-8 -*-

# Scrapy settings for guba project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'guba'

SPIDER_MODULES = ['guba.spiders']
NEWSPIDER_MODULE = 'guba.spiders'

ITEM_PIPELINES = {
	'guba.pipelines.GubaPipeline':300
	}

# SCHEDULER = 'guba.scrapy_redis.scheduler.Scheduler'
# SCHEDULER_PERSIST = True
# SCHEDULER_PERSIST = False
# SCHEDULER_QUEUE_CLASS = 'guba.scrapy_redis.queue.SpiderPriorityQueue'

# REDIS_HOST = '192.168.1.108'
# REDIS_PORT = 6379
# MONGO_SERVER = '192.168.1.108'
# MONGO_DB = 'guba_data'
# MONGO_PORT = '27017'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'guba (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
	'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware':None,
	'guba.spiders.poll_useragent.PollUserAgentMiddleware':400
}
