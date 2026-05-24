from jarvis_app.storage.database import initialize


def test_initialize_creates_database(tmp_path):
    db_path = tmp_path / "jarvis.sqlite3"

    created = initialize(db_path)

    assert created == db_path
    assert db_path.exists()

