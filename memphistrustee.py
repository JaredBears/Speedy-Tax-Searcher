from bs4 import BeautifulSoup
from urllib.request import urlopen

class MemphisTrustee:
    url = "https://epayments.memphistn.gov/Property/Print.aspx?ParcelNo="

    def searchProperty(self, property):
        try:
            parcel = property.getParcelId()
            pin = parcel[0:6] + '%20' + '%20' + parcel[6:]
            page = urlopen(self.url + pin)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            table = soup.find_all("td")
            taxes = float(table[9].text.strip()[1:])
            property.setCityTaxes(taxes)
        except:
            property.setCityTaxes(-1)