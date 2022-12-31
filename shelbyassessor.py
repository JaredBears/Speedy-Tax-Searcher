from bs4 import BeautifulSoup
from urllib.request import urlopen
import shelbyproperty

class ShelbyAssessor:
    url = "https://www.assessormelvinburgess.com/propertyDetails?parcelid="

    def searchProperty(self, pin):
        property = shelbyproperty.ShelbyProperty()
        page = urlopen(self.url + pin)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find_all("td")
        property.setParcelId(pin)
        property.setAddress(self.getAddress(table))
        property.setCity(self.getCity(table))
        property.setSubdivision(self.getSubdivision(table))
        property.setLot(self.getLot(table))
        property.setPlatBookPage(self.getPlatBookPage(table))
        property.setOwner(self.getOwner(table))
        property.setMailingStreet(self.getMailingStreet(table))
        property.setMailingCity(self.getMailingCity(table))
        return property
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