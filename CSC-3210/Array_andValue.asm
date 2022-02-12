;Name Preetham Thelluri
;Class: CSC3210
;Assignment#: 3
;Description: This program attempts to decalre an array and update certain values in it, element by element.
.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword
.data
x WORD 10
y WORD 15
r WORD 4
z DWORD 3 DUP(?) 
.code
main proc
movzx eax, x
movzx ebx, y
movzx edx, r
mov edi, OFFSET z
mov z, 130
add z, eax
add z+4, eax
add z+4, ebx
mov ecx, z
sub z+4, ecx
add z+8, edx
add z+8, eax
sub z+8, 13
invoke ExitProcess,0
main endp
end main
