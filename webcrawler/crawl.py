import scrapy
import requests

class Spider(scrapy.Spider):
    name = "Spider"
    start_urls = ["https://www.lukemcewen.com"]

    def parse(self, response):
        text = " ".join(response.css("p::text").getall())
        processed_text = self.send_to_deepseek(text)
        yield {"url": response.url, "processed_text": processed_text}
    
    def send_to_deepseek(self, text):
        api_url = "http://localhost:8000/v1/completions"
        payload = {
            "model": "deepseek-v3",
            "prompt": text,
            "max_tokens": 200
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, json=payload, headers=headers)
        return response.json().get("choices", [{}])[0].get("text", "").strip()