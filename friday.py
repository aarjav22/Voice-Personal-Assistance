from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback,AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator=IAMAuthenticator('T6sNrk4Pj0FOxd1KkOgHPRe8C9xPMHfEXtixbUV0uECU')
stt=SpeechToTextV1(authenticator=authenticator)
stt.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/6986a753-8c88-4e0a-9205-574cfa641ce1')
