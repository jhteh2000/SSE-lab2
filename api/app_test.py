from app import process_query


def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") == "Dinosaurs ruled the Earth 200 \
million years ago"


def test_knows_about_team_name():
    assert process_query("What is your name?") == "Team_team"


def test_knows_about_plus():
    assert process_query("What is 6 plus 9?") == "15"


def test_knows_about_multiplication():
    assert process_query("What is 27 multiplied by 34?") == 918


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"
