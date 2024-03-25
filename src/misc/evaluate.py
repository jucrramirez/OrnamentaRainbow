def get_probability(cloud_coverage):

    if 0 <= cloud_coverage < 5:
        return 97
    if 5 <= cloud_coverage < 10:
        return 90
    if 10 < cloud_coverage < 15:
        return 80
    if 15 <= cloud_coverage < 20:
        return 75
    if 20 <= cloud_coverage < 25:
        return 60
    if 25 <= cloud_coverage < 30:
        return 50
    if cloud_coverage >= 30:
        return 0
    