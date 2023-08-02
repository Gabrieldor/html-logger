import sys
import html_logger as logger

log = logger.create_new_log("output")

log.log_image("download.png", "this is a dot")
log.log_image("download4.png", "this is not a dot")
log.log_text("Info message", 'info')
log.log_text("error message", 'error')
log.log_text("critical message", 'critical')

raise Exception