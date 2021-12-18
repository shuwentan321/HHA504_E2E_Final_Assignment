'''Step 1:Set up and deploy a virtual machine (VM)
1. Using Microsoft Azure, create an account.
2. Selecte Create + Virtual Machine by searching for Virtual Machine service or going to the Azure portal.
3. Complete all configurations such as name, password, and needed preferences for the virtual machine.
4. Review and create the virtual machine.
5. Add the inbound rule for MySQL by adding port 3306 under networking.

Step 2: Connect the virtual machine via terminal and install MySQL on the Ubuntu instance.
1. Using a terminal, enter the following prompt to connect to the vm
"SSH(uername for the instance)@(public ip address for your instance"
-find the IP address on the Azure overview page for the instance.
2. Type in the password created to access the instance.
3. Run the update command 
   "sudo apt-get update"
4. Install MySQL on VM
   "sudo apt install mysql-server mysql-client"
5. To enter MySQL application via the terminal, use:
   "sudo mysql"
6. After entering MySQL, use the command 'show databases;' to review currently available data.

Step 3: Creating a new user for MySQL

1. Create user with the command, "CREATE USER ‘USERNAME'@'%' IDENTIFIED BY ‘PASSWORD’;"
2. To grant this new user privileges,use the command "GRANT ALL PRIVILEGES ON . TO 'USERNAME'@'%' WITH GRANT OPTION;"
  Note: the username is only used for MySQL, should not be the same username created for the instance.
3. Type "mysql -u 'USERNAME' -p" to see if the new user was created successfully. Enter password when prompted.
4. Create a new database by using "create database NAME;" 
  Note: The name for this command will be given to the database that will be located within MySQL
5. Confirm the database was made by using "show databases;" 

Step 4: Load the dataset into the new database using Python'''
##Import needed packages 
from sqlalchemy import create_engine
import sqlalchemy
import pandas as pd 

##Connect to SQL instance 
MYSQL_HOSTNAME = 'IP ADDRESS FOUND ON AZURE PORTAL' 
MYSQL_USER = 'USERNAME'
MYSQL_PASSWORD = 'PASSWORD'
MYSQL_DATABASE = 'DATABASE NAME '

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

##Load the CSV File 
csvfile = pd.read_csv('url link')
csvfile.to_sql('dataset name', con=engine, if_exists ='append') 

'''Step 5: Fix connection error on Terminal
1. Use the command "sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf" to fix configurations for the SQL instance.
2. Update the bind address to 0.0.0.0.
3. Use Ctrl+O to save change and Ctrl+X to exit out the configuration file.
4. Restart MySQL within the VM using "/etc/init.d/mysql restart"
5. Re-run the python file.

Step 6: Check that the dataset has been uploaded successfully, log back into the MySQL with new user.
Using the following commands
    'mysql -u NAMEOFUSER -p
    show databases;
    use NAMEOFDATABASE;
    show tables;'
    
Step 7: Create a 'cold' backup of SQL file
1. Use the command "sudo mysqldump e2e > backup_e2e.sql"
2. Check to confirm the command has been created using 'ls'

Step 8: Using the SCP command from the terminal, move the file to local computer.
1. Use the command
'scp username@ipaddress:/folderlocationoffile/filename.sql ./homecomputer/folderlocation'

Step 9: Create a Trigger for the dataset (specific for this assignment, which is the H1N1_flu_vaccine dataset)

DELIMITER $$
CREATE TRIGGER H1N1_concern_trigger BEFORE INSERT ON e2e.H1N1
FOR EACH ROW
BEGIN 
IF NEW.H1N1_concern <=3 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'H1N1 concern should be a numerical value between 0 and 3. Please try again.'
;END IF;
END; $$
'''

