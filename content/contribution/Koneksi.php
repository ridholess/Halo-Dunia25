<?php
$koneksi = mysqli_connect("localhost", "root", "", "anu");

if (!$koneksi) {
    die("Koneksi gagal: " . mysqli_connect_error());
}
?>
