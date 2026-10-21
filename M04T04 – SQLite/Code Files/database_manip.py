import sqlite3

try:
    db = sqlite3.connect('python_programming.db')
    cursor = db.cursor()

    # Create the python_programming table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS python_programming (
            id    INTEGER PRIMARY KEY,
            name  TEXT,
            grade INTEGER
        )
    ''')
    db.commit()

    # Insert the required rows using prepared statements
    students = [
        (55, 'Carl Davis',         61),
        (66, 'Dennis Fredrickson', 88),
        (77, 'Jane Richards',      78),
        (12, 'Peyton Sawyer',      45),
        (2,  'Lucas Brooke',       99),
    ]
    cursor.executemany(
        'INSERT INTO python_programming (id, name, grade) VALUES (?, ?, ?)',
        students
    )
    db.commit()
    print('Rows inserted successfully.')

    # Select all records with a grade between 60 and 80
    cursor.execute(
        'SELECT * FROM python_programming WHERE grade BETWEEN ? AND ?',
        (60, 80)
    )
    print('\nStudents with grade between 60 and 80:')
    for row in cursor.fetchall():
        print(f'  {row}')

    # Change Carl Davis's grade to 65
    cursor.execute(
        'UPDATE python_programming SET grade = ? WHERE name = ?',
        (65, 'Carl Davis')
    )
    db.commit()
    print("\nCarl Davis's grade updated to 65.")

    # Delete Dennis Fredrickson's row
    cursor.execute(
        'DELETE FROM python_programming WHERE name = ?',
        ('Dennis Fredrickson',)
    )
    db.commit()
    print("Dennis Fredrickson's row deleted.")

    # Change the grade of all students with an id greater than 55 to 80
    cursor.execute(
        'UPDATE python_programming SET grade = ? WHERE id > ?',
        (80, 55)
    )
    db.commit()
    print('Grade set to 80 for all students with id > 55.')

    # Display the final state of the table
    cursor.execute('SELECT * FROM python_programming')
    print('\nFinal table:')
    for row in cursor.fetchall():
        print(f'  {row}')

except Exception as e:
    db.rollback()
    raise e
finally:
    db.close()
