from subsai.main import SubsAI

def translate_subtitle(subtitle, source_language, target_language, model="m2m100", model_family=None, translation_configs={}):
    # Create an instance of SubsAI
    subs_ai = SubsAI()

    # Translate the subtitle
    translated_subtitle = subs_ai.translate(
        subtitle,
        source_language,
        target_language,
        model,
        model_family,
        translation_configs
    )

    return translated_subtitle
