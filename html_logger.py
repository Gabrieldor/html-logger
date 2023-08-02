import os
from bs4 import BeautifulSoup
from datetime import datetime
import traceback
import sys

def create_new_log(log_directory):
    if not os.path.exists(log_directory):
        os.mkdir(log_directory)

    return logger(log_directory)

class logger():

    def __init__(self, log_directory):
        self.dir = log_directory
        sys.excepthook = self.handle_exception
        try:
            with open(f'{log_directory}/log.html', 'r') as f:
                self.html = BeautifulSoup(f.read(), features='lxml')
        except:
            with open(f'{log_directory}/log.html', 'w') as f:
                f.write('<body></body>')
                
        with open(f'{log_directory}/log.html', 'r') as f:
            self.html = BeautifulSoup(f.read(), features='lxml')

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        self.log_text(f"Unhandled Exception: {traceback.format_exception(exc_type, exc_value, exc_traceback)}", "critical")

    def save_html(self):
        with open(f'{self.dir}/log.html', 'wb') as f:
            f.write(self.html.prettify("utf-8"))

    def log_image(self, img_path, txt):
        time = datetime.now().replace(microsecond=0)
        div = self.html.new_tag("div")

        span_div = self.html.new_tag("div")
        span = self.html.new_tag("span")
        span.string = f"{time} [INFO]: {txt}"
        span_div.append(span)

        div.append(span_div)
        div.append(self.html.new_tag("img"))
        if os.path.exists(f"{self.dir}/{img_path}"):
            div.img["src"] = img_path
        else:
            self.log_text("The image doesnt exist", 'error')
            return
        self.html.body.append(div)
        self.save_html()

    def log_text(self, txt, lvl):
        time = datetime.now().replace(microsecond=0)
        div = self.html.new_tag("div")

        span_div = self.html.new_tag("div")
        span = self.html.new_tag("span")
        span.string = f"{time} [{lvl.upper()}]: {txt}"
        span_div.append(span)

        div.append(span_div)
        self.html.body.append(div)
        self.save_html()




