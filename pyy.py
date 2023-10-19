from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.session import *
from pywebio.platform import *
from pywebio_battery import *






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






if __name__ == '__main__':
        import argparse
        from pywebio.platform.tornado_http import start_server as start_http_server
        from pywebio import start_server as start_ws_server
        
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--port", type=int, default=8080)
        parser.add_argument("--http", action="store_true", default=False,
                            help='Whether to enable http protocol for communicates')
        args = parser.parse_args()

        if args.http:
            start_http_server(
                intro,
                port=args.port, debug=False)
        else:
            # Since some cloud server may close idle connections (such as heroku),
            # use `websocket_ping_interval` to  keep the connection alive
            start_ws_server(
                intro,
                port=args.port, websocket_ping_interval=30, debug=False, cdn=True)

