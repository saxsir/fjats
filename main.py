"""
Fetch the top 525 sites in Japan from alexa.com.

Note: The top sites lists are ordered by their 1 month alexa traffic.
    See http://www.alexa.com/topsites.
"""
import csv
from pyquery import PyQuery as pq
from datetime import datetime as dt

ranks = []
for i in range(21):
  # http://www.alexa.com/topsites/countries;0/JP
  url = 'http://www.alexa.com/topsites/countries;%s/JP' % i
  doc = pq(url, parser='html')
  ul = [doc(li) for li in doc('.site-listing')]
  ranks += [(li('.count').text(), li('.desc-paragraph')('a').text()) for li in ul]
  print('Fetch %s' % url)    # Check script is running

with open('topsites-jp_%s.csv' % dt.now().strftime('%y-%m-%d-%H-%M'), 'w') as f:
  writer = csv.writer(f, lineterminator='\n')
  writer.writerow(('Ranking', 'URL'))
  writer.writerows(ranks)
