import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ['rowid', 'pl_name','hostname','pl_letter','hd_name','hip_name','tic_id', 
             'discoverymethod', 'disc_year', 'pl_controv_flag', 'pl_orbeccen', 'pl_rade',
            'st_spectype', 'pl_dens', 'pl_radj', 'pl_massj', 'pl_orbsmax', 'pl_ratdor', 
            'st_rad', 'pl_orbper']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})