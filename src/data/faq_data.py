"""
FAQ data — bilingual frequently asked questions.
"""

from __future__ import annotations


def get_faqs(lang: str = "en") -> list[dict]:
    """Return FAQ entries."""
    if lang == "hi":
        return [
            {"q": "मतदाता पहचान पत्र कैसे बनवाएँ?",
             "a": "voters.eci.gov.in पर जाएँ → Form 6 भरें → दस्तावेज़ अपलोड करें → BLO सत्यापन के बाद EPIC कार्ड प्राप्त करें। आप Voter Helpline App भी उपयोग कर सकते हैं।"},
            {"q": "क्या मैं बिना वोटर आईडी के वोट कर सकता/सकती हूँ?",
             "a": "हाँ! आप 12 अनुमोदित दस्तावेज़ों में से कोई भी उपयोग कर सकते हैं — आधार कार्ड, पासपोर्ट, ड्राइविंग लाइसेंस, पैन कार्ड आदि।"},
            {"q": "NOTA क्या है?",
             "a": "NOTA (None Of The Above) — यदि आप किसी भी उम्मीदवार से संतुष्ट नहीं हैं तो NOTA बटन दबा सकते हैं। यह 2013 में शुरू हुआ।"},
            {"q": "EVM क्या है और क्या यह सुरक्षित है?",
             "a": "EVM (Electronic Voting Machine) एक स्टैंडअलोन डिवाइस है जो इंटरनेट से कनेक्ट नहीं होती। इसमें VVPAT सत्यापन होता है और इसे हैक करना लगभग असंभव माना जाता है।"},
            {"q": "मतदान के दिन छुट्टी मिलती है?",
             "a": "हाँ, मतदान दिवस पर सवैतनिक अवकाश (paid holiday) होता है। कर्मचारी मतदान के लिए समय ले सकते हैं।"},
            {"q": "विदेश में रहकर क्या मैं वोट कर सकता/सकती हूँ?",
             "a": "हाँ, NRI मतदाता Form 6A भरकर अपना नाम मतदाता सूची में जुड़वा सकते हैं। वोट देने के लिए भारत आना आवश्यक है।"},
            {"q": "चुनाव आचार संहिता (MCC) क्या है?",
             "a": "MCC वह नियमावली है जो चुनाव घोषणा के बाद सभी पार्टियों और सरकार पर लागू होती है। इसके तहत सरकार नई योजनाएँ घोषित नहीं कर सकती।"},
            {"q": "चुनाव में कितना खर्च कर सकते हैं?",
             "a": "लोकसभा: ₹95 लाख, विधानसभा: ₹40 लाख (राज्य अनुसार भिन्न)। सीमा से अधिक खर्च करने पर अयोग्यता हो सकती है।"},
        ]

    return [
        {"q": "How do I get a Voter ID card?",
         "a": "Visit voters.eci.gov.in → Fill Form 6 → Upload documents → After BLO verification, receive your EPIC card. You can also use the Voter Helpline App on mobile."},
        {"q": "Can I vote without a Voter ID?",
         "a": "Yes! You can use any of 12 approved documents — Aadhaar card, Passport, Driving License, PAN card, etc."},
        {"q": "What is NOTA?",
         "a": "NOTA (None Of The Above) — if you are not satisfied with any candidate, you can press the NOTA button. Introduced in 2013 via Supreme Court directive."},
        {"q": "What is an EVM and is it secure?",
         "a": "An EVM (Electronic Voting Machine) is a standalone device with no internet connectivity. It has VVPAT verification and is considered nearly impossible to hack."},
        {"q": "Do I get a holiday on polling day?",
         "a": "Yes, polling day is a paid holiday. Employees are entitled to time off to cast their vote."},
        {"q": "Can NRIs vote in Indian elections?",
         "a": "Yes, NRIs can register by filling Form 6A to add their name to the electoral roll. However, they must be physically present in India to vote."},
        {"q": "What is the Model Code of Conduct (MCC)?",
         "a": "The MCC is a set of rules that applies to all parties and the government once elections are announced. The government cannot announce new schemes during MCC."},
        {"q": "How much can a candidate spend on elections?",
         "a": "Lok Sabha: ₹95 lakh, Assembly: ₹40 lakh (varies by state). Exceeding the limit can lead to disqualification."},
    ]
