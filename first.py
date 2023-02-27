import uuid
import pprint
import datetime
from collections import OrderedDict
from main import load_json_file

# Plan:
# First, check the data to see if there are any activites that correspond to her listed interests
# Second, check all the programs that she has attended in the past, and recommend something similar 

# 1. Something that aligns with her interests
# 2. Something that is similar to the programs that she has attended in the past (physically)
# 3. Something that is similar to the programs that she has attended in the past (spiritually/intellectually)

RECOMMENDED_PROGRAMS = {
  1: {
    "id": uuid.uuid4(),
    "name": "Forever in Motion Exercise Class ",
    "start": "2022-07-02T16:30:00.000Z",
    "end": "2022-07-02T17:30:00.000Z",
    "mode": "RECREATION",
    "dimensions": "Physical",
    "facilitators": "Culinary Team,Resident",
    "hobbies": "Aerobics,Exercise,Weight Training",
    "levelsOfCare": "Assisted Living,Independent",
    "attendees": [
      '730f7708-84d0-4c56-8826-a99529e8399a',
      'cb831f8a-cfc7-43fe-b786-faf157bc314b'
      '0877f70d-270a-4bf2-acde-c008f584ed7e'
      'b10f6b5f-dca9-482d-a45b-f0b8966043a1'
      '6de67bdc-6cb8-44a4-8d5c-2bb50166fb8a'
      'd995d9a4-0a1a-4a76-9358-56ea724beae4'
      '22d7e130-9ec9-43cf-bde5-136b721e0f3d'
      '208d8afb-4e80-460f-8b44-f639f6198f79'
      'a9991bf3-d77f-427e-bc6a-a07db57ac653'
      '48032cb9-9310-4a58-bada-bc8d9882a1ee'
      'fb4894f9-3d06-4865-b37e-5ccc484f145a'
      'a4d884db-9401-4733-a5f1-06eb303f4243'
      '233f7edb-bd0c-4e3c-a2e3-141c2c9ab8fe'
      '2a756d71-25b1-40b8-bec6-a8fdba88dd26'
      '46788a70-ab0a-4581-9813-e820217660d7'
      '94f1555e-6b7c-49c0-8c89-40ce94116da0'
      'fa42d0f3-1738-4673-99e5-5031870cad9c'
      'e7bcb474-0ec2-45e5-b82d-abe76380ae4c'
      'f8bf9534-7f9b-4d0b-b99e-c78e53773b90'
      'd341bae9-6625-496f-828b-77b9660b7216'
      'da22be77-b155-4309-b247-2e6132868c92'
      'b002165d-7a8b-49a6-994e-6b6015b03d0b'
      '67d552f4-9b1d-407b-b47e-3bedc56ec06d'
      '3b7e2f8c-25bf-4b22-9455-c57e7c9fed7f'
    ]
  },
  2: {
    "id": uuid.uuid4(),
    "name": "Entertainment",
    "start": "2022-07-02T01:00:00.000Z",
    "end": "2022-04-27T02:00:00.000Z",
    "mode": "RECREATION",
    "dimensions": "Sensory,Spiritual",
    "facilitators": "Team Member,Culinary Team",
    "hobbies": "Entertaining,Music,Music therapy,Singing",
    "levelsOfCare": "Assisted Living,Independent,Long Term Care,Memory Care",
    "attendees": [
      '48032cb9-9310-4a58-bada-bc8d9882a1ee'
      'b002165d-7a8b-49a6-994e-6b6015b03d0b'
      '1b1cb065-c668-4d6a-9963-7c334cae0047'
      'cdbc0c71-fb6d-49d4-868f-c97ea07ab40c'
      'a7174ea9-2920-478a-95f5-df402b2c8abc'
      '31462c60-15e2-439c-a73d-d8be3929d2ef'
      '2c21c613-90e1-4a6a-a0e3-71000bad2b1c'
      'c001a6e2-67b5-4bc4-b3b4-38e127f7b826'
      '233f7edb-bd0c-4e3c-a2e3-141c2c9ab8fe'
      'ef44cbe6-b35f-45c1-944d-487b49e98402'
      '27e1cd51-d15f-4f24-b689-266af6e00a11'
      '0a82c5fb-5424-4764-a848-415396b17d24'
      '6fbb8b9c-4c36-468f-93ec-efa278da0126'
      '486179c7-b0fb-421a-af8e-0d958f20ca1c'
      '46788a70-ab0a-4581-9813-e820217660d7'
      'e7bcb474-0ec2-45e5-b82d-abe76380ae4c'
      '1c261413-89fe-43e6-ae02-566d97ccf8b3'
      'c323e075-ccbd-4b5f-bf4c-bb910e46efca'
      '24edd52d-d1c9-425f-b051-70edc2d5d219'
      '8d2d53b1-eb51-4fce-93a3-f013c10c2902'
      '1948372d-372b-4d27-aca6-dc065a3e68da'
      'b8b49d05-4e79-41e2-a5fb-9f6aef3a4f2d'
      '03e43226-dec3-4140-90e9-3d7837bac232'
      'c16074ff-3fe0-4185-96d5-0328fbd7d765'
      '0eca3e45-33b4-49bf-9114-baf50d41ca25'
      '3b7e2f8c-25bf-4b22-9455-c57e7c9fed7f'
      '2a756d71-25b1-40b8-bec6-a8fdba88dd26'
      'f1ac0c0a-4f7a-43ac-b426-5885b7213009'
      '3afcd7df-0f80-4cc3-92c8-119852d4bfbd'
      '86077fa5-0792-4a40-a28e-03899c8bceaa'
      '30212d3f-448f-435a-a7e1-e1b452cca8c6'
      '3a0b9d19-b093-4742-86a9-23f183ce14da'
      'c6199c0c-04ed-45c7-b937-b1482a62f30c'
      'bf3cddaf-e221-4b5c-9485-65b5ab04fcd6'
      '730f7708-84d0-4c56-8826-a99529e8399a'
      '9cf224c0-569d-4c95-8071-a7ee54fed3f7'
      '8eea3d0e-8a86-4834-8881-e4d2645ac541'
      'd995d9a4-0a1a-4a76-9358-56ea724beae4'
      'b1935535-8174-40c7-a0d3-c3f910cbe5d8'
      '9e3c5d3c-57a2-4377-b5cf-78f0b754dd87'
      'cbfc2fcf-9483-4331-a031-010d1787f381'
      '2b64a8a7-3b00-41b9-bfdd-80492d9124f3'
      '30701928-2b1d-4618-8a65-11c9ca21b8b6'
    ]
  },
  3: {
    "id": uuid.uuid4(),
    "name": "Collector Enthusiast Meetup",
    "start": "2022-07-02T16:00:00.000Z",
    "end": "2022-07-02T17:00:00.000Z",
    "mode": "RECREATION",
    "dimensions": "Intellectual,Purposeful,Spiritual",
    "facilitators": "Team Member,Resident",
    "hobbies": "Card Collecting, Collecting",
    "levelsOfCare": "Assisted Living,Independent",
    "attendees": [
      '391ddee7-aa30-455c-81db-190f5d6b66ab',
      '233f7edb-bd0c-4e3c-a2e3-141c2c9ab8fe'
    ]
  }
}

def get_resident_by_name(data, given_name):
  residents = data['residents']
  for resident in residents:
    if resident['name'] == given_name:
      return resident

def get_program_data_averages_for_resident(data, hobbies, resident):
  # [0] is avg, [1] is total occurences
  program_data = {
    'sessions': 0,
    'duration': 0,
    'num_attendees': 0,
    'attendees': {}
  }
  programs = data['programs']
  for program in programs:
    if program['hobbies'] is not None and program['hobbies'].split(',') == hobbies:
      attendees = program['attendees']
      for attendee in attendees:
        if resident['userId'] == attendee['userId']:
          program_data['duration'] += (datetime.datetime.fromisoformat(program['end']) - datetime.datetime.fromisoformat(program['start'])).total_seconds() / 60
          program_data['num_attendees'] += len(program['attendees'])
          program_data['sessions'] += 1
        program_data['attendees'][attendee['userId']] = 1 + program_data['attendees'].get(attendee['userId'], 0)
    
  program_data['duration_avg'] = program_data['duration'] / program_data['sessions']
  program_data['num_attendees_avg'] = program_data['num_attendees'] / program_data['sessions']
  program_data['attendees'] = OrderedDict(sorted(program_data['attendees'].items(), key=lambda item: item[1], reverse=True))

  return program_data

def check_resident_programs_info(data, resident):

  attended_programs_count, total_programs_attended, num_programs_by_hobby = {}, 0, {}
  for program in data['programs']:
    attendees = program['attendees']
    for attendee in attendees:
      if resident['userId'] == attendee['userId']:
        total_programs_attended += 1
        for hobby in program['hobbies'].split(','):
          num_programs_by_hobby[hobby] = 1 + num_programs_by_hobby.get(hobby, 0)
        if program['name'].strip() not in attended_programs_count.keys():
          attended_programs_count[program['name'].strip()] = (1, program['hobbies'].split(','))
        else:
          attended_programs_count[program['name'].strip()] = (attended_programs_count[program['name'].strip()][0] + 1, program['hobbies'].split(','))
        
  return OrderedDict(sorted(attended_programs_count.items(), key=lambda item: item[1][0], reverse=True)), total_programs_attended, OrderedDict(sorted(num_programs_by_hobby.items(), key=lambda item: item[1], reverse=True))
  

if __name__ == '__main__':
  my_data = load_json_file("data.json")

  resident_name = 'Darla Blanda'
  resident = get_resident_by_name(my_data, resident_name)
  # avgs = get_program_data_averages_for_resident(my_data, ['Aerobics', 'Exercise', 'Weight Training'], resident)
  # avgs = get_program_data_averages_for_resident(my_data, ['Live music', 'Singing'], resident)
  # pprint.pprint(avgs)
  # attended_programs_info, total_programs, num_programs_by_hobby = check_resident_programs_info(my_data, resident)
  # pprint.pprint(OrderedDict(sorted(attended_programs_info.items(), key=lambda item: item[1][0], reverse=True)))
  # pprint.pprint(OrderedDict(sorted(num_programs_by_hobby.items(), key=lambda item: item[1], reverse=True)))
  # # print('Total Programs Attended by Resident: ' + str(total_programs))
  # pprint.pprint('Recommended Programs for ' + resident_name + ':')
  # pprint.pprint(RECOMMENDED_PROGRAMS)
