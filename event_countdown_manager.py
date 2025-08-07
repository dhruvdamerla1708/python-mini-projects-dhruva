#Event Countdown Manager
import datetime
import json
import os
def add_event():
  event_name=input('Enter event name: ')
  event_date=input('Enter event date (YYYY-MM-DD): ')
  event_datetime=datetime.datetime.strptime(event_date,'%Y-%m-%d')
  event={'name':event_name,'date':event_date,'datetime':event_datetime}
  if os.path.exists('events.json'):
    with open('events.json','r') as f:
      events=json.load(f)
  else:
    events=[]
  events.append(event)
  with open('events.json','w',newline='') as f:
    json.dump(events,f,indent=2)
  print('Event added successfully!')
def view_events():
  if os.path.exists('events.json'):
    with open('events.json','r') as f:
      events=json.load(f)
    if events:
      print('Upcoming Events:')
      for event in events:
        event_datetime=datetime.datetime.strptime(event['date'],'%Y-%m-%d')
        countdown=event_datetime-datetime.datetime.now()
        print(f"{event['name']} - {countdown.days} days left")
    else:
      print('No events found.')
def main():
  while True:
    print('===== Event Countdown Manager =====\n1.Add an Event\n2.View Events\n3.Exit')
    op=int(input('Enter your choice: '))
    match op:
      case 1:
        add_event()
      case 2:
        view_events()
      case 3:
        print('Thank you for using Event Countdown Manager!')
        exit()
      case _:
        print('Invalid choice. Please try again.')
main()
