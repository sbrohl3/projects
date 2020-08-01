from newsapi import NewsApiClient
##pip install newsapi-python

## Default Variables
queries = []
key_count = 0
count = 0
page = 1
retry = 0

## To be imported from file in final product
api_keys = ["599f63190ef34538a1bd12b6ee12739d", "6716aa5c8e2544e69c2e1b7fe1f8c194", "d1d13f1e4d8942d89cd592e16aac6d68"]


newsapi = NewsApiClient(api_key=api_keys[0])

query_input = True
print("Please enter in up to 10 keywords to search for or press Enter to use the default list: \n")
while query_input:
    
    add_queries = str(input(" "))
    queries.append(add_queries)
    
    if len(queries) == 10:
        print("Using this list:\n")
        for query in queries:
            print("\t- " + query)

        print("\nIs this good? ()")
        query_input = False

    elif len(queries) != 10:
        for query in queries:
            print("\t- " + query)
        query_input = True


#queries =["in-vehicle-sensing", "autonomous", "AI", "Artifical Intelligence", "occupant monitoring", "general motors", "GM", "ford motor company", "ford", "waymo", "uber", "lyft", "car sharing", "ride hailing ride sharing", "yandex", "ola", "didi", "maven", "sharenow"] 
done = False

integer = False
while not integer:
    try:
        num_pages = int(input("How many pages would you like to display results for (Can't be greater than 5 pages):  "))
        integer = True

        if num_pages > 5:
            print("\nYou have entered a value greater than 5. Please try again.\n")
            integer = False

        elif num_pages == 0:
            print("\nYou cannot enter 0 for the number of pages. Please try again.\n")
            integer = False

    except:
        print("\nYou have not entered an integer please try again!\n")
        integer = False

while page != num_pages + 1 and integer == True:
    
    print("\nPage " + str(page) + " results: \n")
    
    for query in queries:

        try:
            all_articles = newsapi.get_everything(q=query,
                                                from_param='2020-02-01',
                                                language='en',
                                                sort_by='relevancy',
                                                page=page)

            for count in range(len(all_articles["articles"])):
                
                if query in all_articles["articles"][count]["title"]:
                    
                    print(str(all_articles["articles"][count]["title"]))
                    print("\t- " + str(all_articles["articles"][count]["url"]))
                    print("\t- " + str(all_articles["articles"][count]["source"]["name"]))
                    count += 1
                
                elif count > len(all_articles["articles"]):
                    
                    done = True
                    print("")

                else:
                    count += 1

        except:
            if key_count < len(api_keys):
                print("\nAPI Key exhausted: Choosing new key and restarting crawl...\n")
                newsapi = NewsApiClient(api_key=api_keys[key_count])
                key_count += 1

            elif key_count >= len(api_keys):
                print("\nRan out of working API keys... Resetting list to 0 and retrying.\n")
                key_count = 0

                if retry >= 5:
                    print("\nAll API keys exhausted. Please try again later!\nClosing program...\n")
                    exit()

                else:
                    retry += 1

    count = 0
    page += 1


