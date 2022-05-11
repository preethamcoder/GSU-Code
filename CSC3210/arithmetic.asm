; Student name: Preetham Thelluri
; Class: CSC3210
; Assignment#: 2
; Description: This program attempts to evaluate AL = (val3 + 7) - (val2 + val1) + (5/3)*7, where val1 = 12, val2 = 9, and val3 = 2.

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
val1 BYTE 12
val2 BYTE 9
val3 BYTE 2
.code
main proc
	mov eax, 0
	mov ebx, 0
	mov ecx, 0
	mov edx, 0
	mov bl, val3
	add bl, 7
	mov cl, val2
	add cl, val1
	sub bl, cl
	mov al, bl
	add al, (5/3)*7
invoke ExitProcess,0
main endp
end main
