import random

# Karakter sınıfı
class Character:
    def __init__(self, name, strength, intelligence, agility):
        self.name = name
        self.strength = strength  # Fiziksel güç
        self.intelligence = intelligence  # Zeka
        self.agility = agility  # Çeviklik
        self.mood = "neutral"  # Başlangıç ruh hali
        self.score = 0  # Başlangıç puanı

    def add_task(self, task, difficulty):
        self.tasks.append({"task": task, "difficulty": difficulty})

    def respond_to_task(self, task):
        # Görev zorluk seviyesine göre ruh halini belirleyelim
        if task["difficulty"] == "easy":
            self.mood = "calm"
            return f"{self.name}: Tamam, bu çok kolay. Hadi yapalım!"
        elif task["difficulty"] == "medium":
            self.mood = "neutral"
            return f"{self.name}: Hmm, bu zorlu ama halledebiliriz."
        else:
            self.mood = "angry"
            return f"{self.name}: Bu çok zor! Neden bana bu kadar zor bir şey veriyorsunuz?!"

    def calculate_task_result(self, task):
        # Görevin başarılı olup olmadığını hesaplayalım
        success_chance = 0
        if task["difficulty"] == "easy":
            success_chance = 80  # Kolay görevlerde başarı şansı yüksek
        elif task["difficulty"] == "medium":
            success_chance = 60  # Orta zorluktaki görevlerde başarı şansı daha düşük
        else:
            success_chance = 40  # Zor görevlerde başarı şansı düşük

        # Karakterin özelliklerine göre başarı şansı arttırılabilir
        if self.strength > 5:
            success_chance += 5
        if self.intelligence > 5:
            success_chance += 5
        if self.agility > 5:
            success_chance += 5

        # Başarı oranına göre sonuç belirleniyor
        if random.randint(1, 100) <= success_chance:
            return True
        return False

    def update_score(self, success):
        if success:
            self.score += 10  # Başarı durumunda 10 puan eklenir
        else:
            self.score -= 5  # Başarısızlık durumunda 5 puan kaybedilir

    def show_score(self):
        return f"{self.name}'in puanı: {self.score}"

# Karakterlerin oluşturulması (Fiziksel güç, zeka, çeviklik)
jack = Character("Jack", strength=7, intelligence=6, agility=5)
hans = Character("Hans", strength=6, intelligence=7, agility=6)
winston = Character("Winston", strength=5, intelligence=8, agility=6)

jack.tasks = []
hans.tasks = []
winston.tasks = []

# Görevlerin tanımlanması (zorluklarıyla birlikte)
jack.add_task("No Man's Land'de keşif yap.", "hard")
jack.add_task("Müttefik askerlerine moral ver.", "easy")
jack.add_task("Yaralı askerlere yardım et.", "medium")

hans.add_task("Düşman mevzilerini gözlemle.", "medium")
hans.add_task("Bomba tahkimatı yap.", "hard")
hans.add_task("Haber alma görevine git.", "easy")

winston.add_task("İletişim hattını onar.", "easy")
winston.add_task("Hava durumu raporu al.", "medium")
winston.add_task("Askerler arasında bilgi paylaşımı sağla.", "hard")

# Kullanıcının verdiği görevi karakterlere vermek
def assign_task_to_character(character, task, difficulty):
    task_dict = {"task": task, "difficulty": difficulty}
    print(f"\nVerilen Görev: {task_dict['task']}")
    print(character.respond_to_task(task_dict))

    # Görevin başarılı olup olmadığını hesapla
    success = character.calculate_task_result(task_dict)

    # Sonuçları ekrana yazdır
    if success:
        print(f"{character.name}: Görev başarıyla tamamlandı!")
        character.update_score(True)
    else:
        print(f"{character.name}: Görev başarısız oldu.")
        character.update_score(False)

    # Karakterin güncel puanını göster
    print(character.show_score())

# Ana oyun döngüsü
def game():
    print("Oyun Başlıyor...\n")
    
    characters = [jack, hans, winston]
    
    while True:
        print("\nKime görev vermek istersiniz?")
        print("1. Jack")
        print("2. Hans")
        print("3. Winston")
        
        choice = input("Bir karakter seçin (1/2/3): ")
        
        if choice == "1":
            character = jack
        elif choice == "2":
            character = hans
        elif choice == "3":
            character = winston
        else:
            print("Geçersiz seçim! Lütfen 1, 2 veya 3'ü seçin.")
            continue
        
        task = input(f"\n{character.name}'e vermek istediğiniz görevi girin: ")
        difficulty = input("Görev zorluğunu girin (easy, medium, hard): ").lower()
        
        if difficulty not in ["easy", "medium", "hard"]:
            print("Geçersiz zorluk seviyesi! Lütfen 'easy', 'medium' veya 'hard' girin.")
            continue
        
        assign_task_to_character(character, task, difficulty)
        
        # Oyuncuya tekrar görev vermek isteyip istemediğini soralım
        cont = input("\nYeni bir görev vermek ister misiniz? (Evet/Hayır): ").lower()
        if cont != "evet":
            print("Oyun bitti. Teşekkürler!")
            break

# Oyunu başlat
game()
