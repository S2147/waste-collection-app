from flask import Flask, render_template_string
import requests, re, html

app = Flask(__name__)

@app.route("/")
def show_services():
    data = html.unescape(requests.get("https://www.ryde.nsw.gov.au/ocapi/Public/myarea/wasteservices?geolocationid=c03554da-cd5a-44d5-9699-727f529e8f40&ocsvclang=en-AU&pageLink=/$b9015858-988c-48a4-9473-7c193df083e4$/Information-Pages/My-area").json()['responseContent'])
    matches = re.findall(r'<h3>(.*?)</h3>.*?<div class="next-service">\s*(.*?)\s*</div>', data, re.DOTALL)
    html_out = "<h2>Waste Collection Services</h2><ul>" + "".join(f"<li>{w.strip()}: {d.strip()}</li>" for w, d in matches) + "</ul>"
    return render_template_string(html_out)

if __name__ == "__main__":
    app.run()
