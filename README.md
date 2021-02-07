# rocketbook_automation
Automatically save Rocketbook scans sent to your personal email to your hard drive.  Sort them, and aggregate scans into single pdf files.

This repo has been tested on Ubuntu 20.04.2 LTS and Python 3.8.5.

Description: This tool uses thunderbird mail with the FiltaQuilla extension to save rocketbook scans to a directory of choice.  A cron job then calls sort.py which sorts the rocketbook scans into directories based on their titles.  It then aggregates all scans in one directory into a single file.

Set up:

1) Install FiltaQuilla https://quickfilters.quickfolders.org/filtaquilla.html

2) In Thunderbird, set FiltaQuilla preferences: 'Save Attachments To' and 'Move Later'

3) Set a directory for all notes to be stored in.

4) In thunderbird, create a filter:
    Getting New Mail: Filter before Classification
    
    
    Save Attachments To <path_to_note_directory>
    
5) add PyPDF2 to python3 (pip3 install PyPDF2)

6) In Linux, change the path variable in sort.py to <path_to_note_directory>
 
7) In Linux, move sort.py into the notes directory.  Then set a cronjob to call it (youre preference on time). 
