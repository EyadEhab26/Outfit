def generate_outfit(item_type):
    outfits = {
        "T-shirt": "جينز + كوتشي",
        "Pants": "قميص + حذاء",
        "Jacket": "تيشرت + جينز",
        "Shoes": "لبس كاجوال"
    }
    return outfits.get(item_type, "Simple outfit")
