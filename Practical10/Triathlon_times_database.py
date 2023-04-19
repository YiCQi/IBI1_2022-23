# help a local athletic	club store the records for their members’ times	in local triathlon competitions.
class triathlon(object):
    # store the information
    def __init__(self,firstname,lastname,location,swim_time,cycle_time,run_time):
        self.firstname = firstname
        self.lastname = lastname
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = swim_time + cycle_time + run_time
    # print the information
    def print_information(self):
        print('firstname:'+self.firstname,
              'lastname:'+self.lastname,
              'location:'+self.location,
              'swim_time:'+str(self.swim_time)+'min',
              'cycle_time:'+str(self.cycle_time)+'min',
              'run_time:'+str(self.run_time)+'min',
              'total_time:'+str(self.total_time)+'min')

# example
athlete1 = triathlon('San','Zhang','Haining',20,60,30)
athlete1.print_information()