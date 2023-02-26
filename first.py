import json
import pprint
from collections import OrderedDict
from main import load_json_file

# Plan:
# First, check the data to see if there are any activites that correspond to her listed interests
# Second, check all the programs that she has attended in the past, and recommend something similar 

RECOMMENDED_PROGRAMS = {
  1: {
    #"id": "0d88dc42-7387-4277-a396-8e2aa57fe35c",
    "name": "Forever in Motion Exercise Class ",
    #"start": "2022-04-20T16:30:00.000Z",
    #"end": "2022-04-20T17:30:00.000Z",
    "mode": "RECREATION",
    "dimensions": "Physical",
    "facilitators": "Culinary Team,Resident",
    "hobbies": "Aerobics,Exercise,Weight Training",
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
    #"id": "e7eefdad-a97e-406a-8bae-2494f64ca62e",
    "name": "Interdenominational Bible Study",
    #"start": "2022-04-28T16:00:00.000Z",
    #"end": "2022-04-28T17:00:00.000Z",
    "mode": "RECREATION",
    "dimensions": "Intellectual,Purposeful,Spiritual",
    "facilitators": "Team Member,Resident",
    "hobbies": "Bible Study,Church",
    "levelsOfCare": "Assisted Living,Independent,Long Term Care",
  }
}

def get_resident_by_name(data, given_name):
  residents = data['residents']
  for resident in residents:
    if resident['name'] == given_name:
      return resident

def check_resident_programs_info(data, resident):

  attended_programs_count, total_programs_attended, num_programs_by_hobby = {}, 0, {}
  for program in data['programs']:
    attendees = program['attendees']
    for attendee in attendees:
      if resident['userId'] == attendee['userId']:
        total_programs_attended += 1
        # print(('PROGRAM NAME IS: ' + program['name']), total_programs_attended)
        for hobby in program['hobbies'].split(','):
          num_programs_by_hobby[hobby] = 1 + num_programs_by_hobby.get(hobby, 0)
        if program['name'].strip() not in attended_programs_count.keys():
          attended_programs_count[program['name'].strip()] = (1, program['hobbies'].split(','))
        else:
          attended_programs_count[program['name'].strip()] = (attended_programs_count[program['name'].strip()][0] + 1, program['hobbies'].split(','))
        
  return attended_programs_count, total_programs_attended, num_programs_by_hobby

if __name__ == '__main__':
  my_data = load_json_file("data.json")

  resident_name = 'Darla Blanda'
  resident = get_resident_by_name(my_data, resident_name)
  attended_programs_info, total_programs, num_programs_by_hobby = check_resident_programs_info(my_data, resident)
  # pprint.pprint(OrderedDict(sorted(attended_programs_info.items(), key=lambda item: item[1][0], reverse=True)))
  # pprint.pprint(OrderedDict(sorted(num_programs_by_hobby.items(), key=lambda item: item[1], reverse=True)))
  # print('Total Programs Attended by Resident: ' + str(total_programs))
  pprint.pprint('Recommended Programs for ' + resident_name + ':')
  pprint.pprint(RECOMMENDED_PROGRAMS)
