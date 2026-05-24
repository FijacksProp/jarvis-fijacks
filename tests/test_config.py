from jarvis_app.config import AppConfig, FavoriteApp, FavoriteFolder


def test_config_load_accepts_utf8_bom(tmp_path):
    config_path = tmp_path / "config.json"
    config_path.write_text(
        """
{
  "ollama_base_url": "http://localhost:11434",
  "default_model": "llama3.2:3b",
  "data_dir": "E:/Jarvis/JarvisData",
  "output_dir": "E:/Jarvis/JarvisData/outputs",
  "favorite_apps": [],
  "favorite_folders": []
}
""".lstrip(),
        encoding="utf-8-sig",
    )

    config = AppConfig.load(config_path)

    assert config.default_model == "llama3.2:3b"


def test_config_save_round_trips_favorites(tmp_path):
    config_path = tmp_path / "config.json"
    config = AppConfig(
        default_model="llama3.2:3b",
        data_dir=str(tmp_path),
        output_dir=str(tmp_path / "outputs"),
        favorite_apps=[FavoriteApp("Editor", "C:/Tools/editor.exe")],
        favorite_folders=[FavoriteFolder("Projects", "E:/Projects")],
    )

    config.save(config_path)
    loaded = AppConfig.load(config_path)

    assert loaded.favorite_apps[0].name == "Editor"
    assert loaded.favorite_apps[0].path == "C:/Tools/editor.exe"
    assert loaded.favorite_folders[0].name == "Projects"
    assert loaded.favorite_folders[0].path == "E:/Projects"
