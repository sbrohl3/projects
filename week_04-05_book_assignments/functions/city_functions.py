def get_formatted_location(city_name, country_name):
    """Takes in a city_name and country_name and returns a single string with both values
    Arguments:
    city_name [user input]-- User inserts the name of a city
    country_name [user input] -- User enters the name of the country associated with their provided city
    Returns:
    Returns a single string containing the city_name and country_name neatly formatted with a "," 
    """
    formatted_location = city_name + ", " + country_name
    return(formatted_location)

def get_formatted_location_and_pop(city_name, country_name, city_pop=0):
    """Takes in a city_name and country_name and its population and then returns a single string with both values
    Arguments:
    city_name [user input]-- User inserts the name of a city
    country_name [user input] -- User enters the name of the country associated with their provided city
    population [user input] -- User enters the size of the city/country's population
    Returns:
    Returns a single string containing the city_name and country_name and population all neatly formatted in output
    """
    formatted_location = city_name + ", " + country_name + " - population " + str(city_pop)
    return(formatted_location)

