import multiprocessing

max_requests = 1000
max_requests_jitter = 50

log_file = "/Users/terry-brooksjr/Documents/GitHub/NettHandsHomecare/tmp/gunicorn.log"

workers = multiprocessing.cpu_count() * 2 + 1
