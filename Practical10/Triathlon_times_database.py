# help a local athletic	club store the records for their members’ times	in local triathlon competitions.
class triathlon(object):
    def __init__(self,firstname,lastname,location,swim_time,cycle_time,run_time,total_time):
        self.firstname = firstname
        self.lastname = lastname
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = total_time

# example
athlete1 = triathlon('San','Zhang','Haining','20min','1h','30min','1h50min')
print(athlete1.firstname,
      athlete1.lastname,
      athlete1.location,
      athlete1.swim_time,
      athlete1.cycle_time,
      athlete1.run_time,
      athlete1.total_time)