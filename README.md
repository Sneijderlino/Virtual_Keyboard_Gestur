<p align="center">
  <img src="/img/demo.png" alt="Contoh output virtual keyboard gesture" width="800"/>
</p>



<p align="center">
  <img src="https://img.shields.io/badge/Pentest%20Tool-Automated-red?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/github/license/Sneijderlino/virtual_keyboard_gesture?style=for-the-badge"/>
</p>

<h1 align="center">🖐️ Virtual Keyboard Gesture</h1>
<p align="center">
  Ketik tanpa menyentuh keyboard — gunakan gerakan tangan dan suara untuk mengetik dan membaca teks.<br/>
  <em>Proyek edukatif berbasis Python + OpenCV + TTS. Cocok untuk eksplorasi CV dan interaksi manusia-komputer.</em>
</p>

---



## 🔎 Ringkasan

Virtual Keyboard Gesture adalah aplikasi Python yang memungkinkan pengguna mengetik menggunakan gerakan tangan. Dengan deteksi dua jari (jempol dan telunjuk), pengguna dapat memilih tombol virtual dan mengetik teks. Teks yang diketik dapat dibaca dengan suara menggunakan TTS.

---

## ✨ Fitur Utama

- Deteksi tangan menggunakan `cvzone.HandTrackingModule`.
- Keyboard virtual dengan tombol hover dan klik dua jari.
- Dukungan tombol SHIFT, SPACE, ENTER, dan DELETE.
- Output suara dengan `pyttsx3`.
- Efek suara klik dengan `winsound`.

---

## 📥 Cara Clone

```bash
git clone https://github.com/Sneijderlino/Virtual_Keyboard_Gestur.git
cd Virtual_Keyboard_Gestur
pip install -r requirements.txt
python main.py
```

### 🐉 Instalasi di Kali Linux
```bash
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip
pip3 install opencv-python cvzone pyttsx3
```

### 📱 Instalasi Termux (Android)
```bash
pkg update && pkg upgrade
pkg install python
pip install opencv-python cvzone pyttsx3 playsound
#⚠️Beberapa modul seperti cvzone dan akses kamera mungkin tidak berjalan langsung di Termux. Disarankan menggunakan Kali Linux via Termux + VNC Viewer untuk GUI dan akses penuh.
```


### 🪟 Windows
```bash
pip install opencv-python cvzone pyttsx3 winsound
#✅ Efek suara klik menggunakan winsound hanya tersedia di Windows.
```

# Virtual_Keyboard_Gestur
# Virtual_Keyboard_Gestur
