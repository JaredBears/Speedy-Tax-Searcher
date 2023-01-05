from bs4 import BeautifulSoup
from urllib.request import urlopen

class ShelbyTrustee:
    url = "https://apps.shelbycountytrustee.com/TaxQuery/Inquiry.aspx?ParcelID="

    def searchProperty(self, property):
        try:
            parcel = property.getParcelId()
            pin = parcel[0:6] + "00" + parcel[6:] + "0"
            page = urlopen(self.url + pin)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            table = soup.find_all("tr")[13]
            taxes = float(table.find_all("td")[-1].text.strip()[1:])
            property.setCountyTaxes(taxes)
        except:
            property.setCountyTaxes(-1)