#1 Write a PYTHON program to evaluate the student performance
#Menggunakan function
def evaluate_performance(percentage):   #fungsi untuk evaluasi performa berdasarkan persentase students
    if percentage >= 90:        #jika nilai persentase lebih dari sama dengan 90 maka outputnya Excellent performance
        print ("Excellent performance")
    elif percentage >= 80:      #jika nilai persentase lebih dari sama dengan 80 maka outputnya Very Good performance
        print ("Very Good performance")
    elif percentage >= 70:      #jika nilai persentase lebih dari sama dengan 70 maka outputnya Good performance
        print ("Good performance")
    elif percentage >= 60:      #jika nilai persentase lebih dari sama dengan 60 maka outputnya Average performance
        print ("Average performance")
        
percentage = float(input("Enter the student's percentage: "))   #meminta pengguna untuk memasukkan nilai persentase siswa melalui input dengan tipe data float agar bisa menerima bilangan desimal.
print(evaluate_performance(percentage))

#2 Find the Largest of Three Numbers
def find_largest(a, b, c):  #fumgsi ini digunakan untuk menemukan angka terbesar di antara tiga nilai yang diberikan sebagai input.
    if a >= b and a >= c:   #Jika a lebih besar atau sama dengan b dan c, maka a adalah angka terbesar, sehingga dikembalikan.
        return a
    elif b >= a and b >= c: #Jika b lebih besar atau sama dengan a dan c, maka return b.
        return b
    else:
        return c    #Jika tidak ada yang memenuhi kondisi sebelumnya, maka c adalah yang terbesar, sehingga kita mengembalikannya.

# Input: three numbers
a = float(input("Enter the first number: "))    #input angka pertama 
b = float(input("Enter the second number: "))   #input angka kedua
c = float(input("Enter the third number: "))    #input angka ketiga

# Output: largest number
print("The largest number is:", find_largest(a, b, c)) #output dari hasil yang dicetak adalah angka terbesar di antara tiga nilai yang telah dimasukkan

#3 Write a PYTHON program to print Fibonacci series up to n
def fibonacci(n):       #Fungsi ini untuk menghasilkan deret Fibonacci hingga batas tertentu yang diberikan.
    fib_series =[]      # List ini digunakan untuk menyimpan angka-angka dari deret Fibonacci yang dihasilkan.
    a, b = 0, 1         #Ini digunakan untuk memberikan nilai awal (0 dan 1) pada dua variabel, yaitu a dan b.
    while a <= n:       #loop while digunakan untuk mengulangi blok kode di dalamnya selama kondisi a <= n terpenuhi.
        fib_series.append(a)    #Menambahkan nilai a ke dalam list fib_serie
        a, b = b, a + b     #Digunakan untuk memperbarui nilai variabel a dan b dalam setiap iterasi untuk menghasilkan angka Fibonacci berikutnya.
    return fib_series       #Mengembalikan deret Fibonacci yang sudah lengkap kepada pemanggil fungsi.
n = int(input("Masukkan jumlah angka Fibonacci yang ingin dicetak: "))   #Meminta pengguna memasukkan angka n yang menunjukkan batas deret Fibonacci yang ingin dicetak.
print("fibbonacci series up to", n, ":", fibonacci(n))                   #Hasilnya akan dicetak dengan format yang menampilkan pesan "fibonacci series up to" diikuti oleh nilai n dan deret Fibonacci yang dihasilkan.

#4 Function to print odd numbers up to n
def print_odd_numbers(n):       #Mendefinisikan fungsi untuk mencetak semua angka ganjil dari 1 hingga n
    odd_numbers = [i for i in range(1, n + 1) if i % 2 != 0]        #Digunakan untuk membuat sebuah list (daftar) yang berisi semua angka ganjil dari 1 hingga n dengan menggunakan operator modulus %, kita memeriksa apakah i adalah angka ganjil. Jika i dibagi 2 dan sisa bagi (modulus) tidak sama dengan 0, maka i adalah angka ganjil.
    return odd_numbers          #Untuk mengembalikan list yang berisi angka ganjil dari fungsi kepada pemanggil.

# Input: n value
n = int(input("Enter the value of n: "))    #input dari pengguna

# Output: odd numbers up to n
print("Odd numbers up to", n, ":", print_odd_numbers(n))        #Digunakan untuk mencetak daftar angka ganjil dari 1 hingga n dengan menggabungkan fungsi print() dan fungsi yang telah didefinisikan sebelumnya, yaitu print_odd_numbers(n)

#5 Function to print the pattern
def print_pattern(n):       #Mendefinisikan fungsi dengan nama print_pattern yang menerima parameter n.
    for i in range(1, n+1): #Cara untuk mencetak pola angka berdasarkan nilai n yg diberikan
        # Print the number i, i times
        print((str(i) + " ") * i)       #berfungsi untuk mencetak angka i sebanyak i kali, di mana setiap angka diikuti oleh spasi

n = int(input("Enter a value for n: "))     #input nilai dari pengguna
print_pattern(n)                            #Call the function to print the pattern