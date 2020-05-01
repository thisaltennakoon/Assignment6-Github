import configparser
import hashlib
def hash(password):
    return hashlib.md5(password.encode()).hexdigest()
config = configparser.ConfigParser()

config['Priviladge Levels'] = {'Patient':{'read':['personal details', 'sickness details', 'drug prescriptions', 'lab test prescriptions'],
                                          'write':[]},
                               'Nurse': {'read':['personal details', 'sickness details', 'drug prescriptions', 'lab test prescriptions'],
                                          'write':['personal details']},
                               'MLT': {'read':['personal details', 'sickness details', 'drug prescriptions', 'lab test prescriptions'],
                                          'write':[]},
                               'Pharmacist':{'read':['personal details', 'sickness details', 'drug prescriptions', 'lab test prescriptions'],
                                          'write':[]},
                               'Doctor':{'read':['personal details', 'sickness details', 'drug prescriptions', 'lab test prescriptions'],
                                          'write':['sickness details', 'drug prescriptions', 'lab test prescriptions']},}



config['Users'] = {'Doctor1':{'password': hash('doctor1'),'user type': 'Doctor','privilege level':'doctor'},
                   'Doctor2':{'password': hash('doctor2'),'user type': 'Doctor','privilege level':'doctor'},
                   'Pharmacist1':{'password': hash('pharmacist1'),'user type': 'Pharmacist','privilege level':'pharmacist'},
                   'Pharmacist2':{'password': hash('pharmacist2'),'user type': 'Pharmacist','privilege level':'pharmacist'},
                   'MLT1':{'password': hash('mlt1'),'user type': 'MLT','privilege level':'mlt'},
                   'MLT2':{'password': hash('mlt2'),'user type': 'MLT','privilege level':'mlt'},
                   'Nurse1':{'password': hash('nurse1'),'user type': 'Nurse','privilege level':'nurse'},
                   'Nurse2':{'password': hash('nurse2'),'user type': 'Nurse','privilege level':'nurse'},}


with open('assignment6.ini', 'w') as configfile:
  config.write(configfile)