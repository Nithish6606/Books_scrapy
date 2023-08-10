import scrapy


class AttendenceSpider(scrapy.Spider):
    name = "attendence"
    allowed_domains = ["exams.jntuhcej.ac.in"]
    start_urls = ["https://exams.jntuhcej.ac.in/student/login"]

    def parse(self, response):
        pass
