import mechanicalsoup
from property import Property

class GermantownTrustee:
    url = "https://germ-egov.aspgov.com/Click2GovTX/accountsearch.html?"

    def searchProperty(self, property):
        parcel = property.getParcelId()
        district = parcel[0:3]
        block = parcel[3:6]
        sub = parcel[6]
        lot = parcel[7:]
        browser = mechanicalsoup.StatefulBrowser()
        browser.open(self.url)
        browser.select_form("form")
        

    def test(self):
        property = Property("G0221EH00027", "TN", "Shelby")
        self.searchProperty(property)
        print(property.getCityTaxes())

# germantown = GermantownTrustee()
# germantown.test()
        