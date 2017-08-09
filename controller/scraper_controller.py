import tornado.web
import json
from tornado import gen
from utils.app import InstagramScraper, init_defautl_args


class ScraperController(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        json_data = json.loads(self.request.body)

        if json_data.has_key('password'):
            self.write(json.dumps(json_data))

        if json_data.has_key('username'):
            username = json_data['username']
            scraper = InstagramScraper(**vars(init_defautl_args(username)))
            res = yield scraper.scrape(username)
            self.write(json.dumps(res))

    def prepare(self):
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        super(ScraperController, self).prepare()
