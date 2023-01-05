class Property:
    def __init__(self, parcelId, state, county):
        self.parcelId = parcelId
        self.county = county
        self.state = state
        self.address = None
        self.city = None
        self.subdivision = None
        self.lot = None
        self.platBookPage = None
        self.owner = None
        self.mailingStreet = None
        self.mailingCity = None
        self.cityTaxes = -1.0
        self.countyTaxes = -1.0
        self.notes = None

    # Setters:
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
    def setNotes(self, notes):
        self.notes = notes

    # Getters:
    def getParcelId(self):
        return self.parcelId
    def getState(self):
        return self.state
    def getCounty(self):
        return self.county
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
    def getNotes(self):
        return self.notes

    # To String:
    def __str__(self):
        value = "Parcel ID: " + self.parcelId + "\n" + \
                "State: " + self.state + "\n" + \
                "County: " + self.county + "\n"
        if self.city: value+= "City: " + self.city + "\n"
        if self.address: value+= "Address: " + self.address + "\n"
        if self.subdivision: value += "Subdivision: " + self.subdivision + "\n"
        if self.lot: value += "Lot: " + self.lot + "\n"
        if self.platBookPage: value += "Plat Book Page: " + self.platBookPage + "\n"
        if self.owner: value += "Owner: " + self.owner + "\n"
        if self.mailingStreet: value += "Mailing Line 1: " + self.mailingStreet + "\n"
        if self.mailingCity: value += "Mailing Line 2: " + self.mailingCity + "\n"
        if self.cityTaxes != -1.0:
            value += "City Taxes: $" + str(self.cityTaxes) + "\n"
        else:
            value += "City Taxes: Not Available\n"
        if self.countyTaxes != -1.0:
            value += "County Taxes: $" + str(self.countyTaxes) + "\n"
        else:
            value += "County Taxes: Not Available\n"
        if self.notes: value += "Notes: \n" + self.notes + "\n"
        return value