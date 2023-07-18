class Config(object):
    def __init__(self):
        self.respuesta = {}

    def cognitive_search(self, question):
        """
        Config cognitive search
        Args: question
        Returns: params
        """
        return {
            "api-version": "2023-07-01-Preview",
            "search": question,
            "queryLanguage": "es-ES",
            "speller": "lexicon",
            # "queryType": "semantic",
            # "captions": "extractive",
            # "answers": "extractive|count-3",
            # "semanticConfiguration": "tpclientconf",
        }

    def openai(self, text):
        """
        Config openai
        Args: text
        Returns: config
        """
        config = {}
        prompt = """busca la información en el texto entregado entre ### ### y
                responde la pregunta de acuerdo al texto"""
        personality = "NOTA: explicaselo a un niño de 10 años"
        instrucciones = f"""
                            Tu papel es ayudar a responder preguntas del siguiente
                            texto.

                            ###
                            {text}
                            ###
                        """
        engine = "gpt-4-32k"
        config["prompt"] = prompt
        config["personality"] = personality
        config["instrucciones"] = instrucciones
        config["engine"] = engine
        config["temperature"] = 0.7

        return config
