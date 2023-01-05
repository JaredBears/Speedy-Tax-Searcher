import shelbyassessor
import property

def main():
    while(True):
        # state = input("Enter state (or exit to quit): ")
        # if state.lower() == "exit":
        #     break
        # county = input("Enter county: ")
        state = "TN"
        county = "Shelby"
        parcelId = input("Enter parcel ID (or exit to quit): ")
        if parcelId.lower() == "exit":
            break
        assessor = shelbyassessor.ShelbyAssessor()
        prop = property.Property(parcelId, state, county)
        assessor.searchProperty(prop)
        print(prop)


main()