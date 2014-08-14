DROP DATABASE IF EXISTS Monitoring;

CREATE DATABASE IF NOT EXISTS Monitoring;

USE Monitoring;


/*
CREATE DATABASE "Monitoring"
  WITH OWNER = lev3_13_1003626d
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'Bulgarian_Bulgaria.1251'
       LC_CTYPE = 'Bulgarian_Bulgaria.1251'
       CONNECTION LIMIT = -1;

COMMENT ON DATABASE "Monitoring"
  IS 'Sea life monitoring database';
*/

/*
	ALL INDEXES
CREATE index Area_ID_Index ON Area(Area_ID);

CREATE index FK_Station_ID_Index ON Event(Station_ID);
CREATE index FK_Area_ID_Index ON Event(Area_ID);
CREATE index FK_Cruise_ID_Index ON Event(Cruise_ID);
CREATE index FK_Notes_ID_Index ON Event(Notes_ID);

CREATE index FK_Event_ID_Index ON Chemistry(Event_ID);
CREATE index FK_Param_ID_Index ON Chemistry(Param_ID);

CREATE index FK_Vessel_ID_Index ON Cruise(Vessel_ID);

CREATE index FK_Type_Spec_Index ON TAXA(Type_Spec);

CREATE index FK_Chem_ID_Index ON DataAB(Chem_ID);
CREATE index FK_TAXA_ID_Index ON DataAB(TAXA_ID);

CREATE index FK_A_B_ID_Index ON SizeAgeFish(A_B_ID);

CREATE index FK_Age_ID_Index ON Age(Age_ID);
CREATE index FK_Size_ID_Index ON Size(Size_ID);
*/

/*------------------------
	Area
--------------------------*/
DROP TABLE IF EXISTS Area ;
CREATE TABLE Area (
	Area_ID	INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Start_Latitude CHAR(9),
	Start_Longitude CHAR(9),
	End_Latitude CHAR(9),
	End_Longitude CHAR(9),
	Start_Date DATE,
	Start_Time TIME,
	End_Date DATE,
	End_Time TIME,
	);
ENGINE = InnoDB;

/*------------------------
	Vessel
--------------------------*/
DROP TABLE IF EXISTS Vessel ;
CREATE TABLE Vessel (
	Vessel_ID	INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Name		VARCHAR(64),
	Captain		VARCHAR(64),
	CSR_Code	VARCHAR(32)
	);
	
ENGINE = InnoDB;

/*------------------------
	Cruise
--------------------------*/
DROP TABLE IF EXISTS Cruise ;
CREATE TABLE Cruise (
	Cruise_ID	INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Vessel_ID	INTEGER NOT NULL,
	Start_Date	DATE,
	End_Date	DATE,
	Objectives	VARCHAR(64),
	FOREIGN KEY (Vessel_ID) REFERENCES Vessel(Vessel_ID) ON DELETE CASCADE
	);
CREATE index FK_Vessel_ID_Index ON Cruise(Vessel_ID);
ENGINE = InnoDB;

/*------------------------
	Notes
--------------------------*/
DROP TABLE IF EXISTS Notes ;
CREATE TABLE Notes (
	Notes_ID	SMALLINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Value		VARCHAR(128)
	);
ENGINE = InnoDB;

/*------------------------
	Stations
--------------------------*/
DROP TABLE IF EXISTS Stations ;
CREATE TABLE Stations (
	Station_ID	INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Notes_ID	SMALLINT,
	Station_Type	VARCHAR(10),
	Station_Code	VARCHAR(20),
	Station_Name_BG	VARCHAR(32),
	Station_Name_LAT	VARCHAR(32),
	Station_Depth	FLOAT,
	Latitude	CHAR(9),
	Longitude	CHAR(9),
	Substrat	VARCHAR(20),
	FOREIGN KEY (Notes_ID) REFERENCES Notes(Notes_ID) ON DELETE CASCADE
	);
ENGINE = InnoDB;

/*------------------------
	TypeSpec
--------------------------*/
DROP TABLE IF EXISTS TypeSpec ;
CREATE TABLE TypeSpec (
	Type_Spec_ID	INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Type		VARCHAR(7),
	BSID		INTEGER
	);
ENGINE = InnoDB;

/*------------------------
	TAXA
--------------------------*/
DROP TABLE IF EXISTS TAXA ;	
CREATE TABLE TAXA (
	Taxa_ID		INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Type_Spec	INTEGER NOT NULL,
	URL		VARCHAR(128),
	Scientific_Name	VARCHAR(64),
	Authority	VARCHAR(64),
	Rank		VARCHAR(64),
	Status		VARCHAR(64),
	Unaccept_reason	VARCHAR(64),
	Valid_APHIA_ID	INTEGER,
	Valid_Name	VARCHAR(64),
	Valid_Authority	VARCHAR(64),
	Kingdom		VARCHAR(64),
	Phylum		VARCHAR(64),
	Class		VARCHAR(64),
	Order_		VARCHAR(64),
	Family		VARCHAR(64),
	Genus		VARCHAR(64),
	Citation	VARCHAR(512),
	LSID		VARCHAR(128),
	Is_Marine	BOOLEAN,
	Is_Brackish	BOOLEAN,
	Is_Freshwater	BOOLEAN,
	Is_Terestrial	BOOLEAN,
	Is_Extinct	BOOLEAN,
	Match_Type	VARCHAR(32),
	Modified	CHAR(20),
	FOREIGN KEY (Type_Spec)	REFERENCES TypeSpec(Type_Spec_ID) ON DELETE CASCADE
	);
CREATE index FK_Type_Spec_Index ON TAXA(Type_Spec);
ENGINE = InnoDB;

/*------------------------
	ChemParam
--------------------------*/
DROP TABLE IF EXISTS ChemParam ;	
CREATE TABLE ChemParam (
	Param_ID	INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Parameter	VARCHAR(10),
	Dimention	VARCHAR(10)
	);
ENGINE = InnoDB;

/*------------------------
	Event
--------------------------*/
DROP TABLE IF EXISTS Event ;	
CREATE TABLE Event (
	Event_ID	INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Station_ID	INTEGER NOT NULL,
	Area_ID		INTEGER NOT NULL,
	Cruise_ID	INTEGER NOT NULL,
	Notes_ID	SMALLINT,
	Institute_Code	VARCHAR(15),
	Collect_Code	VARCHAR(32),
	Gear_Equipment	VARCHAR(20),
	Sample_type	VARCHAR(8),
	Date_Local_Time	DATE,
	Date_UTC	VARCHAR(24),
	Start_Depth	FLOAT,
	End_Depth	FLOAT,
	Operator	VARCHAR(32),
	Post_Operator	VARCHAR(32),
	FOREIGN KEY (Station_ID) REFERENCES Stations(Station_ID) ON DELETE CASCADE,
	FOREIGN KEY (Area_ID) REFERENCES Area(Area_ID) ON DELETE CASCADE,
	FOREIGN KEY (Cruise_ID) REFERENCES Cruise(Cruise_ID) ON DELETE CASCADE,
	FOREIGN KEY (Notes_ID) REFERENCES Notes(Notes_ID) ON DELETE CASCADE
	);
ENGINE = InnoDB;

CREATE index FK_Station_ID_Index ON Event(Station_ID);
CREATE index FK_Area_ID_Index ON Event(Area_ID);
CREATE index FK_Cruise_ID_Index ON Event(Cruise_ID);
CREATE index FK_Notes_ID_Index ON Event(Notes_ID);

/*------------------------
	Chemistry
--------------------------*/
DROP TABLE IF EXISTS Chemistry ;
CREATE TABLE Chemistry (
	Chem_ID		INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Event_ID	INTEGER NOT NULL,
	Param_ID	INTEGER NOT NULL,
	Notes_ID	SMALLINT,
	Param_Value	FLOAT,
	Sample_Validated	BOOLEAN,
	Sample_Number	INTEGER,
	Protocol_Number	INTEGER,
	FOREIGN KEY (Event_ID) REFERENCES Event(Event_ID) ON DELETE CASCADE,
	FOREIGN KEY (Param_ID) REFERENCES ChemParam(Param_ID) ON DELETE CASCADE,
	FOREIGN KEY (Notes_ID) REFERENCES Notes(Notes_ID) ON DELETE CASCADE
	);
ENGINE = InnoDB;

CREATE index FK_Event_ID_Index ON Chemistry(Event_ID);
CREATE index FK_Param_ID_Index ON Chemistry(Param_ID);

/*------------------------
	DataAB
--------------------------*/
DROP TABLE IF EXISTS DataAB ;
CREATE TABLE DataAB (
	A_B_ID		SMALLINT PRIMARY KEY NOT NULL AUTO_INCREMENT,/*Event_ID	VARCHAR(15) NOT NULL,
	eventID becomes redundant as it is present in the table
	Chemistry and its eventID should corespond to the same 
	event as being described in dataAB sample.
	(One could add this field here for ease of access to 
	its data, but this way redundency is introduced.)
	*/
	Chem_ID		INTEGER NOT NULL,
	TAXA_ID		INTEGER NOT NULL,
	Type_Spec_ID	INTEGER NOT NULL,
	Notes_ID	SMALLINT,
	Abundance	INTEGER,
	Abundance_Unit	VARCHAR(15),
	Biomass		FLOAT,
	Biomass_Unit	VARCHAR(15),
	Replica_Unit	INTEGER,
	--*FOREIGN KEY Event_ID REFERENCES Event(Event_ID),*/
	FOREIGN KEY (Chem_ID) REFERENCES Chemistry(Chem_ID) ON DELETE CASCADE,
	FOREIGN KEY (TAXA_ID) REFERENCES TAXA(TAXA_ID) ON DELETE CASCADE,
	FOREIGN KEY (Type_Spec_ID) REFERENCES TypeSpec(Type_Spec_ID) ON DELETE CASCADE,
	FOREIGN KEY (Notes_ID) REFERENCES Notes(Notes_ID) ON DELETE CASCADE
	);
ENGINE = InnoDB;

CREATE index FK_Chem_ID_Index ON DataAB(Chem_ID);
CREATE index FK_TAXA_ID_Index ON DataAB(TAXA_ID);

/*------------------------
	SizeAgeFish
--------------------------*/
DROP TABLE IF EXISTS SizeAgeFish ;
CREATE TABLE SizeAgeFish (
	Size_Age_ID	INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	A_B_ID		SMALLINT,
	FOREIGN KEY (A_B_ID) REFERENCES DataAB(A_B_ID) ON DELETE CASCADE
	);
ENGINE = InnoDB;

CREATE index FK_A_B_ID_Index ON DataAB(A_B_ID);

/*------------------------
	Age
--------------------------*/
DROP TABLE IF EXISTS Age ;
CREATE TABLE Age (
	Age_ID		SMALLINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Size_Age_ID	INTEGER,
	Age_From	FLOAT,
	Age_To		FLOAT,
	Weight		FLOAT,
	FOREIGN KEY (Size_Age_ID) REFERENCES SizeAgeFish(Size_Age_ID) ON DELETE CASCADE
	);
ENGINE = InnoDB;

CREATE index FK_Age_ID_Index ON Age(Age_ID);

/*------------------------
	Size
--------------------------*/
DROP TABLE IF EXISTS `Size` ;
CREATE TABLE `Size` (
	Size_ID		SMALLINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Size_Age_ID	INTEGER,
	Size_From	FLOAT,
	Size_To		FLOAT,
	Weight		FLOAT,
	FOREIGN KEY (Size_Age_ID) REFERENCES SizeAgeFish(Size_Age_ID) ON DELETE CASCADE
	);
ENGINE = InnoDB;

CREATE index FK_Size_ID_Index ON Size(Size_ID);
