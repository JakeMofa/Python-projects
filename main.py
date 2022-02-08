#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#




import wsgiref.handlers
import ystockquote
import urllib



from google.appengine.ext import webapp


class MainHandler(webapp.RequestHandler):

  def get(self):
    queryStr = self.request.get('q', default_value='')
    first = 0
    
    
    if queryStr != '': 
       symbols = queryStr.split(' ')
             
       body = '[' 
          
       quotes = []
    
       for symbol in symbols:
            try:
             price = ystockquote.get_price(symbol)
             change = ystockquote.get_change(symbol)
             volume = ystockquote.get_volume(symbol)
             avg_daily_volume = ystockquote.get_avg_daily_volume(symbol)
             stock_exchange = ystockquote.get_stock_exchange(symbol) 
             name = ystockquote.get_name(symbol)  
             if len(price) > 0:                   
                quotes.append(('{"symbol":"%s","name":"%s","price":%f,"change":%f,"volume":%f,"avg_daily_volume":%f,"stock_exchange":"%s"}' % (symbol, name, float(price), float(change), float(volume),float(avg_daily_volume),stock_exchange)))
                if first == 1:
                   body += "," 
                body += ','.join(quotes)
                first = 1
             quotes = []
            except:
             quotes = []             
             
                
       body += ']'
    
       callback = self.request.get('callback', ' ')  
    
       if callback != ' ':
         body = ('%s(%s);' % (callback, body))
      
       self.response.headers['Content-Type'] = 'text/json' 
       self.response.out.write(body)
    
            

def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
