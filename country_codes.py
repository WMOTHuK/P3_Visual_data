from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):

    """Возвращает для заданной страны ее код Pygal, состоящий из 2 букв."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Slovak Republic':
            return 'sk'
        elif country_name == 'Moldova':
            return 'md'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Kyrgyz Republic':
            return 'kg'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Hong Kong SAR, China':
            return 'hk'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Dominica':
            return 'do'
        elif country_name == 'Bolivia':
            return 'bo'
        # Если страна не найдена, вернуть None.
    return None
    