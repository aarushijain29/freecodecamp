import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    races = df['race'].unique().tolist()
    length = len(races)
    race_dict = {}
    for i in range(length):
      race_dict[races[i]] = len(df.loc[df['race'] == races[i]])
    race_count = pd.Series(race_dict, index = races)
    
    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bach = len(df.loc[df['education'] == 'Bachelors'])
    percentage_bachelors = round((bach/len(df)*100), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    
    higher_education = df.loc[(df['education'] == 'Bachelors') |  (df['education'] == 'Masters') | (df['education'] == 'Doctorate'), ['education', 'salary']]
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    lower_education = df.loc[(df['education'] != 'Bachelors') &  (df['education'] != 'Masters') & (df['education'] != 'Doctorate'), ['education', 'salary']]
    # percentage with salary >50K
    higher_education_rich = round(len(higher_education.loc[higher_education['salary'] == '>50K'])/len(higher_education)*100, 1)
    lower_education_rich = round(len(lower_education.loc[lower_education['salary'] == '>50K'])/len(lower_education)*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]

    rich_percentage = round((len(num_min_workers.loc[num_min_workers['salary'] == '>50K'])/len(num_min_workers)*100), 1)

    # What country has the highest percentage of people that earn >50K?
    country = df['native-country'].unique().tolist()
    len_country = len(country)
    rich_country = df.loc[df['salary'] == '>50K']
    
    highest_earning_country_percentage = 0
    highest_earning_country = ''
    for i in range(len_country):
      total = len(df.loc[df['native-country'] == country[i]])
      perc = len(rich_country.loc[rich_country['native-country'] == country[i]])/total*100
      if perc > highest_earning_country_percentage:
        highest_earning_country_percentage = round(perc, 1)
        highest_earning_country = country[i]
    
    # Identify the most popular occupation for those who earn >50K in India.
    india = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    occ = india['occupation'].unique().tolist()
    count = 0 
    top_IN_occupation = ''
    for i in range(len(occ)):
      if len(india.loc[india['occupation'] == occ[i]]) > count:
        count = len(india.loc[india['occupation'] == occ[i]])
        top_IN_occupation = occ[i]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
