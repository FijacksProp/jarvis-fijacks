from jarvis_app.storage.database import initialize
from jarvis_app.storage.conversations import ConversationRepository


def test_initialize_creates_database(tmp_path):
    db_path = tmp_path / "jarvis.sqlite3"

    created = initialize(db_path)

    assert created == db_path
    assert db_path.exists()


def test_conversation_repository_round_trip(tmp_path):
    db_path = tmp_path / "jarvis.sqlite3"
    initialize(db_path)
    repository = ConversationRepository(db_path)

    conversation_id = repository.create_conversation("Test Chat")
    repository.add_message(conversation_id, "user", "Hello")
    repository.add_message(conversation_id, "assistant", "Hi")

    conversations = repository.list_conversations()
    messages = repository.get_messages(conversation_id)

    assert conversations[0].title == "Test Chat"
    assert [message.role for message in messages] == ["user", "assistant"]
    assert [message.content for message in messages] == ["Hello", "Hi"]
