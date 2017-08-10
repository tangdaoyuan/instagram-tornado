import tornado.ioloop
import tornado.options, tornado.web
import sys

tornado.options.define("port", default=8765, help="Run server on a specific port", type=int)
tornado.options.define("host", default="localhost", help="Run server on a specific host")
tornado.options.define("url", default=None, help="Url to show in HTML")
tornado.options.define("config", default="./config.yaml", help="config file's full path")
tornado.options.parse_command_line()

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
