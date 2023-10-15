# TODO Найдите количество книг, которое можно разместить на дискете
obiem_disketi = 1.44 * 1024 * 1024 # TODO Обьем дискеты в байтах
kol_vo_stranic_v_knige = 100
strok_na_stranice = 50
kolv_vo_simvol_v_stroke = 25
obiem_simvola = 4
obiem_knigi = obiem_simvola * kolv_vo_simvol_v_stroke * strok_na_stranice * kol_vo_stranic_v_knige
kol_vo_knig = obiem_disketi // obiem_knigi
print("Количество книг, помещающихся на дискету:", int(kol_vo_knig))

