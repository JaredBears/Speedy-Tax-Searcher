class Property:
    def __init__(self, parcel_id, state, county):
        self.parcel_id = parcel_id
        self.county = county
        self.state = state
        self.address = None
        self.city = None
        self.subdivision = None
        self.legal_description = None
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
    def setLegalDescription(self, legal_description):
        self.legal_description = legal_description
    def setOwner(self, owner):
        self.owner = " ".join(owner.split())
    def setMailingStreet(self, mailing_street):
        self.mailing_street = " ".join(mailing_street.split())
    def setMailingCity(self, mailing_city):
        self.mailing_city = " ".join(mailing_city.split())
    def setAssessment(self, assessment):
        self.assessment = assessment
    def setAppraisedValue(self, appraised_value):
        self.appraised_value = appraised_value
    def setCityTaxes(self, city_taxes):
        self.city_taxes = city_taxes
    def setCountyTaxes(self, county_taxes):
        self.county_taxes = county_taxes
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
    def getLegalDescription(self):
        return self.legal_description
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
        if self.legal_description: value += "Legal Description: " + self.legal_description + "\n"
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
        value = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.parcel_id, self.state, self.county, self.city, self.address, self.legal_description, self.owner, self.mailing_street, self.mailing_city, self.assessment, self.appraised_value, self.city_taxes, self.county_taxes, self.notes)
        return value

    # Return in JSON format:
    def toJSON(self):
        value = "{{\n    \"parcelId\": \"{}\", \n    \"state\": \"{}\", \n    \"county\": \"{}\", \n    \"city\": \"{}\", \n    \"address\": \"{}\", \n    \"legalDescription\": \"{}\", \n    \"owner\": \"{}\", \n    \"mailingStreet\": \"{}\", \n    \"mailingCity\": \"{}\", \n    \"assessment\": {}, \n    \"appraisedValue\": {}, \n    \"cityTaxes\": {}, \n    \"countyTaxes\": {}, \n    \"notes\": \"{}\"\n}}".format(self.parcel_id, self.state, self.county, self.city, self.address, self.legal_description, self.owner, self.mailing_street, self.mailing_city, self.assessment, self.appraised_value, self.city_taxes, self.county_taxes, self.notes)
        return value