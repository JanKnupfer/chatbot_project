from django.apps import AppConfig
from django.core.cache import cache
from transformers import pipeline

from hugging_face.get_transformer_model_path import get_transformer_model_path


class ChatbotuiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbotUI'

    # Load model in cache right after startup
    def ready(self):
        qas = pipeline(
            model=get_transformer_model_path(),
            task='question-answering'
            )
        cache.set('qa_pipeline', qas)
        print("set Model in cache")
