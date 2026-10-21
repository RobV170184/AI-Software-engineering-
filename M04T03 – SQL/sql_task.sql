-- ==========================================================
-- HyperionDev  Level 1 AI Engineering
-- M04T03  SQL Task
-- ==========================================================


-- ==================== CREATE TABLES ====================

-- Employee table (pages 7-8)
CREATE TABLE Employee (
    EmployeeID    int          NOT NULL,
    LastName      varchar(255) NOT NULL,
    FirstName     varchar(255),
    Address       varchar(255),
    PhoneNumber   varchar(255),
    PRIMARY KEY (EmployeeID)
);

-- albums table (page 13)
CREATE TABLE albums (
    Artist            varchar(255),
    Album             varchar(255),
    Released          int,
    Genre             varchar(100),
    sales_in_millions decimal(6,2)
);

-- VideoGame table (page 15)
CREATE TABLE VideoGame (
    ID          int          NOT NULL,
    Name        varchar(255),
    DeveloperID int,
    Genre       varchar(100),
    PRIMARY KEY (ID)
);

-- GameDeveloper table (page 15)
CREATE TABLE GameDeveloper (
    ID      int          NOT NULL,
    Name    varchar(255),
    Country varchar(255),
    PRIMARY KEY (ID)
);

-- Customer table (pages 19-20)
CREATE TABLE Customer (
    CustomerID   int          NOT NULL,
    CustomerName varchar(255),
    Address      varchar(255),
    City         varchar(255),
    PRIMARY KEY (CustomerID)
);


-- ==================== INSERT ROWS ====================

-- Insert into Employee: specific columns (method 1, page 9)
INSERT INTO Employee (EmployeeID, LastName, FirstName, Address, PhoneNumber)
VALUES (1234, 'Smith', 'John', '25 Oak Rd', '0837856767');

-- Insert omitting optional columns -- FirstName and Address will be NULL
INSERT INTO Employee (EmployeeID, LastName, PhoneNumber)
VALUES (1321, 'Jones', '0827546787');

-- Insert multiple rows at once (page 10)
INSERT INTO Employee (EmployeeID, LastName, FirstName, Address, PhoneNumber)
VALUES
    (5678, 'Brown',  'Robert', '5 Pine Str',   '0821116789'),
    (9112, 'Davies', 'Emily',  '25 Maple Ave',  '0876543210');

-- Insert into albums: all columns, no column list (method 2, page 10)
INSERT INTO albums
VALUES
    ('Michael Jackson', 'Thriller',                  1982, 'pop',  70),
    ('AC/DC',           'Back in Black',             1980, 'rock', 50),
    ('Pink Floyd',      'The Dark Side of the Moon', 1973, 'rock', 45),
    ('Whitney Houston', 'The Bodyguard',             1992, 'soul', 44);

-- Insert into GameDeveloper
INSERT INTO GameDeveloper (ID, Name, Country)
VALUES
    (1, 'Blizzard', 'USA'),
    (2, 'Nintendo', 'Japan');

-- Insert into VideoGame
INSERT INTO VideoGame (ID, Name, DeveloperID, Genre)
VALUES
    (1, 'Super Mario Bros.',   2, 'platformer'),
    (2, 'World of Warcraft',   1, 'MMORPG'),
    (3, 'The Legend of Zelda', 2, 'adventure');

-- Insert into Customer
INSERT INTO Customer (CustomerID, CustomerName, Address, City)
VALUES
    (1, 'Maria Anderson', '23 York St',     'New York'),
    (2, 'Jackson Peters', '124 River Rd',   'Berlin'),
    (3, 'Thomas Hardy',   '455 Hanover Sq', 'London'),
    (4, 'Kelly Martins',  '55 Loop St',     'Cape Town');


-- ==================== SELECT ====================

-- Select all columns (page 11)
SELECT * FROM Employee;

-- Select specific columns only (page 11)
SELECT FirstName, LastName FROM Employee;

-- ORDER BY descending (page 12)
SELECT * FROM Employee ORDER BY FirstName DESC;

-- ORDER BY ascending on albums
SELECT * FROM albums ORDER BY Released ASC;


-- ==================== WHERE ====================

-- Exact match: employees named John (page 12)
SELECT * FROM Employee WHERE FirstName = 'John';

-- AND + comparison: rock albums with sales <= 50 million (page 13)
SELECT *
FROM albums
WHERE Genre = 'rock' AND sales_in_millions <= 50
ORDER BY Released;

-- IN: pop and soul albums (page 14)
SELECT * FROM albums WHERE Genre IN ('pop', 'soul');

-- BETWEEN: albums released between 1975 and 1985 (page 15)
SELECT COUNT(*) FROM albums WHERE Released BETWEEN 1975 AND 1985;

-- LIKE: artists whose name starts with 'M' (page 14)
SELECT * FROM albums WHERE Artist LIKE 'M%';


-- ==================== AGGREGATE FUNCTIONS ====================

-- MAX: most recent release year (page 14)
SELECT MAX(Released) FROM albums;

-- COUNT with BETWEEN (page 15)
SELECT COUNT(*) FROM albums WHERE Released BETWEEN 1975 AND 1985;

-- SUM with GROUP BY: total sales by genre (page 15)
SELECT Genre, SUM(sales_in_millions) AS total_sales
FROM albums
GROUP BY Genre;


-- ==================== JOIN ====================

-- INNER JOIN: combine VideoGame and GameDeveloper (page 16)
SELECT VideoGame.Name, VideoGame.Genre,
       GameDeveloper.Name, GameDeveloper.Country
FROM VideoGame
INNER JOIN GameDeveloper
ON VideoGame.DeveloperID = GameDeveloper.ID;


-- ==================== ALIASES ====================

-- Column alias (page 18)
SELECT Name AS Developer FROM GameDeveloper;

-- Table aliases in a JOIN (page 18)
SELECT games.Name, games.Genre, devs.Name AS Developer, devs.Country
FROM VideoGame AS games
INNER JOIN GameDeveloper AS devs
ON games.DeveloperID = devs.ID;


-- ==================== WITH / CTE ====================

-- CTE: GameInfo joins VideoGame and GameDeveloper (page 19)
WITH GameInfo AS (
    SELECT games.ID, games.Name AS GameName, games.Genre,
           devs.Name AS Developer
    FROM VideoGame AS games
    INNER JOIN GameDeveloper AS devs
    ON games.DeveloperID = devs.ID
)
SELECT DISTINCT Developer
FROM GameInfo;


-- ==================== UPDATE ====================

-- Update Customer 1 with a new address and city (page 20)
UPDATE Customer
SET Address = '78 Oak St', City = 'Los Angeles'
WHERE CustomerID = 1;


-- ==================== DELETE ====================

-- Delete the customer named Jackson Peters (page 20)
DELETE FROM Customer
WHERE CustomerName = 'Jackson Peters';
