from destinations import Destinations


def main():
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




    continent_list = ["asia", "africa", "north america", "south america",
                      "europe", "oceania", "antarctica"]

    season_list = ["spring", "summer", "autumn", "winter"]

    if ans_kid == 1:
        kid_list = [True]
    else:
        kid_list = [True,False]


    #-------------task6----------------
    print("Thank you for answering all our questions.")

    recommend_flag = 1
    Score = []
    recommend_list = []
    for destination in Destinations().get_all():
        for i in ans_continent:
            if (continent_list[int(i) - 1] == destination.get_continent()
                    and destination.is_kid_friendly() in kid_list):
                season_factor_list = []
                for j in ans_season:
                    season_factor_list.append(destination.get_season_factor(season_list[int(j) - 1]))
                max_season_factor = max(season_factor_list)
                Score.append(max_season_factor)
                recommend_list.append(destination.get_name())
                print("alternative_destination is:", recommend_list)
                print("alternative_Score is:", Score)
                recommend_flag = 0



    if recommend_flag:
        print("Your next travel destination is None")
    else:
        print("\nThank you for answering all our questions. Your next travel destination is:")
        print(recommend_list[Score.index(max(Score))])
        print("Destination Score is:")
        print(Score[Score.index(max(Score))])




if __name__ == "__main__":
    main()