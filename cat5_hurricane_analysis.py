# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(lst):
    new_lst = []
    for record in lst:
        if record[-1] == "M":
            new_lst.append(float(record[:-1]) * 1000000)
        elif record[-1] == "B":
            new_lst.append(float(record[:-1]) * 1000000000)
        else:
            new_lst.append("Damages not recorded")
    return new_lst

updated_damages = update_damages(damages)
# Checked that it works well

# write your construct hurricane dictionary function here:
def hurricane_dict_creator(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    new_dict = {}
    for hurricane in range(len(names)):
        sub_dict = {}
        sub_dict["Name"] = names[hurricane]
        sub_dict["Month"] = months[hurricane]
        sub_dict["Year"] = years[hurricane]
        sub_dict["Max Sustained Winds"] = max_sustained_winds[hurricane]
        sub_dict["Areas Affected"] = areas_affected[hurricane]
        sub_dict["Damage"] = damages[hurricane]
        sub_dict["Deaths"] = deaths[hurricane]
        new_dict[names[hurricane]] = sub_dict
    return new_dict

# Testing function
hurricane_dict = hurricane_dict_creator(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricane_dict)
# Works!

# write your construct hurricane by year dictionary function here:
def hurricane_by_year_converter(dict):
    new_dict = {}
    hurricane_years = []
    for record in dict.values():
        if not record["Year"] in hurricane_years:
            hurricane_years.append(record["Year"])
    for year in hurricane_years:
        yearly_lst = []
        for record in dict.values():
            if record["Year"] == year:
                yearly_lst.append(record)
        new_dict[year] = yearly_lst
    return new_dict

# Need to account for mutiple hurricanes per year
hurricane_by_year = hurricane_by_year_converter(hurricane_dict)
#print(hurricane_by_year)
# Works!

# write your count affected areas function here:
def count_affected_areas(dict):
    new_dict = {}
    for record in dict.values():
        for item in record["Areas Affected"]:
            if not item in new_dict:
                new_dict[item] = 1
            else:
                new_dict[item] = new_dict[item] + 1
    return new_dict

# Works!
affected_areas_counts = count_affected_areas(hurricane_dict)
# print(affected_areas_counts)


# write your find most affected area function here:
def most_affected_area(dict):
    greatest_num = 0
    most_affected_place = []
    for place in dict.values():
        if place > greatest_num:
            greatest_num = place
    for key, value in dict.items():
        if value == greatest_num:
            most_affected_place.append(key)
    if len(most_affected_place) == 1:
        print("The most affected area is {most_affected_place} having been affected by {greatest_num} hurricanes.".format(most_affected_place=most_affected_place[0], greatest_num=greatest_num))
    else:
        print("The most affected areas are {most_affected_place} having been affected by {greatest_num} hurricanes.".format(most_affected_place=most_affected_place[0], greatest_num=greatest_num))
    return [most_affected_place, greatest_num]

most_affected_area = most_affected_area(affected_areas_counts)

# write your greatest number of deaths function here:
def greatest_num_deaths(dict):
    num_deaths = 0
    for key, value in dict.items():
        if value["Deaths"] > num_deaths:
            num_deaths = value["Deaths"]
            deadliest = key 
        elif value["Deaths"] == num_deaths:
            deadliest = [deadliest, key]
    print("The deadliest hurricane is {deadliest} with {num_deaths} deaths.".format(deadliest=deadliest, num_deaths=num_deaths))
    return [deadliest, num_deaths]

# Testing function
hurr_greatest_deaths = greatest_num_deaths(hurricane_dict)

# write your catgeorize by mortality function here:
def mortality_rating(dict):
    new_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for key, value in dict.items():
        if value["Deaths"] == 0:
            new_dict[0].append(value)
        elif value["Deaths"] <= 100:
            new_dict[1].append(value)
        elif value["Deaths"] <= 500:
            new_dict[2].append(value)
        elif value["Deaths"] <= 1000:
            new_dict[3].append(value)
        elif value["Deaths"] <= 10000:
            new_dict[4].append(value)
        else:
            new_dict[5].append(value)
    return new_dict

# Testing on hurricane_dict
mort_rated = mortality_rating(hurricane_dict)
print(mort_rated)

# write your greatest damage function here:
def greatest_damage(dict):
    largest_damage = 0
    for key, value in dict.items():
        if value["Damage"] == "Damages not recorded":
            continue
        if value["Damage"] > largest_damage:
            most_damaging = key
            largest_damage = value["Damage"]
    print("The most costly hurricane was {most_damaging} which caused {largest_damage} USD of damage.".format(most_damaging=most_damaging, largest_damage=largest_damage))
    return [most_damaging, largest_damage]

# Testing
greatest_damage(hurricane_dict)

# write your catgeorize by damage function here:
def damage_rating(dict):
    new_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for key, value in dict.items():
        if value["Damage"] == "Damages not recorded":
            continue
        elif value["Damage"] == 0:
            new_dict[0].append(value)
        elif value["Damage"] <= 100000000:
            new_dict[1].append(value)
        elif value["Damage"] <= 1000000000:
            new_dict[2].append(value)
        elif value["Damage"] <= 10000000000:
            new_dict[3].append(value)
        elif value["Damage"] <= 50000000000:
            new_dict[4].append(value)
        else:
            new_dict[5].append(value)
    return new_dict

# Testing
damage_rated_hurricanes = damage_rating(hurricane_dict)
print(damage_rated_hurricanes)