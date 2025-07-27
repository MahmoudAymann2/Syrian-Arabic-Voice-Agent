from tts import synthesize_speech
from stt import transcribe_audio
from intent_detector import detect_intent
from api import submit_order


def handle_user_input(audio_path):
    text = transcribe_audio(audio_path)
    intent, entities = detect_intent(text)

    if intent == "order_food":
        order_response = submit_order({"name": "عميل مجهول", "order": entities})
        response_text = f"تم تسجيل طلبك. رقم الطلب: {order_response['order_id']}. الوقت المتوقع: {order_response['eta']}"
    elif intent == "complaint":
        response_text = "نأسف لسماع هالشي، ممكن نحاول نحل المشكلة سوا؟"
    elif intent == "greeting":
        response_text = "أهلا وسهلا فيك! كيف بقدر ساعدك اليوم؟"
    elif intent == "fallback":
        response_text = "ما فهمت تمام، ممكن تعيد السؤال بطريقة تانية؟"
    else:
        response_text = "شو بتحب تطلب اليوم؟"

    audio_response_path = synthesize_speech(response_text)
    return text, intent, response_text, audio_response_path