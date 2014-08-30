To create DB:

mysql -u root -p
CREATE DATABASE SeaLifeMonitoring;
CREATE USER 'gogodi91'@'localhost' IDENTIFIED BY 'gogo159378';
GRANT ALL PRIVILEGES ON SeaLifeMonitoring.* TO 'gogodi91'@'localhost';
quit
