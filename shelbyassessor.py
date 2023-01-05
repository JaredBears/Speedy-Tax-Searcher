from bs4 import BeautifulSoup
from urllib.request import urlopen
from property import Property
from shelbytrustee import ShelbyTrustee
from memphistrustee import MemphisTrustee
from bartletttrustee import BartlettTrustee

class ShelbyAssessor:
    url = "https://www.assessormelvinburgess.com/propertyDetails?parcelid="
    countyTrustee = ShelbyTrustee()
    memphisTrustee = MemphisTrustee()
    bartlettTrustee = BartlettTrustee()

    def searchProperty(self, property):
        try:
            parcel = property.getParcelId()
            page = urlopen(self.url + parcel)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            table = soup.find_all("td")
            property.setAddress(self.getAddress(table))
            property.setCity(self.getCity(table))
            property.setSubdivision(self.getSubdivision(table))
            property.setLot(self.getLot(table))
            property.setPlatBookPage(self.getPlatBookPage(table))
            property.setOwner(self.getOwner(table))
            property.setMailingStreet(self.getMailingStreet(table))
            property.setMailingCity(self.getMailingCity(table))
            self.countyTrustee.searchProperty(property)
            if parcel[0] == '0':
                self.memphisTrustee.searchProperty(property)
            elif parcel[0] == 'B':
                self.bartlettTrustee.searchProperty(property)
        except:
            property.setAddress("Error: Could not find property")
    def getAddress(self, table):
        return table[3].text.strip()
    def getCity(self, table):
        return table[5].text.strip()
    def getSubdivision(self, table):
        return table[17].text.strip()
    def getLot(self, table):
        return table[19].text.strip()
    def getPlatBookPage(self, table):
        return table[21].text.strip()
    def getOwner(self, table):
        return table[25].text.strip()
    def getMailingStreet(self, table):
        return table[27].text.strip()
    def getMailingCity(self, table):
        return table[29].text.strip()

    def test(self):
        property = Property("06303400001", "Shelby")
        self.searchProperty(property)
        print(property)

        propertyTwo = Property("B0149M00007", "Shelby")
        self.searchProperty(propertyTwo)
        print(propertyTwo)

# shelby = ShelbyAssessor()
# shelby.test()