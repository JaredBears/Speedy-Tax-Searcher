class ShelbyProperty:
    def __init__(self):
        self.parcelId = ""
        self.address = ""
        self.city = ""
        self.subdivision = ""
        self.lot = ""
        self.platBookPage = ""
        self.owner = ""
        self.mailingStreet = ""
        self.mailingCity = ""
        self.cityTaxes = 0.0
        self.countyTaxes = 0.0
    def setParcelId(self, parcelId):
        self.parcelId = " ".join(parcelId.split())
    def setAddress(self, address):
        self.address = " ".join(address.split())
    def setCity(self, city):
        self.city = " ".join(city.split())
    def setSubdivision(self, subdivision):
        self.subdivision = " ".join(subdivision.split())
    def setLot(self, lot):
        self.lot = " ".join(lot.split())
    def setPlatBookPage(self, platBookPage):
        self.platBookPage = " ".join(platBookPage.split())
    def setOwner(self, owner):
        self.owner = " ".join(owner.split())
    def setMailingStreet(self, mailingStreet):
        self.mailingStreet = " ".join(mailingStreet.split())
    def setMailingCity(self, mailingCity):
        self.mailingCity = " ".join(mailingCity.split())
    def setCityTaxes(self, cityTaxes):
        self.cityTaxes = cityTaxes
    def setCountyTaxes(self, countyTaxes):
        self.countyTaxes = countyTaxes
    def getParcelId(self):
        return self.parcelId
    def getAddress(self):
        return self.address
    def getCity(self):
        return self.city
    def getSubdivision(self):
        return self.subdivision
    def getLot(self):
        return self.lot
    def getPlatBookPage(self):
        return self.platBookPage
    def getOwner(self):
        return self.owner
    def getMailingStreet(self):
        return self.mailingStreet
    def getMailingCity(self):
        return self.mailingCity
    def getCityTaxes(self):
        return self.cityTaxes
    def getCountyTaxes(self):
        return self.countyTaxes
    def __str__(self):
        value = "Parcel ID: " + self.parcelId + "\n" + \
                "Address: " + self.address + "\n" + \
                "City: " + self.city + "\n" + \
                "Subdivision: " + self.subdivision + "\n" + \
                "Lot: " + self.lot + "\n" + \
                "Plat Book Page: " + self.platBookPage + "\n" + \
                "Owner: " + self.owner + "\n" + \
                "Mailing Line 1: " + self.mailingStreet + "\n" + \
                "Mailing Line 2: " + self.mailingCity + "\n" + \
                "City Taxes Due: $" + str(self.cityTaxes) + "\n" + \
                "County Taxes Due: $" + str(self.countyTaxes) + "\n"
        return value