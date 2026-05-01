"""
Internationalization (i18n) — Hindi + English bilingual support.

All user-facing strings are defined here so the UI can switch languages
without touching component code.
"""

from __future__ import annotations

_STRINGS: dict[str, dict[str, str]] = {
    # ── Navigation & Global ──────────────────────────────────────────
    "app_title": {
        "en": "🗳️ BharatVote Guide",
        "hi": "🗳️ भारतवोट गाइड",
    },
    "app_subtitle": {
        "en": "Your complete guide to Indian elections",
        "hi": "भारतीय चुनावों की आपकी संपूर्ण मार्गदर्शिका",
    },
    "nav_home": {"en": "🏠 Home", "hi": "🏠 होम"},
    "nav_timeline": {"en": "📅 Election Timeline", "hi": "📅 चुनाव समयरेखा"},
    "nav_wizard": {"en": "🧭 Step-by-Step Guide", "hi": "🧭 चरण-दर-चरण मार्गदर्शिका"},
    "nav_quiz": {"en": "📝 Test Your Knowledge", "hi": "📝 अपना ज्ञान परखें"},
    "nav_faq": {"en": "❓ FAQ", "hi": "❓ अक्सर पूछे जाने वाले प्रश्न"},
    "nav_states": {"en": "🗺️ State Info", "hi": "🗺️ राज्य की जानकारी"},
    "nav_ask_ai": {"en": "🤖 Ask AI", "hi": "🤖 AI से पूछें"},

    # ── Home ─────────────────────────────────────────────────────────
    "home_hero_title": {
        "en": "Understand Indian Elections",
        "hi": "भारतीय चुनावों को समझें",
    },
    "home_hero_subtitle": {
        "en": "Learn every step of the democratic process — from voter registration to counting day.",
        "hi": "मतदाता पंजीकरण से लेकर मतगणना दिवस तक — लोकतांत्रिक प्रक्रिया के हर चरण को जानें।",
    },
    "home_card_timeline": {
        "en": "Interactive Timeline",
        "hi": "इंटरैक्टिव समयरेखा",
    },
    "home_card_timeline_desc": {
        "en": "Visualise the entire election journey from announcement to results.",
        "hi": "घोषणा से परिणाम तक पूरी चुनाव यात्रा को देखें।",
    },
    "home_card_wizard": {
        "en": "Step-by-Step Guide",
        "hi": "चरण-दर-चरण मार्गदर्शिका",
    },
    "home_card_wizard_desc": {
        "en": "Walk through voter registration, nomination, campaigning, voting, and counting.",
        "hi": "मतदाता पंजीकरण, नामांकन, प्रचार, मतदान और मतगणना के बारे में जानें।",
    },
    "home_card_quiz": {
        "en": "Election Quiz",
        "hi": "चुनाव क्विज़",
    },
    "home_card_quiz_desc": {
        "en": "Test how well you know the Indian election process.",
        "hi": "जाँचें कि आप भारतीय चुनाव प्रक्रिया को कितना जानते हैं।",
    },
    "home_card_ai": {
        "en": "Ask AI Assistant",
        "hi": "AI सहायक से पूछें",
    },
    "home_card_ai_desc": {
        "en": "Get instant, personalised answers powered by Google Gemini.",
        "hi": "Google Gemini द्वारा संचालित तुरंत, व्यक्तिगत उत्तर प्राप्त करें।",
    },

    # ── Timeline ─────────────────────────────────────────────────────
    "timeline_title": {
        "en": "📅 Election Timeline",
        "hi": "📅 चुनाव समयरेखा",
    },
    "timeline_subtitle": {
        "en": "Follow the journey of an Indian General Election from start to finish.",
        "hi": "भारतीय आम चुनाव की शुरुआत से अंत तक की यात्रा का अनुसरण करें।",
    },

    # ── Wizard ───────────────────────────────────────────────────────
    "wizard_title": {
        "en": "🧭 Step-by-Step Election Guide",
        "hi": "🧭 चरण-दर-चरण चुनाव मार्गदर्शिका",
    },
    "wizard_next": {"en": "Next →", "hi": "अगला →"},
    "wizard_prev": {"en": "← Previous", "hi": "← पिछला"},
    "wizard_step": {"en": "Step", "hi": "चरण"},

    # ── Quiz ─────────────────────────────────────────────────────────
    "quiz_title": {
        "en": "📝 Election Knowledge Quiz",
        "hi": "📝 चुनाव ज्ञान क्विज़",
    },
    "quiz_start": {"en": "Start Quiz", "hi": "क्विज़ शुरू करें"},
    "quiz_submit": {"en": "Submit Answer", "hi": "उत्तर जमा करें"},
    "quiz_next": {"en": "Next Question", "hi": "अगला प्रश्न"},
    "quiz_score": {"en": "Your Score", "hi": "आपका स्कोर"},
    "quiz_correct": {"en": "✅ Correct!", "hi": "✅ सही!"},
    "quiz_wrong": {"en": "❌ Incorrect", "hi": "❌ गलत"},
    "quiz_restart": {"en": "Restart Quiz", "hi": "क्विज़ पुनः आरंभ करें"},
    "quiz_question": {"en": "Question", "hi": "प्रश्न"},

    # ── FAQ ───────────────────────────────────────────────────────────
    "faq_title": {
        "en": "❓ Frequently Asked Questions",
        "hi": "❓ अक्सर पूछे जाने वाले प्रश्न",
    },

    # ── State Info ───────────────────────────────────────────────────
    "state_title": {
        "en": "🗺️ State-Specific Election Info",
        "hi": "🗺️ राज्य-विशिष्ट चुनाव जानकारी",
    },
    "state_select": {"en": "Select a State / UT", "hi": "एक राज्य / केंद्र शासित प्रदेश चुनें"},

    # ── AI Chat ──────────────────────────────────────────────────────
    "ai_title": {
        "en": "🤖 Ask the AI Assistant",
        "hi": "🤖 AI सहायक से पूछें",
    },
    "ai_placeholder": {
        "en": "e.g., How do I register as a voter? What is EVM?",
        "hi": "जैसे, मैं मतदाता के रूप में पंजीकरण कैसे करूँ? ईवीएम क्या है?",
    },
    "ai_send": {"en": "Ask Gemini ✨", "hi": "Gemini से पूछें ✨"},
    "ai_disclaimer": {
        "en": "💡 Powered by Google Gemini. Responses are AI-generated and may not reflect official ECI positions.",
        "hi": "💡 Google Gemini द्वारा संचालित। उत्तर AI-जनित हैं और आधिकारिक ECI स्थिति को प्रतिबिंबित नहीं कर सकते।",
    },

    # ── Footer ───────────────────────────────────────────────────────
    "footer_text": {
        "en": "Built with ❤️ for Indian Democracy • Powered by Google Gemini",
        "hi": "भारतीय लोकतंत्र के लिए ❤️ से बनाया गया • Google Gemini द्वारा संचालित",
    },

    # ── Sidebar ──────────────────────────────────────────────────────
    "sidebar_language": {"en": "🌐 Language", "hi": "🌐 भाषा"},
    "sidebar_theme": {"en": "🎨 Theme", "hi": "🎨 थीम"},
}


def t(key: str, lang: str = "en") -> str:
    """
    Translate a string key to the given language.

    Args:
        key: String identifier.
        lang: 'en' or 'hi'.

    Returns:
        Translated string, or the key itself if not found.
    """
    entry = _STRINGS.get(key)
    if entry is None:
        return key
    return entry.get(lang, entry.get("en", key))
