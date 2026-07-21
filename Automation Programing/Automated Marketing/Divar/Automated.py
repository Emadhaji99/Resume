import requests
import arabic_reshaper
from bidi.algorithm import get_display


def rtl(text):
    """
    تبدیل متن فارسی/عربی به حالت راست به چپ
    برای نمایش درست در ترمینال
    """
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

#--------------------------------------

def build_car_search_url(
    city="tehran",
    business_type=None,
    min_price=None,
    max_price=None,
    min_year=None,
    max_year=None,
    keyword=None,
    recent_ads=None,
    min_usage=None,
    max_usage=None
    ):
    base = f"https://divar.ir/s/{city}/car"
    params = []

    if business_type:
        params.append(f"business-type={business_type}%2C")
    if min_price and max_price:
        params.append(f"price={min_price}-{max_price}")
    if min_year and max_year:
        params.append(f"production-year={min_year}-{max_year}")
    if keyword:
        params.append(f"q={keyword}")
    if recent_ads:
        params.append(f"recent_ads={recent_ads}")
    if min_usage and max_usage:
        params.append(f"usage={min_usage}-{max_usage}")

    if params:
        return base + "?" + "&".join(params)
    return base


# -----------------------------
# گرفتن ورودی از کاربر
# -----------------------------

city = "tehran"
business_type = "personal,"
min_price = 100000000
max_price = 850000000
min_year = 1390
max_year = 1405
recent_ads = "3h"
min_usage = 10000
max_usage = 200000

# تبدیل رشته‌های عددی به None اگر خالی باشند
min_price = int(min_price) if min_price else None
max_price = int(max_price) if max_price else None
min_year = int(min_year) if min_year else None
max_year = int(max_year) if max_year else None
min_usage = int(min_usage) if min_usage else None


car_List=["سمند","پرشیا","رانا"]
for car in car_List:
    url = build_car_search_url(
        city=city,
        business_type=business_type,
        min_price=min_price,
        max_price=max_price,
        min_year=min_year,
        max_year=max_year,
        keyword=car,
        recent_ads=recent_ads,
        min_usage=min_usage,
        max_usage=max_usage
    )
    print(rtl("\nURL ساخته شد:"))
    print(url)
    



#--------------------

