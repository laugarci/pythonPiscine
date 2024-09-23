import time
from datetime import datetime

epoch_time = time.time()

print(f"Seconds since January 1, 1970: {epoch_time.4f} or {epoch_time:.2e} in scientific notation")

current_time = datetime.now()
formatted_date = current_time.strftime("%b %d %Y")

print(formatted_date)
