import numpy as np

def calculate_distance(city1, city2):
    # Fungsi ini menghitung jarak antara dua kota menggunakan metode Euclidean
    x1, y1 = city1
    x2, y2 = city2
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_nearest_neighbor(current_city, unvisited_cities):
    # Fungsi ini mencari kota terdekat dari kota saat ini
    nearest_city = None
    min_distance = float('inf')

    for city in unvisited_cities:
        distance = calculate_distance(current_city, city)
        if distance < min_distance:
            min_distance = distance
            nearest_city = city

    return nearest_city

def tsp_approximation(cities):
    start_city = cities[0]  # Memilih kota awal
    unvisited_cities = cities[1:]  # Daftar kota yang belum dikunjungi
    current_city = start_city
    tour = [current_city]  # Inisialisasi tur dengan kota awal

    while unvisited_cities:
        nearest_city = find_nearest_neighbor(current_city, unvisited_cities)
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city

    tour.append(start_city)  # Kembali ke kota awal untuk melengkapi tur

    return tour

# Contoh penggunaan
cities = [(0, 0), (1, 5), (2, 3), (5, 2), (6, 4)]
tour = tsp_approximation(cities)

print("Tur Perjalanan:", tour)
