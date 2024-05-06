# TASK1
# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
#   for eded in mylist:
#     if eded >= 0:  
#         kok = eded ** 0.5
#         if kok.is_integer():  
#             print("Ədədin Kökaltısı:", kok)
#         else:
#             print("Kökaltısı yoxdur")
#     else:
#         print("Kökaltısı yoxdur")
# ................................................................................................................................
# TASK 2
# def tekrarlanmayan_elementleri_tap(input_list):
#     unique_elements = []  
#     for element in input_list:
#         if input_list.count(element) == 1:  
#             unique_elements.append(element)  
#     return unique_elements
# test_list = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 10]
# print("Tekrarlanmayan Elementlər:")
# print(tekrarlanmayan_elementleri_tap(test_list))
# ...............................................................................................................................
# TASK 3
# def vurma(giris):
#     hasil = 1
#     for simvol in giris:
#         if simvol.isdigit():  
#             hasil *= int(simvol)
#     return hasil
# giris = input("Rəqəmləri daxil edin: ")
# print("Rəqəmlərin Bir-birlərinə Hasili:", vurma(giris))
# ..................................................................................................................................
# TASK 4
# mylist = ['may', 'iyun', 'iyul']
# ay_uzunlugu = {ay: len(ay) for ay in mylist}
# print(ay_uzunlugu)
# .................................................................................................................................
# TASK 5
# def adlar_kicik(ad):
#     return [ad.split()[0].lower() for ad in ad]
# ad = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# adlar = adlar_kicik(ad)
# print(adlar)
# ...................................................................................................................................
# TASK 6

def ededi_orta(nums1, nums2):
    results = [(nums1[i] + nums2[i]) / 2 for i in range(len(nums1))]
    return results
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
results = ededi_orta(nums1, nums2)
