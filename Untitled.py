import Scraper as sp
import pandas as pd

path='C:\Users\blaise\.wdm\drivers\chromedriver\win32\98.0.4758.80\chromedriver.exe'

df = sp.get_jobs("data scientist", 15, False,path,15)
df