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
-- UPDATE show SET seats_booked = 0 WHERE id = 6
-- INSERT INTO tag VALUES
-- (1, 'Jazz'),
-- (2, 'Theatre'),
-- (3, 'Movie'),
-- (4, 'Comedy'),
-- (5, 'Drama'),
-- (6, 'Action'),
-- (7, 'Romance'),
-- (8, 'Thriller'),
-- (9, 'Horror'),
-- (10, 'Sci-Fi')
-- INSERT into show_tags VALUES
-- (1, 1, 1),
-- (2, 1, 2),
-- (3, 2, 2),
-- (4, 2, 5),
-- (5, 3, 3),
-- (6, 3, 4),
-- (7, 3, 7)
-- INSERT into ticket VALUES
-- (1, 1, 2, 2),
-- (2, 1, 2, 1),
-- (3, 2, 3, 4),
-- (4, 3, 3, 19)
-- SELECT a.id, v.name, a.seats, a.name, a.show_date, a.details FROM (SELECT t.id, t.seats, s.name, s.show_date, s.venue_id, s.details FROM ticket t join show s on t.show_id = s.id WHERE t.user_id = 3) a join venue v on a.venue_id = v.id
-- SELECT t.name FROM tag t join show_tags st on t.id = st.tag_id WHERE st.show_id = 3
-- SELECT
--     u.id,
--     u.username,
--     u.password,
--     ud.fname,
--     ud.lname,
--     ud.age,
--     ud.email
-- FROM
--     users u
--     JOIN user_details ud ON u.id = ud.id
-- WHERE
--     u.id = 1



-- SELECT id, show_date FROM show WHERE venue_id = 1

-- SELECT t.id, t.seats FROM ticket t join (SELECT venue_id, id FROM show) vs WHERE t.show_id = vs.id AND vs.venue_id = 1

-- ALTER table ticket ADD COLUMN date_booked DATE NOT NULL DEFAULT '2021-01-01'




-- UPDATE ticket SET date_booked = '2023-09-01' WHERE id = 1

-- SELECT email from user_details WHERE id in (SELECT id FROM users WHERE id not in (SELECT user_id FROM ticket WHERE date_booked > DATE('now','-1 month')) AND id not in (SELECT id FROM admin))

SELECT t.id, s.name, s.show_date, s.seats_booked FROM ticket t join show s WHERE date_booked > DATE('now','-1 month') AND t.show_id = s.id AND user_id = 3