-- Task 1: Schema Design
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    available BOOLEAN
);

CREATE TABLE Members (
    member_id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE Loans (
    loan_id INT PRIMARY KEY,
    book_id INT,
    member_id INT,
    loan_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

-- Task 2: Insert Data
INSERT INTO Books VALUES (1, 'The Alchemist', 'Paulo Coelho', TRUE);
INSERT INTO Books VALUES (2, '1984', 'George Orwell', TRUE);
INSERT INTO Books VALUES (3, 'Sapiens', 'Yuval Noah Harari', TRUE);

INSERT INTO Members VALUES (1, 'Alice', 'alice@example.com');
INSERT INTO Members VALUES (2, 'Bob', 'bob@example.com');
INSERT INTO Members VALUES (3, 'Charlie', 'charlie@example.com');

INSERT INTO Loans VALUES (1, 1, 1, '2025-05-01');
INSERT INTO Loans VALUES (2, 2, 2, '2025-05-03');
INSERT INTO Loans VALUES (3, 3, 3, '2025-05-05');

-- Task 3: Books borrowed by a specific member
SELECT Books.title 
FROM Loans
JOIN Books ON Loans.book_id = Books.book_id
WHERE Loans.member_id = 1;

-- Task 4: Update/ Delete
UPDATE Books SET available = FALSE WHERE book_id = 1;
DELETE FROM Members WHERE member_id = 3;
