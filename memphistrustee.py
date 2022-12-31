import mechanicalsoup
import datetime
from urllib.request import urlopen

class MemphisTrustee:
    browser = mechanicalsoup.Browser()
    url = "https://epayments.memphistn.gov/Property/Print.aspx?ParcelNo="

    def searchProperty(self, property):
        currentYear = datetime.datetime.now().year
        parcel = property.getParcelId()
        pin = parcel[0:6] + '%20' + '%20' + parcel[6:]
        page = self.browser.get(self.url + pin)
        html = page.soup
        table = html.find_all("td")
        taxes = float(table[9].text.strip()[1:])
        property.setCityTaxes(taxes)