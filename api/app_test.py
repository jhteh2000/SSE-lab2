from app import process_query


def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") == "Dinosaurs ruled the Earth 200 \
million years ago"


def test_knows_about_team_name():
    assert process_query("What is your name?") == "Team_team"


def test_knows_about_plus():
    assert process_query("What is 6 plus 9?") == "15"


def test_knows_about_minus():
    assert process_query("What is 9 minus 4?") == "5"


def test_knows_about_multiplication():
    assert process_query("What is 27 multiplied by 34?") == "918"


def test_knows_about_largest():
    assert process_query("Which of the following numbers\
                          is the largest: 68, 78, 40?") == "78"


def test_knows_about_cube_and_sqr():
    assert process_query("Which of the following numbers is both a square and\
                          a cube: 2304, 1324, 4702, 729, 64, 8, 1?") == \
                            "729, 64, 1"


def test_knows_about_prime():
    assert process_query("Which of the following numbers are primes: \
                         66, 35, 74, 42, 43, 7?") == "43, 7"


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"
