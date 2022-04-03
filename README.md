# PanCSV-ACO-optimization
Script for PanAIO, optimize the creation of accounts for Zalando ACO with .csv order by Discord user ID

------------------------------------------------------------

# How to configure:

## 1- Add your Pan configuration:

- replace PanAIOblank.json with your own .json export config (rename it 'PanAIOblank.json)

- delete accounts parts with this shape:  

    "aaaaaaaaa": {

    "accounts": [{"email":"email","password":"pswd"},{"email":"email2","password":"pswd2"}],

    "site": "Zalando",

    "name": "a"}
    
- add 'EKIP' (without quotes) instead

## 2- Add your list of Zalando accounts:

- do it the same way as in the example : Discord#XXXX,email,password in PanAioZalando.csv

## Use the script:

- Once you have configured the script files

- Add in listDiscord.csv the list of discord accounts for which you will make ACOs (like in example)

- You can now run the script 

### Warning
do not change file names !
