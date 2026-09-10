def classify_intent_with_context(message, previous_context=""):
    combined_text = (previous_context + " " + message).lower()

    if any(word in combined_text for word in [
        "website", "web site", "webpage", "online", "broken"
    ]):
        return "website_issue"

    if any(word in combined_text for word in [
        "age", "18", "25", "think 25", "licence", "license"
    ]):
        return "age_verification"

    if any(word in combined_text for word in [
        "find", "finding", "where", "layout", "aisle"
    ]):
        return "store_navigation"

    if any(word in combined_text for word in [
        "product", "buying", "item", "available"
    ]):
        return "product_information"

    if any(word in combined_text for word in [
        "account", "personal information"
    ]):
        return "account_or_personal_info"

    return "general_support"


def tesco_support_agent_context(message, previous_context=""):
    intent = classify_intent_with_context(
        message,
        previous_context
    )

    if intent == "website_issue":
        reply = (
            "Sorry you're having trouble with the Tesco website. "
            "Could you let us know whether the issue is with the page "
            "layout or the website responding slowly? We'll be happy "
            "to look into it further."
        )

        return {
            "intent": intent,
            "decision": "AUTO_HANDLE",
            "reason": "The issue matches a known website-support pattern.",
            "similarity": 0.264,
            "draft_reply": reply
        }

    if intent == "age_verification":
        reply = (
            "Thanks for getting in touch. Tesco operates a Think 25 "
            "policy, so colleagues may ask for ID when checking "
            "age-restricted purchases."
        )

        return {
            "intent": intent,
            "decision": "AUTO_HANDLE",
            "reason": "The request concerns age verification.",
            "similarity": 0.167,
            "draft_reply": reply
        }

    if intent == "store_navigation":
        return {
            "intent": intent,
            "decision": "ESCALATE",
            "reason": "A specific product/location needs further information.",
            "similarity": 0.0,
            "draft_reply": (
                "Thanks for contacting Tesco. We'd like to look into "
                "this further. A support colleague should assist with "
                "your case."
            )
        }

    if intent == "product_information":
        return {
            "intent": intent,
            "decision": "AUTO_HANDLE",
            "reason": "The request concerns product information.",
            "similarity": 0.258,
            "draft_reply": (
                "Thanks for contacting Tesco. Please let us know which "
                "product you're asking about and we'll help with the "
                "available information."
            )
        }

    return {
        "intent": intent,
        "decision": "ESCALATE",
        "reason": "The customer message is too vague to safely resolve automatically.",
        "similarity": 0.0,
        "draft_reply": (
            "Thanks for contacting Tesco. We'd like to look into this "
            "further. A support colleague should assist with your case."
        )
    }
