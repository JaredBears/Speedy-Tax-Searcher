import shelbyassessor
import property

def main():
    parcelId = "06303400001"
    county = "Shelby"
    assessor = shelbyassessor.ShelbyAssessor()
    prop = property.Property(parcelId, county)
    assessor.searchProperty(prop)
    print(prop)


main()