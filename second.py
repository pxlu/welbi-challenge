# Plan:
# First, check the data to see what are the interests of the residents aggregated
# Second, for the top 3 interests across all the residents listed, recommend a program for each of those interests, as long as they don't overlap
# Third, check the most attended programs previously and recommend something similar to the top attended program

import pprint
import operator
from main import load_json_file

RECOMMENDED_PROGRAMS = {
  1: {
    #"id": "d1c3ef3a-1396-470a-8ac5-518cda34f6f7",
    "name": "Book Club",
    #"start": "2022-06-21T16:00:00.000Z",
    #"end": "2022-06-21T17:00:00.000Z",
    "mode": "RECREATION",
    "dimensions": "Intellectual",
    "facilitators": "Sales & Marketing,Culinary Team",
    "hobbies": "Book club,Reading,Socializing",
    "levelsOfCare": "Assisted Living,Independent",
  },
  2: {
    #"id": "19fee0ad-e169-4ee2-850f-7880db148d59",
    "name": "Entertainment",
    #"start": "2022-04-27T01:00:00.000Z",
    #"end": "2022-04-27T02:00:00.000Z",
    "mode": "RECREATION",
    "dimensions": "Sensory,Spiritual",
    "facilitators": "Team Member,Culinary Team",
    "hobbies": "Entertaining,Music,Music therapy,Singing",
    "levelsOfCare": "Assisted Living,Independent,Long Term Care,Memory Care",
  },
  3: {
    #"id": "8cc647da-ef4a-42fc-a902-2e58079611f4",
    "name": "Living Loving Local Dinner",
    #"start": "2022-06-03T22:30:00.000Z",
    #"end": "2022-06-03T23:30:00.000Z",
    "mode": "RECREATION",
    "dimensions": "Purposeful",
    "facilitators": "Contractor,Team Member",
    "hobbies": "Eating,Food",
    "levelsOfCare": "Assisted Living,Independent,Long Term Care,Memory Care",
  },
  4: {
    #"id": "b91e6738-4aa1-4aeb-b678-47fe642e282d",
    "name": "Happy Hour",
    #"start": "2022-06-16T21:00:00.000Z",
    #"end": "2022-06-16T22:00:00.000Z",
    "mode": "RECREATION",
    "dimensions": "Social",
    "facilitators": "Culinary Team,Volunteer",
    "hobbies": "Bartending,Eating,Socializing",
    "levelsOfCare": "Assisted Living,Independent,Long Term Care",
  }
}

def get_hobbies_by_residents(residents):
  hobbies = {}
  for resident in residents:
    if resident['hobbies'] is not None:
      resident_hobbies = resident['hobbies'].split(',')
      for hobby in resident_hobbies:
        hobbies[hobby] = 1 + hobbies.get(hobby, 0)
  
  return sorted(hobbies.items(), key=lambda item: item[1], reverse=True)

def get_care_status_by_resident(residents):

  care_statuses = {}
  for resident in residents:
    if resident['levelOfCare'] is not None:
      care_statuses[resident['levelOfCare'].strip()] = 1 + care_statuses.get(resident['levelOfCare'].strip(), 0)

  return sorted(care_statuses.items(), key=lambda item: item[1], reverse=True)

def get_partipation_by_program(programs):

  program_partipation_count = []
  for program in programs:
    program_partipation_count.append((program['name'], len(program['attendees'])))

  return sorted(program_partipation_count, key=lambda item: item[1], reverse=True)[:20]

if __name__ == '__main__':
  my_data = load_json_file("data.json")

  resident_hobbies = get_hobbies_by_residents(my_data['residents'])
  resident_care_statuses = get_care_status_by_resident(my_data['residents'])
  program_partipation_count = get_partipation_by_program(my_data['programs'])
  # pprint.pprint(resident_hobbies)
  # pprint.pprint(resident_care_statuses)
  # pprint.pprint(program_partipation_count)

  pprint.pprint('Recommended Programs for Highest Resident Engagement')
  pprint.pprint(RECOMMENDED_PROGRAMS)