.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword
.data
array_list WORD 10, 11, 13, 18, 21, 23, 24, 17, 45
sizeOAr = ($-array_list)/(TYPE array_list)
sum WORD 0
.code
main PROC
mov esi, 0
mov esi, OFFSET array_list
mov ecx, sizeOAr
mov eax, 0
mov ebx, WORD
mov ax, sum
L1:
	add ax, [esi]
	add esi, ebx
LOOP L1
invoke ExitProcess,0
main endp
end main
