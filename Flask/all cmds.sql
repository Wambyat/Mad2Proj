-- CREATE TABLE venue (
--     id int NOT NULL PRIMARY KEY,
--     name TEXT,
--     address TEXT,
--     style TEXT
-- )

-- INSERT INTO venue VALUES
-- (1, 'The Local hang', '1st Street Bop Town', 'Ya like Jazz?'),
-- (2, 'Buzz Baby', '335 Decency Street', 'Classical Theatre'),
-- (3, 'INOX', 'Random Mall Downtown', 'Movie Hall')

-- CREATE TABLE show (
--     id int NOT NULL PRIMARY KEY,
--     name TEXT,
--     show_date DATE,
--     venue_id int,
--     seats int,
--     seats_booked int,
--     details TEXT,
--     FOREIGN KEY (venue_id) REFERENCES venue(id)
-- )

-- CREATE TABLE ticket (
--     id int NOT NULL PRIMARY KEY,
--     show_id int,
--     user_id int,
--     seats int,
--     FOREIGN KEY (show_id) REFERENCES show(id),
--     FOREIGN KEY (user_id) REFERENCES user(id)
-- )

-- INSERT INTO show VALUES
-- (1, 'Jazz Night', '2023-01-01', 1, 100, 0, 'Jazz Night at the local hang. ft The bee movie'),
-- (2, 'Classical Theatre', '2021-01-02', 2, 100, 0, 'Classical Theatre at Buzz Baby'),
-- (3, 'Movie Night', '2021-01-03', 3, 100, 0, 'Shrek 5')
-- CREATE TABLE show_tags (
--     id int NOT NULL PRIMARY KEY,
--     show_id int,
--     tag_id int,
--     FOREIGN KEY (show_id) REFERENCES show(id),
--     FOREIGN KEY (tag_id) REFERENCES tag(id)
-- )

-- CREATE TABLE tag (
--     id int NOT NULL PRIMARY KEY,
--     name TEXT
-- )

UPDATE show SET seats_booked = 0 WHERE id = 6