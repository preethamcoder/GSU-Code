;Preetham Thelluri
;Class: CSC 3210
;Assignment#: 4
;Description: This program checks if the MSB of the Al register is set and divides it by 8 if it is set or divides it by 4 if it isn't
.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword
.data
.code
main PROC
mov eax, 0
mov ebx, 0
mov al, 88h
mov bl, 10000000b
test al, bl
jnz L1
shl al, 2
L1:
	shr al, 3
invoke ExitProcess,0
main endp
end main