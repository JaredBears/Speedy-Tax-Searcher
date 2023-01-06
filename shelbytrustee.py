from locale import atof, setlocale, LC_NUMERIC
from bs4 import BeautifulSoup
from urllib.request import urlopen
from property import Property

setlocale(LC_NUMERIC, 'English_United States.1252')

class ShelbyTrustee:
    url = "https://apps.shelbycountytrustee.com/TaxQuery/Inquiry.aspx?ParcelID="

    def searchProperty(self, property):
        try:
            pin = ""
            parcel = property.getParcelId()
            if parcel[0] == '0':
                pin = parcel[0:6] + "00" + parcel[6:] + "0"
            elif parcel[0] == 'B':
                pin = parcel[0:5] + "00" + parcel[5:] + "0"
            elif parcel[0] == 'G':
                pin = parcel[0:6] + "0" + parcel[6:] + "0"
            page = urlopen(self.url + pin)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            table = soup.find_all("tr")[13]
            taxes = atof(table.find_all("td")[-1].text.strip()[1:])
            property.setCountyTaxes(taxes)
        except:
            property.setCountyTaxes(-1)
    def test(self):
        property = Property("G0221EH00027","TN", "Shelby")
        self.searchProperty(property)
        print(property.getCountyTaxes())

# shelby = ShelbyTrustee()
# shelby.test()