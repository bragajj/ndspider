# Jeff Braga 12/12/22
import scrapy
from scrapy.http import Request
import json
import requests


class NDSpider(scrapy.Spider):
    name = 'ndspider'
    start_urls = 'https://firststop.sos.nd.gov/api/Records/businesssearch/'

    # Start crawling with business search POST request
    def start_requests(self):
        url = 'https://firststop.sos.nd.gov/api/Records/businesssearch/'
        headers = {
            "authority": "firststop.sos.nd.gov",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "authorization": "undefined",
            "content-type": "application/json",
            "origin": "https://firststop.sos.nd.gov",
            "referer": "https://firststop.sos.nd.gov/search/business",
            "sec-ch-ua": "\"Opera\";v=\"93\", \"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"107\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
        }
        body = '{"SEARCH_VALUE":"X","STARTS_WITH_YN":"true","ACTIVE_ONLY_YN":true}'
        yield Request(url=url, method='POST', dont_filter=True, headers=headers, body=body)

    # Work through initial POST response, add additional data for each business
    def parse(self, response) -> None:
        data = json.loads(response.text)
        for id in data["rows"]:
            company_url = "https://firststop.sos.nd.gov/api/FilingDetail/business/" + \
                str(id)+"/false/"
            company_info = requests.get(company_url)
            company_json = json.loads(company_info.text)
            # Data cleanup
            trim_json = {detail['LABEL']: detail['VALUE']
                         for detail in company_json['DRAWER_DETAIL_LIST']}
            data["rows"][id]["INFO"] = trim_json
        self.save_data(data)

    def save_data(self, crawled_data) -> None:
        with open("data/nd_data.json", "w") as outfile:
            json.dump(crawled_data, outfile)