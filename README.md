# Requirements

Create a single (1) system that will recommend programs to be run. It should propose three candidate programs which address one of the following needs:

1. Something that Darla Blanda would like
2. Engages the highest number of residents
3. Engages multiple isolated residents (those who have not been to a program recently)
4. Addresses a gap in offerings (lots of interest from residents, but no similar programs planned)
5. Addresses a gap in time (a reasonable day and time with few programs offered)

# How to use

With Python >3.11.0, you can get recommendations for #1 using `python first.py`

# Methodology

My initial plan:

- First, check the data to see if there are any activites that correspond to her listed interests
- Second, check all the programs that she has attended in the past, and recommend something similar

After checking the data, I saw that there were no programs that corresponds to her listed interests, so I chose to create an program that relates to her interests for one of the recommendations. For the other two programs, I did the following:

1. Check all the programs Darla attended in the past
2. Aggregate the categories of each program, find out the categories of her most attended programs
3. Find the programs that correspond to those categories

I found that her top 2 attended programs were `Forever in Motion`, an exercise class, `Entertainment`, a live music event.
Then, I calculated all the other factors for those events, such as average attendees (the actual people), the average length of the program, etc.
To estimate who would attend future programs of the suggested type, I calculated the attendence rate of each of those two events, and put all residents who had >50% attendence rate across all the events that Darla was a part of in the estimate attendees of those suggested programs.
