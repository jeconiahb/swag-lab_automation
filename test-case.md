### Test Case Login

#### Positive Test Cases (Login):
1. **Login dengan kredensial valid (standard_user)**
   - **Step**: Masukkan username "standard_user" dan password "secret_sauce".
   - **Expected Result**: Berhasil login dan diarahkan ke halaman inventori.
   - **Actual Result**: Berhasil login dan diarahkan ke halaman inventori.
   - **Status**: Passed

2. **Login dengan kredensial valid (problem_user)**
   - **Step**: Masukkan username "problem_user" dan password "secret_sauce".
   - **Expected Result**: Berhasil login dan diarahkan ke halaman inventori.
   - **Actual Result**: Berhasil login dan diarahkan ke halaman inventori.
   - **Status**: Passed

3. **Login dengan kredensial valid (performance_glitch_user)**
   - **Step**: Masukkan username "performance_glitch_user" dan password "secret_sauce".
   - **Expected Result**: Berhasil login, meskipun halaman mungkin memuat sedikit lebih lambat.
   - **Actual Result**: Berhasil login, halaman mungkin memuat sedikit lebih lambat.
   - **Status**: Passed

#### Negative Test Cases (Login):
1. **Login dengan username yang tidak valid**
   - **Step**: Masukkan username "invalid_user" dan password "secret_sauce".
   - **Expected Result**: Muncul pesan error "Username and password do not match".
   - **Actual Result**: Muncul pesan error "Username and password do not match".
   - **Status**: Passed

2. **Login dengan password yang tidak valid**
   - **Step**: Masukkan username "standard_user" dan password "invalid_password".
   - **Expected Result**: Muncul pesan error "Username and password do not match".
   - **Actual Result**: Muncul pesan error "Username and password do not match".
   - **Status**: Passed

3. **Login dengan username kosong**
   - **Step**: Biarkan kolom username kosong dan masukkan password "secret_sauce".
   - **Expected Result**: Muncul pesan error "Username is required".
   - **Actual Result**: Muncul pesan error "Username is required".
   - **Status**: Passed

4. **Login dengan password kosong**
   - **Step**: Masukkan username "standard_user" dan biarkan kolom password kosong.
   - **Expected Result**: Muncul pesan error "Password is required".
   - **Actual Result**: Muncul pesan error "Password is required".
   - **Status**: Passed

5. **Login dengan username dan password kosong**
   - **Step**: Biarkan kolom username dan password kosong.
   - **Expected Result**: Muncul pesan error "Username is required".
   - **Actual Result**: Muncul pesan error "Username is required".
   - **Status**: Passed

6. **Login dengan username dan password menggunakan kapitalisasi yang salah**
   - **Step**: Masukkan username "STANDARD_USER" dan password "SECRET_SAUCE".
   - **Expected Result**: Login gagal karena login case-insensitive.
   - **Actual Result**: gagal login meskipun kapitalisasi berbeda.
   - **Status**: Passed

#### Boundary Test Cases (Login):
1. **Login dengan username yang sangat panjang**
   - **Step**: Masukkan username dengan 100 karakter (misalnya "u" * 100) dan password "secret_sauce".
   - **Expected Result**: Sistem harus menampilkan pesan error atau menangani input dengan benar.
   - **Actual Result**: Tidak ada pesan error, login berhasil dengan username panjang.
   - **Status**: Passed

2. **Login dengan password yang sangat panjang**
   - **Step**: Masukkan username "standard_user" dan password dengan 100 karakter (misalnya "p" * 100).
   - **Expected Result**: Sistem harus menampilkan pesan error atau menangani input dengan benar.
   - **Actual Result**: Tidak ada pesan error, login berhasil dengan password panjang.
   - **Status**: Passed

3. **Login dengan username dan password satu karakter**
   - **Step**: Masukkan username "u" dan password "p".
   - **Expected Result**: Login harus gagal atau sistem harus menampilkan pesan error yang sesuai.
   - **Actual Result**: Login gagal dengan username dan password satu karakter.
   - **Status**: Passed

### Test Case Transaksi

#### Positive Test Cases (Transaksi):
1. **Melakukan transaksi dengan satu item**
   - **Step**: Login sebagai "standard_user", tambahkan item ke keranjang, lanjutkan ke checkout, masukkan informasi pelanggan, dan selesaikan transaksi.
   - **Expected Result**: Transaksi berhasil dan muncul pesan "THANK YOU FOR YOUR ORDER".
   - **Actual Result**: Transaksi berhasil dengan pesan "Thank you for your order!".
   - **Status**: Passed

2. **Melakukan transaksi dengan beberapa item**
   - **Step**: Login, tambahkan beberapa item ke keranjang, lanjutkan ke checkout, masukkan informasi pelanggan, dan selesaikan transaksi.
   - **Expected Result**: Transaksi berhasil dengan pesan "THANK YOU FOR YOUR ORDER".
   - **Actual Result**: Transaksi berhasil dengan pesan "Thank you for your order!".
   - **Status**: Passed

3. **Melakukan transaksi tanpa menambahkan item lalu kembali ke inventori**
   - **Step**: Login, langsung menuju keranjang tanpa menambahkan item, lalu kembali ke inventori.
   - **Expected Result**: Dapat kembali ke halaman inventori tanpa masalah.
   - **Actual Result**: Dapat kembali ke halaman inventori tanpa masalah.
   - **Status**: Passed

4. **Melakukan transaksi dengan memasukkan informasi pelanggan lengkap**
   - **Step**: Login, tambahkan item ke keranjang, lanjutkan ke checkout, masukkan informasi pelanggan lengkap (First name, Last name, ZIP code), dan selesaikan transaksi.
   - **Expected Result**: Transaksi berhasil dengan pesan "THANK YOU FOR YOUR ORDER".
   - **Actual Result**: Transaksi berhasil dengan pesan "Thank you for your order!".
   - **Status**: Passed

#### Negative Test Cases (Transaksi):
1. **Melakukan transaksi dengan informasi pelanggan yang tidak lengkap**
   - **Step**: Login, tambahkan item ke keranjang, lanjutkan ke checkout, masukkan hanya sebagian informasi pelanggan (misalnya hanya First Name tanpa ZIP code).
   - **Expected Result**: Muncul pesan error yang menyatakan bahwa informasi pelanggan harus lengkap.
   - **Actual Result**: Gagal melanjutkan transaksi, muncul pesan error yang menyatakan bahwa informasi pelanggan tidak lengkap.
   - **Status**: Passed

2. **Melakukan transaksi tanpa menambahkan item ke keranjang**
   - **Step**: Login, langsung menuju checkout tanpa menambahkan item ke keranjang.
   - **Expected Result**: Tidak dapat melanjutkan transaksi karena tidak ada item di keranjang.
   - **Actual Result**: Dapat melanjutkan transaksi karena keranjang kosong.
   - **Status**: Failed

3. **Membatalkan transaksi pada saat di halaman checkout**
   - **Step**: Login, tambahkan item ke keranjang, lanjutkan ke checkout, lalu klik "Cancel" di halaman checkout.
   - **Expected Result**: Kembali ke halaman keranjang dan transaksi dibatalkan.
   - **Actual Result**: Kembali ke halaman inventory dan transaksi dibatalkan.
   - **Status**: Passed

#### Boundary Test Cases (Transaksi):
1. **Melakukan transaksi dengan input nama depan dan nama belakang yang sangat panjang**
   - **Step**: Login, tambahkan item ke keranjang, lanjutkan ke checkout, masukkan nama depan dan nama belakang dengan 100 karakter (misalnya "FirstName" * 10 dan "LastName" * 10), serta ZIP code valid.
   - **Expected Result**: Sistem harus menangani input dengan benar atau menampilkan pesan error yang sesuai.
   - **Actual Result**: Tidak ada pesan error, transaksi berhasil dengan nama panjang.
   - **Status**: Failed

2. **Melakukan transaksi dengan ZIP code yang sangat panjang**
   - **Step**: Login, tambahkan item ke keranjang, lanjutkan ke checkout, masukkan nama depan dan nama belakang yang valid, dan ZIP code dengan 10 karakter (misalnya "1234567890").
   - **Expected Result**: Sistem harus menangani input dengan benar atau menampilkan pesan error yang sesuai.
   - **Actual Result**: Tidak ada pesan error, transaksi berhasil dengan ZIP code panjang.
   - **Status**: Failed

3. **Melakukan transaksi dengan nama depan dan nama belakang kosong**
   - **Step**: Login, tambahkan item ke keranjang, lanjutkan ke checkout, biarkan kolom nama depan dan nama belakang kosong, dan masukkan ZIP code.
   - **Expected Result**: Muncul pesan error yang menyatakan bahwa nama depan dan nama belakang diperlukan.
   - **Actual Result**: Gagal melanjutkan transaksi, muncul pesan error bahwa nama depan dan nama belakang diperlukan.
   - **Status**: Passed

### Ringkasan:
- **Positive Test Cases (Login)**: Semua tes berhasil.
- **Negative Test Cases (Login)**: Semua tes berhasil.
- **Boundary Test Cases (Login)**: Beberapa tes gagal.
- **Positive Test Cases (Transaksi)**: Semua tes berhasil.
- **Negative Test Cases (Transaksi)**: Semua tes berhasil
- **Boundary Test Cases (Transaksi)**: Beberapa tes gagal.
.
