class Property:
    def __init__(self, parcel_id, state, county):
        self.parcel_id = parcel_id
        self.county = county
        self.state = state
        self.address = None
        self.city = None
        self.subdivision = None
        self.lot = None
        self.platbook_page = None
        self.owner = None
        self.mailing_street = None
        self.mailing_city = None
        self.assessment = -1.0
        self.appraised_value = -1.0
        self.city_taxes = -1.0
        self.county_taxes = -1.0
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
        self.platbook_page = " ".join(platBookPage.split())
    def setOwner(self, owner):
        self.owner = " ".join(owner.split())
    def setMailingStreet(self, mailingStreet):
        self.mailing_street = " ".join(mailingStreet.split())
    def setMailingCity(self, mailingCity):
        self.mailing_city = " ".join(mailingCity.split())
    def setAssessment(self, assessment):
        self.assessment = assessment
    def setAppraisedValue(self, appraisedValue):
        self.appraised_value = appraisedValue
    def setCityTaxes(self, cityTaxes):
        self.city_taxes = cityTaxes
    def setCountyTaxes(self, countyTaxes):
        self.county_taxes = countyTaxes
    def setNotes(self, notes):
        self.notes = notes

    # Getters:
    def getParcelId(self):
        return self.parcel_id
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
        return self.platbook_page
    def getOwner(self):
        return self.owner
    def getMailingStreet(self):
        return self.mailing_street
    def getMailingCity(self):
        return self.mailing_city
    def getAssessment(self):
        return self.assessment
    def getAppraisedValue(self):
        return self.appraised_value
    def getCityTaxes(self):
        return self.city_taxes
    def getCountyTaxes(self):
        return self.county_taxes
    def getNotes(self):
        return self.notes

    # To String:
    def __str__(self):
        value = "Parcel ID: " + self.parcel_id + "\n" + \
                "State: " + self.state + "\n" + \
                "County: " + self.county + "\n"
        if self.city: value+= "City: " + self.city + "\n"
        if self.address: value+= "Address: " + self.address + "\n"
        if self.subdivision: value += "Subdivision: " + self.subdivision + "\n"
        if self.lot: value += "Lot: " + self.lot + "\n"
        if self.platbook_page: value += "Plat Book Page: " + self.platbook_page + "\n"
        if self.owner: value += "Owner: " + self.owner + "\n"
        if self.mailing_street: value += "Mailing Line 1: " + self.mailing_street + "\n"
        if self.mailing_city: value += "Mailing Line 2: " + self.mailing_city + "\n"
        if self.assessment != -1.0:
            value += "Assessment: $" + str(self.assessment) + "\n"
        else:
            value += "Assessment: Not Available\n"
        if self.appraised_value != -1.0:
            value += "Appraised Value: $" + str(self.appraised_value) + "\n"
        else:
            value += "Appraised Value: Not Available\n"
        if self.city_taxes != -1.0:
            value += "City Taxes: $" + str(self.city_taxes) + "\n"
        else:
            value += "City Taxes: Not Available\n"
        if self.county_taxes != -1.0:
            value += "County Taxes: $" + str(self.county_taxes) + "\n"
        else:
            value += "County Taxes: Not Available\n"
        if self.notes: value += "Notes: \n" + self.notes + "\n"
        return value

    # Return in CSV format:
    def toCSV(self):
        value = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.parcel_id, self.state, self.county, self.city, self.address, self.subdivision, self.lot, self.platbook_page, self.owner, self.mailing_street, self.mailing_city, self.assessment, self.appraised_value, self.city_taxes, self.county_taxes, self.notes)
        return value

    # Return in JSON format:
    def toJSON(self):
        value = "{{\n    \"parcelId\": \"{}\", \n    \"state\": \"{}\", \n    \"county\": \"{}\", \n    \"city\": \"{}\", \n    \"address\": \"{}\", \n    \"subdivision\": \"{}\", \n    \"lot\": \"{}\", \n    \"platbookPage\": \"{}\", \n    \"owner\": \"{}\", \n    \"mailingStreet\": \"{}\", \n    \"mailingCity\": \"{}\", \n    \"assessment\": {}, \n    \"appraisedValue\": {}, \n    \"cityTaxes\": {}, \n    \"countyTaxes\": {}, \n    \"notes\": \"{}\"\n}}".format(self.parcel_id, self.state, self.county, self.city, self.address, self.subdivision, self.lot, self.platbook_page, self.owner, self.mailing_street, self.mailing_city, self.assessment, self.appraised_value, self.city_taxes, self.county_taxes, self.notes)
        return value