# -*- coding: utf-8 -*-

# Scrapy settings for FinishLine project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'FinishLine'

SPIDER_MODULES = ['FinishLine.spiders']
NEWSPIDER_MODULE = 'FinishLine.spiders'
DOWNLOAD_DELAY = 2.5
