'''
Kevin Collura
CS-175L
World Series Winners
'''





def open_file():
    
    worldSeriesWinners = []
    worldSeries = open('WorldSeriesWinners.txt','r')
    
    for team in worldSeries:
        team = team.rstrip('\n')
        worldSeriesWinners.append(team)
    return worldSeriesWinners

def search_file(worldSeriesWinners):
    
    search_team = input("Enter the name of a team: ")
    sublist = [team for team in worldSeriesWinners if search_team.lower() == team.lower()]
    if(len(sublist)==0):
        print("No results found.")
    else:
        print("The", search_team, "won the World Series", len(sublist), "times between 1903 and 2009")


def main():
    
    ask = True
    while ask:
        worldSeriesWinners = open_file()
        search_file(worldSeriesWinners)
        repeat = input("Enter 'q' if you would like to quit: ")
        if repeat.lower() == 'q':
            ask = False
            print("Goodbye!")


    
if __name__ == '__main__':
    main()






































