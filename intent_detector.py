import re

def detect_intent(text):
    if any(word in text for word in ["طلب", "أطلب", "فروج"]):
        return "order_food", ["فروج"]
    elif "شكوى" in text or "مشكلة" in text:
        return "complaint", {}
    elif any(greet in text for greet in ["مرحبا", "أهلا"]):
        return "greeting", {}
    else:
        return "fallback", {}
