import base64
import os
from pathlib import Path
import requests
from django.core.files.storage import Storage
from django.core.exceptions import ImproperlyConfigured

GITHUB_USERNAME = 'dastonsultonov8747'
GITHUB_REPO = 'Kinoteatr_sayt_media'
GITHUB_TOKEN = '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'


class GitHubStorage(Storage):
    GITHUB_API_URL = "https://api.github.com/repos/{username}/{repo}/contents/{file_path}"
    GITHUB_HEADERS = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json",
    }

    def __init__(self, username=None, repo=None):
        self.username = username or GITHUB_USERNAME
        self.repo = (repo or GITHUB_REPO).replace("https://github.com/", "").replace(".git", "")
        if not self.username or not self.repo:
            raise ImproperlyConfigured("GitHub username yoki repo noto'g'ri sozlangan.")

    def _save(self, name, content):
        """Rasmni GitHub repozitoriyasiga yuklash."""
        file_path = f"images/{Path(name).name}"  # Fayl `images` papkasiga yuklanadi
        encoded_content = base64.b64encode(content.read()).decode("utf-8")

        url = self.GITHUB_API_URL.format(username=self.username, repo=self.repo, file_path=file_path)
        data = {
            "message": f"Add {name}",
            "content": encoded_content
        }

        response = requests.put(url, headers=self.GITHUB_HEADERS, json=data)

        if response.status_code == 201:
            # Fayl muvaffaqiyatli yuklandi
            return self._get_file_url(file_path)
        else:
            # Xatolik yuz berdi
            raise Exception(f"Fayl yuklashda xatolik: {response.status_code} - {response.json()}")

    def _get_file_url(self, file_path):
        """GitHub-dan fayl linkini olish."""
        return f"https://raw.githubusercontent.com/{self.username}/{self.repo}/refs/heads/main/{file_path}"

    def url(self, name):
        """Rasm URL'sini qaytarish."""
        return name

    def exists(self, name):
        """Fayl mavjudligini tekshirish."""
        url = self.GITHUB_API_URL.format(username=self.username, repo=self.repo, file_path=f"images/{name}")
        response = requests.get(url, headers=self.GITHUB_HEADERS)
        return response.status_code == 200

    def delete(self, name):
        """Faylni GitHub repozitoriyasidan o‘chirish."""
        file_path = f"images/{name}"
        url = self.GITHUB_API_URL.format(username=self.username, repo=self.repo, file_path=file_path)

        # Faylni yuklab, `sha` (file hash) olish
        get_response = requests.get(url, headers=self.GITHUB_HEADERS)
        if get_response.status_code == 200:
            sha = get_response.json()['sha']

            # Faylni o'chirish uchun API chaqiruvi
            delete_data = {"message": f"Delete {name}", "sha": sha}
            delete_response = requests.delete(url, headers=self.GITHUB_HEADERS, json=delete_data)

            if delete_response.status_code == 200:
                return True
            else:
                raise Exception(f"Faylni o'chirishda xatolik: {delete_response.status_code} - {delete_response.json()}")
        else:
            raise Exception(f"Faylni olishda xatolik: {get_response.status_code} - {get_response.json()}")
