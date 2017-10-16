DROP DATABASE deadchannel;
DROP USER deadchannel;
CREATE USER deadchannel WITH PASSWORD 'deadchannel';
CREATE DATABASE deadchannel WITH OWNER deadchannel;
GRANT ALL PRIVILEGES ON DATABASE deadchannel to deadchannel;


