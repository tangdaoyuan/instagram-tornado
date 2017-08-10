import tornado.ioloop
import tornado.options, tornado.web
import sys
import yaml

globals_config = {}
try:
    with open("./config/config.yaml", 'r') as fin:
        globals_config = yaml.load(fin)
except:
    print "cannot found config.yaml file"
    sys.exit(0)

print globals_config

tornado.options.define("port", default=8765, help="Run server on a specific port", type=int)
tornado.options.define("host", default="localhost", help="Run server on a specific host")
tornado.options.define("url", default=None, help="Url to show in HTML")
tornado.options.define("config", default="./tornado_config.yaml", help="config file's full path")
tornado.options.define("proxy_host", default=None)
tornado.options.define("proxy_port", default=None, type=int)
tornado.options.parse_command_line()

tornado.options.options.host = globals_config['http_server']['server_address']
tornado.options.options.port = globals_config['http_server']['server_port']

if globals_config.has_key("proxy_server"):
    tornado.options.options.proxy_host = globals_config["proxy_server"]["proxy_address"]
    tornado.options.options.proxy_port = globals_config["proxy_server"]["proxy_port"]

if not tornado.options.options.url:
    tornado.options.options.url = "http://%s:%d" % (tornado.options.options.host, tornado.options.options.port)

application = tornado.web.Application([(r"^/scraper/*", "controller.scraper_controller.ScraperController")])

if __name__ == "__main__":
    try:
        application.listen(tornado.options.options.port)
        print r"bind address:%d" % tornado.options.options.port
        tornado.ioloop.IOLoop.instance().start()
    except:
        import traceback

        print traceback.print_exc()
    finally:
        sys.exit(0)
