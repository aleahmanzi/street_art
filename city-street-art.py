#!/usr/bin/python
# coding: latin-1

Site = 'City Street Art'

# Timezone = 'Pacific/Honolulu'
Timezone = 'US/Pacific'

Analytics = '''<script>
</script>'''

# - HTML Page Code

upload_page_html = '''<style>
body { background: url(../pics/main_img.jpg); }
.pic_wrap { outline: 0px solid blue; width: 500px; height: 600px; position: relative; margin: 0 auto; }
.load_pic { outline: 0px solid red; width: 500px; height: 600px; font-family: Hind; margin: 0 auto; }
.main_wrap { outline: 0px solid black; width: 400px; height: 600px; margin: 0 auto; }
.form_wrap { margin-top: 35px; padding: 45px; }
.color_b { position: relative; top: 25px; color: black; font-family: "Rock Salt"; font-size: 22px; }
tr { height: 30px; }
input[type="text"] { height: 35px; width: 300px; border-radius: 15px; outline: none; background: ##FFFBFD; border: none; }
#location { width: 150px; border-radius: 15px; outline: none; background: ##FFFBFD; border: none; display: inline-block;}
.add_location { position: relative; right: 100px; }


.custom-file-input::-webkit-file-upload-button { visibility: hidden; }
.custom-file-input::before { content: 'Browse files'; display: inline-block; border: 1px solid #999; border-radius: 10px; padding: 10px 10px; outline: none; white-space: nowrap; font-weight: 700; font-size: 10pt; background: #FFFBFD; width: 180px; text-align: center; position: relative; bottom: 35px; }
.custom-file-input:hover:before { border-color: #88C7CC; cursor: pointer; background: #FFFAFF; }

.next_button { content: 'Browse files'; display: inline-block; border: 1px solid #999; border-radius: 10px; padding: 5px 25px; outline: none; font-size: 10pt; background: #FFFBFD; width: 25px; float: right; }
.next_button:hover { border-color: #88C7CC; cursor: pointer; color: #88C7CC; }
.add_location { content: 'Browse files'; display: inline-block; border: 1px solid #999; border-radius: 10px; padding: 5px 25px; outline: none; font-size: 10pt; background: #FFFBFD; width: 75px; float: right; }
.add_location:hover { border-color: #88C7CC; cursor: pointer; color: #88C7CC; }

.fileDetails-yes { display: block; }
.fileDetails-no { display: none; } 
.fileSelect-yes { display: block; }
.fileSelect-no { display: none; } 


</style>

<section class="pic_wrap fileSelect-[!fileSelect!]">
 <div class="load_pic">
  <div class="main_wrap">
    <article class="form_wrap">
      <form action="../../add_data" enctype="multipart/form-data" method="post">
        <table>
          <tr>
            <td class="input"><input type="file" class="custom-file-input" name="art_photo" title="Browse Files"/></td>
          </tr>
          <tr>
            <td class="next_button">
             <div ng-click="addDetails()">Next
             </div>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- .main_wrap - -->
 </div><!-- - .load_pic - -->
</section><!-- . pic_wrap - -->

<section class="pic_wrap fileDetails-[!fileDetails!]">
 <div class="load_pic">
  <div class="main_wrap">
    <article class="form_wrap">
      <form action="../../add_data" enctype="multipart/form-data" method="post">
        <table>
          <tr>
            <td class="input"><input type="text" name="art_title" placeholder="   Add Title Here" required/></td>
          </tr>
          <tr>
            <td class="input"><input type="text" name="art_desc" placeholder="   Add Description Here" required/></td>
          </tr>
          <tr>
            <td class="add_location">
             <div ng-click="addCoordinates()">Add Location
             </div>
          </tr>
          <tr>
            <td class="input" id="location"><input type="text" name="art_latitude" placeholder="    latitude" ng-model="latitude" value="[! latitude !]" required/></td>
          </tr>
          <tr>
            <td class="input" id="location"><input type="text" name="art_longitude" placeholder="    longitude" ng-model="longitude" value="[! $scope.longitude!]" required/></td>
          </tr>
          <tr>
            <td style="text-align:right" id="submit" class="add_button"><input type="submit" value="Add New Street Art" /></td>
          </tr>
        </table>
      </form>
    </article><!-- - /form_wrap - -->
  </div><!-- .main_wrap - -->
 </div><!-- - .load_pic - -->
</section><!-- . pic_wrap - -->
'''

gallery_page_html = '''<style>
.projects_wrap { outline: 0px solid blue; width: 100%; }
.top_section { outline: 0px solid black; margin: 0 auto; width: 675px; }
.project_image_wrap { display: inline-block; vertical-align: top; height: 400px;  }
.project_image_wrap img { height: 100%; margin-left: 150px; }

.thumb_wrap { outline: 0px solid red; width: 300px;  }
.photo_thumb { outline: 0px solid red; display: inline-block; height: 50px; margin-right: 10px; cursor: pointer; }
.photo_thumb img { height: 100%; opacity: 0.7; transition: all 2s ease;  }
.photo_thumb img:hover { opacity: 1; transition: all 2s ease; }
.thumb_wrap { margin-left: 210px; margin-top: 10px;  }

.text_wrap { font-size: 13px; line-height: 20px; white-space: pre-wrap; margin-left: 210px; margin-top: 10px; }
.project_text_wrap p { margin-left: 210px; margin-top: 30px; }

</style>

<div class="projects_wrap">

<div class="top_section">
  <div class="project_image_wrap">
    <img ng-src="../../render?photo?large?[!mainImageUrl!]">
  </div><!-- - /project_image_wrap - -->
  <div class="thumb_wrap">
   <div class="photo_thumb" ng-repeat="item in street_photos" ng-click="setImage(item)"><img ng-src="../../render?photo?small?[! item.data_id !]" /></div>
  </div><!-- - /thumb_wrap - -->
</div><!-- - /top_section - -->

  <div class="project_text_wrap">
    <p class="title">[! item.art_title !] &nbsp; [! item.art_latitude !] [! item.art_longitude !]</p>
    <hr />
    <div class="text_wrap">[! item.art_about !]</div>
  </div>

</div><!-- - /projects_wrap - -->
'''

map_page_html = '''<style>
.map_wrap { outline: 0px solid blue; }
#map_canvas { outline: 0px solid red; width: 700px; height: 500px; margin: 0 auto; position: relative; }
.item_wrap { outline: 0px solid red; width: 100%; }
.button_wrap { outline: 0px solid blue; margin: 0 auto; width: 125px; }
#geoFindMe { cursor: pointer; border: 1px solid #212121; width: 125px; text-align: center; font-size: 14px; border-radius: 5px; color: #212121; }
#geoFindMe :hover { border: 1px solid #eee; color: #eee; }
</style>

<section class="map_wrap open_map-[!open_map!]">
 <div id="map_canvas">[! map !]</div>
  <section class="item_wrap">
   <div class="button_wrap">
    <p id="geoFindMe">Search Near Me</p>
    <div id="out"></div>
  </section><!-- . map_wrap - --> 
 </div><!-- .button_wrap - -->
</section><!- .item_wrap - -->

'''


#----------------------------------------------#
#             Code                             #
#----------------------------------------------#
import os
import urllib
import wsgiref.handlers
import webapp2
from webapp2_extras import routes
import json
import logging
# - 
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
# -
from google.appengine.ext import db
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
# -
from urlparse import urlparse
import urllib2
# -
import time
import datetime
from pytz.gae import pytz
#- stripe
import stripe
stripe.api_key = "xxxxxxxx"

#----------------------------------------------#
#           Art Data Stucture                  #
#----------------------------------------------#
class Data_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
    #
    user_name =  ndb.StringProperty()
    #
    art_title = ndb.StringProperty()
    art_about = ndb.StringProperty()
    art_latitude = ndb.StringProperty()
    art_longitude = ndb.StringProperty()
    art_photo = ndb.BlobProperty()

class addData_db(webapp2.RequestHandler):
  def post(self):

    data_id = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d%H%M%S")
    item = Data_db(id=data_id)
    item.data_id = data_id

    if users.get_current_user():
      data_id = self.request.get('data_id')
      if data_id and data_id != '':
        item = Data_db.get_by_id(data_id)
      else:
        data_id = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y%m%d%H%M%S")
        item = Data_db(id=data_id)
        item.data_id = data_id
      # - -
    item.user_name = users.get_current_user()
    item.art_title = self.request.get('art_title')
    item.art_about = self.request.get('art_desc')
    item.art_latitude = self.request.get('art_latitude')
    item.art_longitude = self.request.get('art_longitude')
    
    art_photo = self.request.get('art_photo')
    if art_photo:
      item.art_photo = images.resize(art_photo, 800, 600)
    #
    item.put()
    time.sleep(1)
    self.redirect('/gallery')

#----------------------------------------------#
#             Photo Rendering                  #
#----------------------------------------------#
class renderImage(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        data_set = base.split('?')[1]
        img_size = base.split('?')[2]
        data_id = base.split('?')[3]

        if data_set == 'photo':
            item = Data_db.get_by_id(data_id)
            img = images.Image(item.art_photo)
            if img_size == 'small':
                img.resize(width=90)
            if img_size == 'medium':
                img.resize(width=175)
            if img_size == 'large':
                img.resize(width=675)
            image = img.execute_transforms(output_encoding=images.JPEG)
            self.response.headers['Content-Type'] = 'image/jpeg'
            self.response.out.write(image)
        else:
            self.response.out.write("No image")
#----------------------------------------------#
#             HTML Page Production             #
#----------------------------------------------#
class publicSite(webapp2.RequestHandler):
    def get(self):
      # - page url
        page_address = self.request.uri
        path_layer = urlparse(page_address)[2].split('/')[1]
        base = os.path.basename(page_address)
      # - user
        user = users.get_current_user()
        if users.get_current_user(): # - logged in
          login_key = users.create_logout_url(self.request.uri)
          gate = 'Sign out'
          user_name = user.email()
        else: # - logged out
          login_key = users.create_login_url(self.request.uri)
          gate = 'Sign in'
          user_name = 'No User'
      # - app data
        app = Site
        page_name = 'Main'
        page_id = 'about'
        analytics = Analytics
        page_html = map_page_html
        admin = ''
        program_chosen = ''
        data_id = ''

        if users.is_current_user_admin():
            admin = 'true' 

        if path_layer == 'gallery':
            page_id = 'gallery'
            page_name = 'Gallery'
            page_html = gallery_page_html

        if path_layer == 'map':
            page_id = 'map'
            page_name = 'Map'
            page_html = map_page_html

        if path_layer == 'upload':
            page_id = 'upload'
            page_name = 'Upload'
            page_html = upload_page_html

      # - template
        objects = {
            'Site': app,
            'analytics': analytics,
            'login_key': login_key,
            'gate': gate,
            'user_name': user_name,
            'admin': admin,
          # -
            'path_layer': path_layer,
            'base': base,
            'page_name': page_name,
            'page_id': page_id,
            'page_html': page_html,
            'data_id': data_id,
            'program_chosen': program_chosen,     
        }
      # - render
        path = os.path.join(os.path.dirname(__file__), 'html/publicSite.html')
        self.response.out.write(template.render(path, objects))
#----------------------------------------------#
#            Error Handling                    #
#----------------------------------------------#
def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('A 404 error occurred!')
    response.set_status(404)

def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('A 500 error occurred!')
    response.set_status(500)

#----------------------------------------------#
#                                              #
#----------------------------------------------#

class listData(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        data_set = base.split('?')[1]
        if data_set == 'street_photos':
            db_data = Data_db.query().fetch(projection=[
              'data_id',
              'art_title',
              'art_about',
              'art_longitude',
              'art_latitude',
            ])
        data = []
        for f in db_data:
            data.append(f.to_dict())
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(data))

#----------------------------------------------#
#                                              #
#----------------------------------------------#
app = webapp2.WSGIApplication([    # - Pages

    ('/', publicSite),
    ('/list/?', listData),


    ('/gallery/?', publicSite),
    ('/upload/?', publicSite),
    ('/location/?', publicSite),
    ('/add_data/?', addData_db),

    ('/render/?', renderImage),


], debug=True)
# app.error_handlers[404] = handle_404
# app.error_handlers[500] = handle_500
