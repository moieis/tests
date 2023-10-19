import time
import requests
from bs4 import BeautifulSoup
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.session import *
from pywebio.platform import *
from pywebio_battery import *





ss = open('stl.css','r').read()
sss= open('pal.png','rb').read()
yu = open('yemen.png','rb').read()


config(title='Free 🇵🇸',css_style=f'''{ss}''')
def intro():

               set_env(output_max_width='100%')


               put_html('''
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/5b/Flag-map_of_Yemen.png" class="yemenimage">
    ''')

               put_html('''
                       <img src="https://imageupload.io/ib/S1MkuBeGeWH05cR_1697670226.png" class="logoimage">
                   ''')


               put_html('''
                       <img src= 'https://upload.wikimedia.org/wikipedia/commons/7/7c/Flag_map_of_Mandatory_Palestine_with_a_Palestinian_flag.svg' class="plimage">
                   ''')



               put_text(''' وَلَقَدْ كَتَبْنَا فِي الزَّبُورِ مِن بَعْدِ الذِّكْرِ أَنَّ الْأَرْضَ يَرِثُهَا عِبَادِيَ الصَّالِحُونَ''').style("font-family: 'Amiri Quran';")




               put_html('''
<head>
<link href='https://fonts.googleapis.com/css?family=Amiri Quran' rel='stylesheet'>
</head>



''')

start_server(intro,port=1232)