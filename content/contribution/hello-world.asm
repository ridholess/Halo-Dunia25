; Program "Hello World" dalam bahasa Assembly (x86-64)

section .data
    msg db 'Hello World', 0xa    ; pesan yang akan dicetak dengan baris baru
    len equ $ - msg              ; panjang pesan

section .text
    global _start

_start:
    ; System call untuk menulis ke stdout/tampilan (sys_write)
    mov rax, 1          ; ini nomor system call untuk write
    mov rdi, 1          ; file descriptor stdout
    mov rsi, msg        ; alamat pesan
    mov rdx, len        ; panjang pesan
    syscall             ; menjalankan system call

    ; System call untuk keluar dari program (sys_exit)
    mov rax, 60         ; nomor system call untuk keluar/exit
    mov rdi, 0          ; status keluar (0 = sukses)
    syscall             ; menjalankan system call

; Cara menjalankannya:
; nasm -f elf64 hello-world.asm
; ld hello-world.o -o hello-world
; ./hello-world
