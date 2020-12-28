import scrapy
import time
from selenium import webdriver
from scrapy.http import Request
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import math

class BestbuySpider(scrapy.Spider):
   name = "bocho"
   USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) " \
                "Chrome/43.0.2357.130 Safari/537.36 "

   start_urls =[
       "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"]

   def parse(self, response):

       for x in range(0, 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
           product = response.xpath(
               "//*[@class='btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button']")
           if product:
               print("Product is Currently: Available.")
           else:
               print("Product is Out of Stock.")
