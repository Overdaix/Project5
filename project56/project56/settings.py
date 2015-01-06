# -*- coding: utf-8 -*-

# Scrapy settings for project56 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'project56'

SPIDER_MODULES = ['project56.spiders']
NEWSPIDER_MODULE = 'project56.spiders'

ITEM_PIPELINES = ['project56.pipelines.MongoDBPipeline']
MONGODB_HOST = 'ds057000.mongolab.com'
MONGODB_PORT = 57000
MONGODB_DATABASE = 'db_pcmaster'
MONGODB_COLLECTION = 'c_part'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'project56 (+http://www.yourdomain.com)'
