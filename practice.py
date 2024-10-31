
def main():

    class Congregation:

        # Here I am initializing the class attributes to a default state
        def __init__(self, congregation_name=None, congregation_exists=False, publishers=0, elders=0, pioneers=0):
            self.congregation_name = congregation_name
            self.congregation_exists = congregation_exists
            self.publishers = publishers
            self.elders = elders
            self.pioneers = pioneers
            


        def __str__(self):
            empty_data = [self.congregation_name, self.publishers, self.elders, self.pioneers, self.congregation_exists]

            return empty_data

        # Here we have a function with logic that will change the default values of the class attributes depending on the boolean value inside "congregation_exists".
        def exists(self, congregation_exists, name_of_congregation=None, number_of_publishers=0, number_of_elders=0, number_of_pioneers=0):

            if congregation_exists == True:
                self.congregation_name = name_of_congregation
                self.congregation_exists = True
                self.publishers = number_of_publishers
                self.elders = number_of_elders
                self.pioneers = number_of_pioneers

                return f"Congregation exists: {self.congregation_exists}\nCongregation name: {self.congregation_name}\nNumber of publishers: {self.publishers}\nNumber of elders: {self.elders}\nNumber of pioneers: {self.pioneers}"

            elif congregation_exists == False:
                return f"Congregation exists: {congregation_exists}\nCongregation name: {self.congregation_name}\nNumber of publishers: {number_of_publishers}\nNumber of elders: {number_of_elders}\nNumber of pioneers: {number_of_pioneers}"

    # Creating a class instance "kingdom_hall" with all the Congregation class functions
    kingdom_hall = Congregation()

    print("Default mode on")
    # Default mode.
    print(kingdom_hall.exists(congregation_exists=False))
    print("\nDefault mode off")
    # Changed the value from the default mode.
    print(kingdom_hall.exists(congregation_exists=True, name_of_congregation="Revenna", number_of_publishers=123, number_of_elders=13, number_of_pioneers=28))

if __name__=="__main__":
    main()