'''
Create a single (1) system that will recommend programs to be run. It should propose three candidate programs which address one of the following needs:

- Something that Darla Blanda would like
- Engages the highest number of residents
- Engages multiple isolated residents (those who have not been to a program recently)
- Addresses a gap in offerings (lots of interest from residents, but no similar programs planned)
- Addresses a gap in time (a reasonable day and time with few programs offered)

'''
import json
import pprint
from datetime import datetime

# ------------------------------------------------------------------------
# Engages the highest number of residents

def get_hobbies_by_residents(residents):
  hobbies = {}
  for resident in residents:
    if resident['hobbies'] is not None:
      resident_hobbies = resident['hobbies'].split(',')
      for hobby in resident_hobbies:
        hobbies[hobby] = 1 + hobbies.get(hobby, 0)
  
  return dict(sorted(hobbies.items(), key=lambda item: item[1], reverse=True))

# ------------------------------------------------------------------------
# Addresses a gap in offerings (lots of interest from residents, but no similar programs planned)

def get_programs_by_category(data):
  categories = {}
  programs = data['programs']
  for program in programs:
    if program['hobbies'] is not None:
      program_categories = program['hobbies'].split(',')
      for category in program_categories:
        categories[category] = 1 + categories.get(category, 0)

  return dict(sorted(categories.items(), key=lambda item: item[1], reverse=True))

# ------------------------------------------------------------------------
# Engages multiple isolated residents (those who have not been to a program recently)

def get_isolated_residents(data):
  residents = data['residents']
  isolated_resident_ids = [resident['userId'] for resident in residents]

  for program in data['programs']:
    attendees = program['attendees']
    for attendee in attendees:
      if attendee['userId'] in isolated_resident_ids:
        isolated_resident_ids.remove(attendee['userId'])
  
  isolated_residents = []
  for resident in residents:
    if resident['userId'] in isolated_resident_ids:
      isolated_residents.append(resident)

  return isolated_residents

# ------------------------------------------------------------------------

def load_json_file(filepath):
  with open(filepath) as f:
    data = json.load(f)
  return data

def get_resident_by_name(data, given_name):
  residents = data['residents']
  for resident in residents:
    if resident['name'] == given_name:
      return resident

def check_resident_programs_categories(data, resident):

  attended_programs_categories = []
  for program in data['programs']:
    attendees = program['attendees']
    for attendee in attendees:
      if resident['userId'] == attendee['userId']:
        attended_programs_categories += program['hobbies'].split(',')

  return set(attended_programs_categories)

# ------------------------------------------------------------------------

def check_resident_program_compatibility(program, resident):
  # 1. They should not already be an attendee
  # 2. The level of care of the resident should be within the program's 
  # 3. The resident's move in time should be before the program's start time

  resident_movein = datetime.fromisoformat(resident['moveInDate'])
  program_attendees, program_levels, program_starttime = program['attendees'], program['levelsOfCare'].split(','), datetime.fromisoformat(program['start'])

  for attendee in program_attendees:
    if resident['userId'] == attendee['userId']:
      return False
  
  if resident['levelOfCare'] not in program_levels:
    return False
  
  if resident_movein < program_starttime:
    return False

  return True

def get_candidate_programs_by_hobbies(data, resident, limit=3):
  
  # Data is a dictonary of dictionary objects, representing json data of residents
  hobbies, programs = resident['hobbies'].split(','), data['programs']
  candidate_programs = []

  for program in programs:
    program_compatibility = check_resident_program_compatibility(program, resident)
    if program_compatibility:
      program_categories = program['hobbies'].split(',')
      if len(list(set(hobbies) & set(program_categories))) > 0:
        candidate_programs.append((program, 1))
      else:
        candidate_programs.append((program, 0))

  return candidate_programs

# ------------------------------------------------------------------------
if __name__ == '__main__':
  my_data = load_json_file("data.json")

  # 1.
  resident = get_resident_by_name(my_data, 'Darla Blanda')

  resident_programs_categories = check_resident_programs_categories(my_data, resident)
  pprint.pprint(resident_programs_categories)

  residents_hobbies = get_hobbies_by_residents(my_data['residents'])
  print(residents_hobbies)

  isolated_residents = get_isolated_residents(my_data)
  # print(len(isolated_residents))
  isolated_resident_hobbies = get_hobbies_by_residents(isolated_residents)
  print(isolated_resident_hobbies)

  programs_by_category = get_programs_by_category(my_data)
  print(programs_by_category)