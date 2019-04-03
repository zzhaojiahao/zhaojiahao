"""

"""

__author__ = ""
__date__ = ""


from destinations import Destinations


def main():
    # Task 1: Ask questions here

    def continent_valid(ans_continent):
        for i in range(len(ans_continent)):
            while (ans_continent[i] not in ["1", "2", "3", "4", "5", "6", "7"]):
                print("\nI'm sorry, but", ans_continent, "is not a valid choice. Please try again.")
                print("\nWhich continent would you like to travel to?")
                print("  1) Asia")
                print("  2) Africa")
                print("  3) North America")
                print("  4) South America")
                print("  5) Europe")
                print("  6) Oceania")
                print("  7) Antarctica")
                return True
        return False


    def season_valid(ans_season):
        for i in range(len(ans_season)):
            while (ans_season[i] not in ["1", "2", "3", "4"]):
                print("\nI'm sorry, but", ans_season, "is not a valid choice. Please try again.")
                print("\nWhich season do you plan to travel in?")
                print("  1) Spring")
                print("  2) Summer")
                print("  3) Autum")
                print("  4) Winter")
                return True
        return False


    def crime_level(crime):
        crime_list = ["low", "average", "high"]
        for i in range(3):
            if crime == crime_list[i]:
                level = i + 1
                return level




    # investigation

    print("Welcome to Travel Inspiration!")
    print("What is your name?")
    ans_name = input(">")
    print("Hi,", ans_name + "!")



    print("Which continent would you like to travel to?")
    print("  1) Asia")
    print("  2) Africa")
    print("  3) North America")
    print("  4) South America")
    print("  5) Europe")
    print("  6) Oceania")
    print("  7) Antarctica")
    flag_continent = True
    while (flag_continent):
        ans_continent = input(">")
        if ("," in ans_continent):
            ans_continent = list([one.strip() for one in ans_continent.split(",")])
        flag_continent = continent_valid(ans_continent)

    ans_continent = list(map(int, set(ans_continent)))



    print("\nWhat is money to you?")
    print("  $$$) No object")
    print("  $$) Spendable, so long as I get value from doing so")
    print("  $) Extremely important; I want to spend as little as possible")
    ans_cost = input(">")
    while (ans_cost not in ["$$$","$$","$"]):
        print("\nI'm sorry, but", ans_cost, "is not a valid choice. Please try again.")
        print("\nWhat is money to you?")
        print("  $$$) No object")
        print("  $$) Spendable, so long as I get value from doing so")
        print("  $) Extremely important; I want to spend as little as possible")
        ans_cost = input(">")



    print("\nHow much crime is acceptable when you travel?")
    print("  1) Low")
    print("  2) Average")
    print("  3) High")
    ans_crime = input(">")
    while (ans_crime not in ["1","2","3"]):
        print("\nI'm sorry, but", ans_crime, "is not a valid choice. Please try again.")
        print("\nHow much crime is acceptable when you travel?")
        print("  1) Low")
        print("  2) Average")
        print("  3) High")
        ans_crime = input(">")
    ans_crime = int(ans_crime)



    print("\nWill you be travelling with children?")
    print("  1) Yes")
    print("  2) No")
    ans_kid = input(">")
    while (ans_kid not in ["1", "2"]):
        print("\nI'm sorry, but", ans_kid, "is not a valid choice. Please try again.")
        print("\nWill you be travelling with children?")
        print("  1) Yes")
        print("  2) No")
        ans_kid = input(">")
    ans_kid = int(ans_kid)



    print("\nWhich season do you plan to travel in?")
    print("  1) Spring")
    print("  2) Summer")
    print("  3) Autum")
    print("  4) Winter")
    flag_season = True
    while (flag_season):
        ans_season = input(">")
        if ("," in ans_season):
            ans_season = list([one.strip() for one in ans_season.split(",")])
        flag_season = season_valid(ans_season)

    ans_season = list(map(int, set(ans_season)))



    print("\nWhat climate do you prefer?")
    print("  1) Cold")
    print("  2) Cool")
    print("  3) Mederate")
    print("  4) Warm")
    print("  5) Hot")
    ans_climate = input(">")
    while (ans_climate not in ["1","2","3","4","5"]):
        print("\nI'm sorry, but", ans_climate, "is not a valid choice. Please try again.")
        print("\nWhat climate do you prefer?")
        print("  1) Cold")
        print("  2) Cool")
        print("  3) Mederate")
        print("  4) Warm")
        print("  5) Hot")
        ans_climate = input(">")
    ans_climate = int(ans_climate)



    print("\nNow we would like to ask you some questions about your interests, on a scale of -5 to 5. ")
    print("-5 indicates strong dislike, whereas 5 indicates strong interest, and 0 indicates indifference.")


    print("\nHow much do you like sports? (-5 to 5)")
    ans_sports = input(">")
    while (ans_sports not in ["-5","-4","-3","-2","-1","0","1","2","3","4","5"]):
        print("\nI'm sorry, but", ans_sports, "is not a valid choice. Please try again.")
        print("\nHow much do you like sports? (-5 to 5)")
        ans_sports = input(">")
    ans_sports = int(ans_sports)



    print("\nHow much do you like wildlife? (-5 to 5)")
    ans_wildlife = input(">")
    while (ans_wildlife not in ["-5","-4","-3","-2","-1","0","1","2","3","4","5"]):
        print("\nI'm sorry, but", ans_wildlife, "is not a valid choice. Please try again.")
        print("\nHow much do you like wildlife? (-5 to 5)")
        ans_wildlife = input(">")
    ans_wildlife = int(ans_wildlife)





    print("\nHow much do you like nature? (-5 to 5)")
    ans_nature = input(">")
    while (ans_nature not in ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"]):
        print("\nI'm sorry, but", ans_nature, "is not a valid choice. Please try again.")
        print("\nHow much do you like nature? (-5 to 5)")
        ans_nature = input(">")
    ans_nature = int(ans_nature)



    print("\nHow much do you like historical sites? (-5 to 5)")
    ans_history = input(">")
    while (ans_history not in ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"]):
        print("\nI'm sorry, but", ans_history, "is not a valid choice. Please try again.")
        print("\nHow much do you like historical sites? (-5 to 5)")
        ans_history = input(">")
    ans_history = int(ans_history)



    print("\nHow much do you like fine dining? (-5 to 5)")
    ans_dining = input(">")
    while (ans_dining not in ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"]):
        print("\nI'm sorry, but", ans_dining, "is not a valid choice. Please try again.")
        print("\nHow much do you like fine dining? (-5 to 5)")
        ans_dining = input(">")
    ans_dining = int(ans_dining)



    print("\nHow much do you like adventure activities? (-5 to 5)")
    ans_adventure = input(">")
    while (ans_adventure not in ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"]):
        print("\nI'm sorry, but", ans_adventure, "is not a valid choice. Please try again.")
        print("\nHow much do you like adventure activities? (-5 to 5)")
        ans_adventure = input(">")
    ans_adventure = int(ans_adventure)



    print("\nHow much do you like the beach? (-5 to 5)")
    ans_beach = input(">")
    while (ans_beach not in ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"]):
        print("\nI'm sorry, but", ans_beach, "is not a valid choice. Please try again.")
        print("\nHow much do you like the beach? (-5 to 5)")
        ans_beach = input(">")
    ans_beach = int(ans_beach)






    # Task 2+: Output final answer here

    continent_list = ["asia","africa","north america","south america",
                      "europe","oceania","antarctica"]

    if ans_kid == 1:
        kid_list = [True]
    else:
        kid_list = [True,False]

    climate_list = ["cold", "cool", "moderate", "warm", "hot"]

    season_list = ["spring", "summer", "autumn", "winter"]



    print("Thank you for answering all our questions.")

    recommend_flag = 1
    Score = []
    recommend_list = []
    for destination in Destinations().get_all():
        for ans in ans_continent:
            if (continent_list[int(ans) - 1] == destination.get_continent()
                    and destination.is_kid_friendly() in kid_list
                    and len(ans_cost) >= len(destination.get_cost())
                    and ans_crime >= crime_level(destination.get_crime())
                    and climate_list[ans_climate-1] == destination.get_climate()):

                interest_score = (ans_sports * destination.get_interest_score("sports")
                                  + ans_wildlife * destination.get_interest_score("wildlife")
                                  + ans_nature * destination.get_interest_score("nature")
                                  + ans_history * destination.get_interest_score("historical")
                                  + ans_dining * destination.get_interest_score("cuisine")
                                  + ans_adventure * destination.get_interest_score("adventure")
                                  + ans_beach * destination.get_interest_score("beach"))
                season_factor_list = []
                for j in ans_season:
                    season_factor_list.append(destination.get_season_factor(season_list[int(j) - 1]))
                max_season_factor = max(season_factor_list)
                Score.append((max_season_factor * interest_score))
                recommend_list.append(destination.get_name())
                recommend_flag = 0

    # print("alternative_destination is:", recommend_list)
    # print("alternative_Score is:", Score)

    if recommend_flag:
        print("Your next travel destination is None")
    else:
        print("\nThank you for answering all our questions. Your next travel destination is:")
        print(recommend_list[Score.index(max(Score))])
        print("Destination Score is:")
        print(round(Score[Score.index(max(Score))], 2))



if __name__ == "__main__":
    main()