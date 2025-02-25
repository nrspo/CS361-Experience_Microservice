-- Data Definitions for CS361 Course Project by Nathan Spoerle

SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

DROP TABLE IF EXISTS Experiences;

CREATE OR REPLACE TABLE Experiences (
    experienceID INT NOT NULL AUTO_INCREMENT,
    rating INT NOT NULL -- value 1-5, validated front end
    details VARCHAR(255) NULL
    image VARCHAR(255) NULL # holds an image address
    userID INT NOT NULL # FK from Users table 
    PRIMARY KEY(experienceID)
);

