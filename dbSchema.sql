CREATE DATABASE IF NOT EXISTS inf19;

CREATE TABLE IF NOT EXISTS discord_users(

user_id bigint not null unique primary key ,
username varchar(33) not null ,
discriminator varchar(4) not null,
user_nick varchar(33)

);


GRANT SELECT, INSERT, UPDATE ON discord_users TO testbot;


CREATE TABLE IF NOT EXISTS ping_score(

userID
score
userName
userNumber
userNickname

);