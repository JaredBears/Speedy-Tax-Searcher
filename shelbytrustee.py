import mechanicalsoup
import datetime
from urllib.request import urlopen

class ShelbyTrustee:
    browser = mechanicalsoup.Browser()
    url = "https://apps.shelbycountytrustee.com/TaxQuery/Inquiry.aspx?ParcelID="

    def searchProperty(self, property):
        currentYear = datetime.datetime.now().year
        parcel = property.getParcelId()
        pin = parcel[0:6] + "00" + parcel[6:] + "0"
        page = self.browser.get(self.url + pin)
        html = page.soup
        table = html.find_all("tr")[13]
        taxes = float(table.find_all("td")[-1].text.strip()[1:])
        property.setCountyTaxes(taxes)