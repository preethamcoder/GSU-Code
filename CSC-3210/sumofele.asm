.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword
.data
array_list WORD 10, 11, 13, 18, 21, 23, 24, 17, 45
sizeOAr = ($-array_list)/(TYPE array_list)
sum WORD 0
ind WORD 0
.code
main PROC
mov edx, OFFSET sum
mov esi, 0
mov ecx, sizeOAr
mov eax, 0
mov ebx, 0
mov ax, sum
mov bx, ind
L1:
	cmp esi, ecx
	jl L2
	jmp L4
L2:
	add ax, array_list[esi*4]
L3:
	inc esi
	jmp L1
L4:
	mov sum, ax
invoke ExitProcess,0
main endp
end main
